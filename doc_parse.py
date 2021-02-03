import PyPDF2
from PyPDF2.utils import PdfReadError
from pathlib import Path
from typing import List, Tuple
import pytesseract
from PIL import Image
import re


def pdf_image_extract(pdf_path: Path) -> List[Path]:
    file_decode = {
        '/DCTDecode': 'jpg',
        '/FlateDecode': 'png',
        '/JPXDecode': 'jp2'
    }
    result = []
    with open(pdf_path, 'rb') as file:
        try:
            pdf_file = PyPDF2.PdfFileReader(file)
        except PdfReadError:
            # log error
            pass
        print(1)
        for page_num, page in enumerate(pdf_file.pages, 1):
            file_name = f"{pdf_path.name}.{page_num}.{file_decode[page['/Resources']['/XObject']['/Im0']['/Filter']]}"
            image_data = page['/Resources']['/XObject']['/Im0']._data
            img_path = pdf_path.parent.joinpath(file_name)
            # записываем файл
            img_path.write_bytes(image_data)  # полезная фича pathlib. также можно и читать
            result.append(img_path)
    return result


def get_serial_number(img_path: Path) -> Tuple[Path, List[str]]:
    numbers = []
    text_ru = pytesseract.image_to_string(Image.open(img_path), 'eng+rus')
    numbers = re.findall(r'[\n\r][ \t]*заводской.*номер[ \t]*([^\n\r]*)', text_ru)
    return img_path, numbers


if __name__ == '__main__':
    pdf_file_path = Path('/Users/virux/PycharmProjects/data-mining/8416_4.pdf')

    images = pdf_image_extract(pdf_file_path)
    numbers = list(map(get_serial_number, images))
    print(1)
