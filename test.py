import os
import requests

# Define the folder path containing the images
folder_path = r'C:\Users\Home\Desktop\Keerthana\lab_report_api\lab_images'

# FastAPI URL for testing
url = 'http://127.0.0.1:8000/get-lab-tests'

# Iterate over all image files in the directory
for filename in os.listdir(folder_path):
    if filename.endswith(('.png', '.jpg', '.jpeg')):  # Filter image files
        image_path = os.path.join(folder_path, filename)
        
        with open(image_path, 'rb') as image_file:
            files = {'file': (filename, image_file, 'image/jpeg')}  # 'image/jpeg' is a generic MIME type, change it accordingly
            response = requests.post(url, files=files)
            
            if response.status_code == 200:
                print(f"Successfully processed {filename}:")
                print(response.json())  # Print the extracted lab test data
            else:
                print(f"Failed to process {filename}: {response.status_code}")

