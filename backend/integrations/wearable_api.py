from fastapi import APIRouter, HTTPException
import requests
import os

router = APIRouter()

WEARABLE_API_URLS = {
    "fitbit": "https://api.fitbit.com/1/user/-/activities/date/{date}.json",
    "garmin": "https://api.garmin.com/wellness-api/rest/user/{user_id}/activities",
    "apple_health": "https://api.apple.com/health/v1/user/{user_id}/activities"
}

class WearableAPIError(Exception):
    pass

def fetch_fitbit_data(date: str, access_token: str):
    url = WEARABLE_API_URLS["fitbit"].format(date=date)
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise WearableAPIError("Failed to fetch data from Fitbit API")
    return response.json()

def fetch_garmin_data(user_id: str, access_token: str):
    url = WEARABLE_API_URLS["garmin"].format(user_id=user_id)
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise WearableAPIError("Failed to fetch data from Garmin API")
    return response.json()

def fetch_apple_health_data(user_id: str, access_token: str):
    url = WEARABLE_API_URLS["apple_health"].format(user_id=user_id)
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise WearableAPIError("Failed to fetch data from Apple Health API")
    return response.json()

@router.get("/wearable/{device}/{user_id}")
async def get_wearable_data(device: str, user_id: str, date: str = None):
    access_token = os.getenv("WEARABLE_ACCESS_TOKEN")
    if device == "fitbit":
        if not date:
            raise HTTPException(status_code=400, detail="Date is required for Fitbit data")
        return fetch_fitbit_data(date, access_token)
    elif device == "garmin":
        return fetch_garmin_data(user_id, access_token)
    elif device == "apple_health":
        return fetch_apple_health_data(user_id, access_token)
    else:
        raise HTTPException(status_code=404, detail="Device not supported")