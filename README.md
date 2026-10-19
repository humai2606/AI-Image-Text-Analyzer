# AI Image Text Analyzer

An AI-powered image text analysis application built using Python and Streamlit. It uses Tesseract OCR to extract text from uploaded images, evaluates OCR confidence, generates text embeddings, and visualizes illustrative attention scores.

## Features

- Upload PNG, JPG, and JPEG images.
- Extract readable text using Tesseract OCR.
- Display extracted text in the application.
- Calculate average OCR confidence.
- Count recognized words.
- Display word-by-word OCR confidence scores.
- Generate text embeddings using Sentence Transformers.
- Visualize illustrative attention scores.
- Download extracted text as a text file.
- Download a full analysis report.

## Technologies Used

- Python
- Streamlit
- NumPy
- Pandas
- Pillow
- Pytesseract
- Tesseract OCR
- Sentence Transformers

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

### 1. Clone the repository

```bash
git clone https://github.com/humai2606/AI-Image-Text-Analyzer.git
cd AI-Image-Text-Analyzer
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR

Install the Tesseract OCR engine separately.

On Windows, configure the Tesseract executable path in the application if it is not automatically detected.

### 4. Run the application

```bash
streamlit run app.py
```

## How to Use

1. Start the application.
2. Upload a PNG, JPG, or JPEG image containing text.
3. Click **Analyze Image**.
4. View the extracted text and OCR confidence statistics.
5. Explore the word-by-word confidence table and attention visualization.
6. Download the extracted text or full analysis report.

## Limitations

- OCR accuracy depends on image quality, text clarity, and layout.
- Blurry or low-resolution images may produce incorrect results.
- OCR confidence does not guarantee that extracted text is correct.
- Attention scores are illustrative and are not explanations from a trained attention model.
- Text embeddings represent text numerically and do not guarantee semantic understanding in every context.

## Future Improvements

- Add image preprocessing to improve OCR results.
- Support multiple OCR languages.
- Improve text analysis and visualization.
- Deploy the application online using Streamlit Community Cloud.

## Author

Humairul Jashira M.

