import os
import shutil
import schedule
import time
from datetime import datetime

# Define the directory where backups will be stored
backup_directory = "C:/var/lib/mysql/backups"

def perform_backup():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  

    # Create backup directory with timestamp
    data_backup_dir = os.path.join(backup_directory, f"data_backup_{timestamp}")
    os.makedirs(data_backup_dir, exist_ok=True)
    try:
        
        shutil.copytree("/var/lib/mysql", data_backup_dir) 
        print(f"Data backup created at: {data_backup_dir}")
    except FileExistsError:
        print(f"Backup directory {data_backup_dir} already exists. Skipping backup.")

#
schedule.every().day.at("3:00").do(perform_backup)


while True:
    schedule.run_pending()
    time.sleep(60)
