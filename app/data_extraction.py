import subprocess
import os

def extract_android_data():
    # Define the path to save the extracted data
    local_path = "./data/"

    # Ensure the local directory exists
    if not os.path.exists(local_path):
        os.makedirs(local_path)

    # Define the adb command to pull the file from the device
    command = ["adb", "pull", "/sdcard/WhatsApp/Databases/msgstore.db", local_path]

    # Execute the command
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Output:", result.stdout.decode())
        print("Error:", result.stderr.decode())
        return "Data extraction successful."
    except subprocess.CalledProcessError as e:
        print("Error occurred:", e.stderr.decode())
        return "Data extraction failed."