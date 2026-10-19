
import os
import shutil
import pytesseract
from PIL import Image


def extract_text(image):
    # Find Tesseract on the current system
    tesseract_path = shutil.which("tesseract")

    if tesseract_path:
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
    elif os.name == "nt":
        # Local Windows installation
        windows_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        if os.path.exists(windows_path):
            pytesseract.pytesseract.tesseract_cmd = windows_path
        else:
            raise FileNotFoundError(
                "Tesseract OCR is not installed or not found."
            )
    else:
        raise FileNotFoundError(
            "Tesseract OCR was not found. Check packages.txt."
        )

    text = pytesseract.image_to_string(image)
    words = text.split()

    return {
        "text": text,
        "words": words
    }
