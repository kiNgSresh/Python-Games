try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\User\AppData\Local\Tesseract-OCR\tesseract.exe'

print(pytesseract.image_to_string(r'C:\Users\User\Desktop\res.jpg', timeout=10))
