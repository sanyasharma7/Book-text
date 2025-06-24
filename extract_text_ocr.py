import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = "/home/runner/.nix-profile/bin/tesseract"

def extract_text_ocr(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""

    for page in doc:
        pix = page.get_pixmap(dpi=300)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        text = pytesseract.image_to_string(img, lang='eng')
        full_text += text + "\n"

    with open("raw_text.txt", "w", encoding="utf-8") as f:
        f.write(full_text)

if __name__ == "__main__":
    extract_text_ocr("book.pdf")
