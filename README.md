Lab Report Processing API Setup and Usage
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/Keerthana2702/Lab_report_api.git
cd Lab_report_api
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
3. Activate the Virtual Environment
On Windows:

bash
Copy
Edit
venv\Scripts\activate
On macOS/Linux:

bash
Copy
Edit
source venv/bin/activate
4. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
5. Install Tesseract OCR
Windows: Download and Install

macOS: brew install tesseract

Linux: sudo apt install tesseract-ocr

6. Configure Tesseract Path (If Needed)
Add this to the Python code if Tesseract is not in your PATH:

python
Copy
Edit
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows path
7. Run the API
bash
Copy
Edit
uvicorn main:app --reload
This will start the server at http://127.0.0.1:8000.

8. Test the API
Use Postman or any HTTP client to send a POST request to http://127.0.0.1:8000/get-lab-tests with a lab report image (PNG/JPG) in the body.

Example Request:
URL: http://127.0.0.1:8000/get-lab-tests

Method: POST

Body: file (image file, PNG/JPG)

9. Expected JSON Response
json
Copy
Edit
{
  "tests": [
    {
      "test_name": "Blood Pressure",
      "value": "120/80 mmHg",
      "reference_range": "90/60 - 140/90 mmHg"
    },
    {
      "test_name": "Cholesterol",
      "value": "200 mg/dL",
      "reference_range": "150-200 mg/dL"
    }
  ]
}
