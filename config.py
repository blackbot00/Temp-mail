import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    MONGO_URL = os.getenv("MONGO_URL")
    UPI_ID = os.getenv("UPI_ID")
    QR_URL = os.getenv("QR_IMAGE_URL")
    
    # Plans
    PLANS = {
        "1_week": "29",
        "1_month": "49",
        "3_month": "79"
  }
  
