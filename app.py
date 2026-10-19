
import os
os.environ["STREAMLIT_SERVER_FILE_WATCHER_TYPE"] = "none"

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import pytesseract

from ocr import extract_text
from embedding import create_embeddings
from attention import calculate_attention


# Page settings
st.set_page_config(
    page_title="AI Image Text Analyzer",
    layout="wide"
)

st.title("AI Image Text Analyzer")
st.write(
    "Extract and analyze text from images using OCR, embeddings, and attention."
)


# Image upload
uploaded = st.file_uploader(
    "Upload Image",
    type=["png", "jpg", "jpeg"]
)


if uploaded is None:
    st.info("Please upload an image to get started.")

else:
    try:
        image = Image.open(uploaded).convert("RGB")
        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        if st.button("Analyze Image"):
            with st.spinner("Analyzing image..."):

                # OCR extraction
                result = extract_text(image)
                text = result["text"].strip()
                words = result["words"]

                # Word confidence extraction
                data = pytesseract.image_to_data(
                    image,
                    output_type=pytesseract.Output.DICT
                )

                details = []

                for w, c in zip(data["text"], data["conf"]):
                    w = w.strip()

                    try:
                        score = float(c)
                    except (ValueError, TypeError):
                        continue

                    if w and score >= 0:
                        details.append((w, score))

            # Show results only after OCR is complete
            if not text:
                st.warning(
                    "No text detected. Try a clearer image."
                )

            else:
                st.success("Text extraction completed!")

                st.subheader("Extracted Text")
                st.text_area(
                    "Recognized Text",
                    value=text,
                    height=150
                )

                st.download_button(
                    label="Download Text",
                    data=text,
                    file_name="extracted_text.txt",
                    mime="text/plain"
                )

                # Confidence calculations
                confidence = [
                    score for word, score in details
                ]

                avg = (
                    sum(confidence) / len(confidence)
                    if confidence else 0.0
                )

                high_confidence = sum(
                    score >= 70 for score in confidence
                )

                # Metrics
                st.subheader("Text Statistics")

                c1, c2, c3 = st.columns(3)

                c1.metric("Total Words", len(words))
                c2.metric(
                    "Average OCR Confidence",
                    f"{avg:.2f}%"
                )
                c3.metric(
                    "High-Confidence Words",
                    high_confidence
                )

                # Word-by-word confidence
                st.subheader("Word-by-Word OCR Confidence")

                confidence_df = pd.DataFrame(
                    details,
                    columns=["Word", "Confidence (%)"]
                )

                st.dataframe(
                    confidence_df,
                    use_container_width=True,
                    hide_index=True
                )

                # Attention analysis
                scores = np.array([], dtype=float)

                if words:
                    embeddings = np.asarray(
                        create_embeddings(words)
                    )

                    if embeddings.ndim == 1:
                        embeddings = embeddings.reshape(1, -1)

                    scores = np.asarray(
                        calculate_attention(embeddings)
                    ).flatten()

                    st.subheader("Attention Visualization")

                    st.caption(
                        f"Embedding dimensions: {embeddings.shape[1]}"
                    )

                    attention_df = pd.DataFrame({
                        "Word": words[:len(scores)],
                        "Attention Score (%)": np.round(
                            scores[:len(words)] * 100, 2
                        )
                    })

                    st.dataframe(
                        attention_df,
                        use_container_width=True,
                        hide_index=True
                    )

                    for word, score in zip(words, scores):
                        st.write(
                            f"**{word}** — {score * 100:.2f}%"
                        )

                        st.progress(
                            float(np.clip(score, 0, 1))
                        )

                    st.caption(
                        "Attention scores are illustrative, "
                        "not OCR confidence or trained-model explanations."
                    )

                # Build full report
                confidence_lines = "\n".join(
                    f"{word}: {score:.2f}%"
                    for word, score in details
                )

                attention_lines = "\n".join(
                    f"{word}: {score * 100:.2f}%"
                    for word, score in zip(words, scores)
                )

                report = f"""
AI IMAGE TEXT ANALYZER - FULL REPORT

EXTRACTED TEXT:
{text}

TOTAL WORDS: {len(words)}
AVERAGE OCR CONFIDENCE: {avg:.2f}%
HIGH-CONFIDENCE WORDS: {high_confidence}

WORD-BY-WORD OCR CONFIDENCE:
{confidence_lines}

ATTENTION SCORES:
{attention_lines}

NOTE:
Attention scores are illustrative and are not trained-model explanations.
"""

                st.download_button(
                    label="Download Full Analysis",
                    data=report,
                    file_name="AI_Analysis_Report.txt",
                    mime="text/plain"
                )

    except Exception as e:
        st.error(f"An error occurred: {e}")
