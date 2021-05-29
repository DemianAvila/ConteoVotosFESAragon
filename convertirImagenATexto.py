try:
    from PIL import Image
except ImportError:
    import Image
from re import I
import pytesseract

def textoCrudo(archivo):
    img = Image.open(archivo)
    img = img.convert('L')
    return(pytesseract.image_to_string(img, lang="spa"))