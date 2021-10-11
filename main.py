'''
Image OCR (Optical Character Recognition) to text.
'''

import os
from PIL import Image
from tkinter import filedialog
import pytesseract


def main() -> None:
  img_paths = get_image_paths()

  for img_path in img_paths:
    img = Image.open(img_path)

    print(f'Scan image "{img_path}"...')
    img_str = image_to_string(img, 'swe')

    out_filename = get_out_filename(img_path, '.txt')

    with open(f'out/{out_filename}', 'w') as file:
      file.write(img_str)


def get_image_paths() -> tuple[str]:
  return filedialog.askopenfilenames(
    title='Scan images',
    filetypes=[
      ('JPEG image', '*.jpg'),
      ('PNG image', '*.png'),
    ]
  )


def image_to_string(img, lang) -> str:
  return pytesseract.image_to_string(img,
    lang=lang,
    timeout=30
  )


def get_out_filename(file_path, file_ext) -> str:
  return os.path.splitext(os.path.basename(file_path))[0] + file_ext


if __name__ == '__main__':
  main()
