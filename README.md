# AI Image Text Analyzer

An image text extraction application built using Python, Streamlit, and Tesseract OCR.

## Features

- Upload PNG, JPG, and JPEG images.
- Extract readable text from images using OCR.
- Display extracted text in the application.
- Calculate average OCR confidence.
- Count recognized words.
- Convert text into numerical TF-IDF vectors.
- Classify OCR confidence as High, Medium, or Low.
- Download extracted text as a text file.

## Technologies Used

- Python
- Streamlit
- Pillow
- Pytesseract
- Tesseract OCR
- Scikit-learn

## Project Structure

```text
AI-Image-Text-Analyzer/
├── app.py
├── ocr.py
├── attention.py
├── embedding.py
├── requirements.txt
├── packages.txt
└── README.md
```

## Installation

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Install the Tesseract OCR engine separately.

On Windows, configure its executable path in the application.

## Run the Application

```bash
streamlit run app.py
```

## Limitations

- OCR accuracy depends on image quality.
- Blurry images may produce incorrect text.
- OCR confidence does not guarantee that every word is correct.
- TF-IDF vectors are numerical text representations, not contextual AI embeddings.

## Future Improvements

- Integrate OCR, confidence analysis, and text embeddings.
- Add image preprocessing.
- Support multiple OCR languages.
- Deploy the application online.
