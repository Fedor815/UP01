import asyncio
from parsers.medical_parser import MedicalParser
from utils.database import Database
from utils.notifications import TelegramNotifier

async def main():
    db = Database()
    notifier = TelegramNotifier()
    parser = MedicalParser(db=db, notifier=notifier)
    
    try:
        await parser.run()
    except Exception as e:
        await notifier.send_error(f"Parser error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())