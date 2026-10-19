import shutil
import pytesseract
from PIL import Image

def extract_text(image):
    tesseract_path = shutil.which("tesseract")

    if not tesseract_path:
        raise FileNotFoundError(
            "Tesseract OCR is not installed. "
            "Check that packages.txt contains tesseract-ocr."
        )

    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    text = pytesseract.image_to_string(image)
    words = text.split()

    return {
        "text": text,
        "words": words
    }
