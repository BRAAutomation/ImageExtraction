import os
import argparse
from util import *

parser = argparse.ArgumentParser()
parser.add_argument('--pdf_file', type=str, default='PDF/sample.pdf')
parser.add_argument('--save_dir', type=str, default='Images')
args = parser.parse_args()

def main(args):
    print('a')
    pymupdf = PyMuPDF(args.pdf_file)
    images = pymupdf.crop_imgs_from_pdf()
    pymupdf.save_images(images, args.save_dir)

if __name__ == '__main__':
    main(args)
