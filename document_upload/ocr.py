import os

import pytesseract

from PIL import Image

from pdf2image import convert_from_path


def extract_text_from_image(file_path: str):

    image = Image.open(file_path)

    text = pytesseract.image_to_string(image)

    return text


def extract_text_from_pdf(file_path: str):

    pages = convert_from_path(file_path)

    extracted_text = []

    for page in pages:

        text = pytesseract.image_to_string(page)

        extracted_text.append(text)

    return "\n".join(extracted_text)


def extract_text(file_path: str):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":

        return extract_text_from_pdf(file_path)

    return extract_text_from_image(file_path)
