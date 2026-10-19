
import pytesseract
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def extract_text(image):
    text = pytesseract.image_to_string(image)

    data = pytesseract.image_to_data(
        image,
        output_type=pytesseract.Output.DICT
    )

    words = []
    confidences = []

    for word, confidence in zip(data["text"], data["conf"]):
        word = word.strip()

        if word and float(confidence) >= 0:
            words.append(word)
            confidences.append(float(confidence))

    average_confidence = (
        sum(confidences) / len(confidences)
        if confidences else 0
    )

    return {
        "text": text,
        "words": words,
        "word_count": len(words),
        "average_confidence": average_confidence
    }
