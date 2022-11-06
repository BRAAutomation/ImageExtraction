import os
import argparse
from util import *
import glob

parser = argparse.ArgumentParser()
parser.add_argument('--pdf_file', type=str, default='PDF/*')
parser.add_argument('--save_dir', type=str, default='Images')
args = parser.parse_args()

def main(args):
    #take from all pdf files
    for pdf_fl in glob.glob(args.pdf_file):
        pymupdf = PyMuPDF(pdf_fl)
        images = pymupdf.crop_imgs_from_pdf()
        pymupdf.save_images(images, args.save_dir)

if __name__ == '__main__':
    main(args)
