from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import io
import re

# 👉 Set the tesseract path manually
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = FastAPI()

@app.post("/get-lab-tests")
async def get_lab_tests(file: UploadFile = File(...)):
    # 1. Read image
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))
    image = image.convert('L')  # Grayscale

    # 2. Extract text
    text = pytesseract.image_to_string(image)

    # 3. Extract test info
    tests = []
    lines = text.split("\n")
    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Example pattern: Hemoglobin  13.5  11.5 - 15.5
        match = re.match(r"([A-Za-z\s]+)\s+([\d\.]+)\s+([\d\.\-\s]+)", line)
        if match:
            tests.append({
                "test_name": match.group(1).strip(),
                "value": match.group(2).strip(),
                "reference_range": match.group(3).strip()
            })

    return JSONResponse(content={"tests": tests})
