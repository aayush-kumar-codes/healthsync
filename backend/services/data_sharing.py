from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import User, HealthData, Provider
from database import get_db
from security import get_current_user
from pydantic import BaseModel
import json
import os
from langchain import OpenAI

router = APIRouter()

class ShareHealthDataRequest(BaseModel):
    provider_id: int
    data: dict

@router.post("/share_health_data")
async def share_health_data(request: ShareHealthDataRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        provider = db.query(Provider).filter(Provider.id == request.provider_id).first()
        if not provider:
            raise HTTPException(status_code=404, detail="Provider not found")

        health_data = HealthData(user_id=current_user.id, provider_id=request.provider_id, data=json.dumps(request.data))
        db.add(health_data)
        db.commit()
        db.refresh(health_data)

        # Optionally, notify the provider or log the sharing event
        notify_provider(provider, health_data)

        return {"message": "Health data shared successfully", "health_data_id": health_data.id}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def notify_provider(provider, health_data):
    try:
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OpenAI API key not set")

        openai_client = OpenAI(api_key=openai_api_key)
        message = f"User {health_data.user_id} has shared health data with you."
        openai_client.send_message(provider.contact_info, message)
    except Exception as e:
        print(f"Failed to notify provider: {str(e)}")