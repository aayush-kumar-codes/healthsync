# HealthSync ![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Version](https://img.shields.io/badge/version-1.0.0-blue)

## Project Description
HealthSync is a web application that aggregates health data from various wearable devices and provides users with personalized insights and recommendations. It allows users to securely share their health information with healthcare providers, facilitating better health management and communication.

## Features
- 📊 Real-time health data integration from various wearable devices
- 🤖 Personalized health insights and recommendations using AI
- 🔒 Secure sharing of health data with healthcare providers

## Tech Stack
### Frontend
- **Next.js** 🌐

### Backend
- **FastAPI** 🚀
- **LangChain** 📚
- **OpenAI** 🤖

### Database
- **PostgreSQL** 🗄️

## Installation
To set up the project locally, follow these steps:

- Clone the repository
bash
git clone https://github.com/aayush-kumar-codes/healthsync
- Navigate to the project directory
bash
cd healthsync
- Create a virtual environment
bash
python -m venv venv
- Activate the virtual environment
bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
- Install the required dependencies
bash
pip install -r requirements.txt
- Set up the PostgreSQL database and update the connection settings in the `.env` file

## Usage
To start the development server, run the following command:
bash
uvicorn main:app --reload
Visit `http://localhost:8000` in your browser to access the application.

## API Documentation
For detailed API documentation, please refer to the [API Docs](https://github.com/aayush-kumar-codes/healthsync/wiki/API-Documentation).

## Testing
To run the tests, execute the following command:
bash
pytest
## Deployment
For deploying the application, follow these steps:

- Build the application
bash
npm run build
- Start the production server
bash
uvicorn main:app --host 0.0.0.0 --port 80
## Contributing
We welcome contributions! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Make your changes and commit them (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

Thank you for your interest in contributing to HealthSync!