# @author ashihara

# PyMuPDFをインポート（歴史的な経緯でなぜかfitzのインポートになっていることに注意）
import fitz
import os
# import fitz as pymu とかしておくと読み込み時にPyMuPDF感が出るかもしれない

class PyMuPDF():
    def __init__(self, filename):
        self.filename = filename

    def save_images(self, pdfNo, images, save_dir):
        pdf_file = fitz.open(self.filename)
        #保存ディレクトリが指定されていない時は作る
        if os.path.isdir(save_dir) == False:
            os.mkdir(save_dir)
        for pageNo, image in enumerate(images):
            if image != []:
                for i in range(len(image)):
                    xref = image[i][0]
                    #smask = image[i][1]
                    if image[i][8] == 'FlateDecode':
                        ext = 'png'
                    elif image[i][8] == 'DCTDecode':
                        ext = 'jpeg'

                    pix = fitz.Pixmap(pdf_file.extract_image(xref)["image"])
                    if not pix.colorspace.name in (fitz.csGRAY.name, fitz.csRGB.name):
                        pix = fitz.Pixmap(fitz.csRGB, pix)
                        pix.invert_irect(pix)

                    img_name = os.path.join(save_dir, f'image{pdfNo+1}_{pageNo+1}_{i}.{ext}')
                    pix.save(img_name)

    # return : list of images
    def crop_imgs_from_pdf(self):
        pdf_file = fitz.open(self.filename)
        image_list = []
        # pdf から画像を抜き取りリストにして返す
        for page in range(len(pdf_file)):
            image_list.append(pdf_file[page].get_images())
        return image_list