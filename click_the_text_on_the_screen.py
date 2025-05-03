import pyautogui
import pytesseract
from PIL import ImageGrab

# Optional: Uncomment if Tesseract is not in your PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def find_text_on_screen(text_to_find):
    screenshot = ImageGrab.grab()
    text_data = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)
    for i in range(len(text_data['text'])):
        if text_to_find.lower() in text_data['text'][i].lower():
            x, y, w, h = text_data['left'][i], text_data['top'][i], text_data['width'][i], text_data['height'][i]
            return x + w // 2, y + h // 2
    return None

# === Example usage ===
text = "screenshot"
pos = find_text_on_screen(text)
if pos:
    pyautogui.click(pos)
    print(f"Clicked on '{text}' at {pos}")
else:
    print(f"'{text}' not found on screen.")
