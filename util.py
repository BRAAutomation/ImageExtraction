# @author ashihara

# PyMuPDFをインポート（歴史的な経緯でなぜかfitzのインポートになっていることに注意）
import fitz
# import fitz as pymu とかしておくと読み込み時にPyMuPDF感が出るかもしれない

class PyMuPDF():
    def __init__(self, filename):
        self.filename = filename

    def save_images(self, images, save_dir):
        pdf_file = fitz.open(self.filename)
        counter = 0
        #images内のデータをcounterに合わせて保存
        if not len(images) == 0:
            for image in images:
                counter += 1
                xref = image[0]
                img = pdf_file.extract_image(xref)
                with open(save_dir + "/extracted_image{}.png".format(counter), "wb") as f:
                    f.write(img["image"])

    # return : list of images
    def crop_imgs_from_pdf(self):
        pdf_file = fitz.open(self.filename)
        image_list = []
        # pdf から画像を抜き取る
        for page in pdf_file:
           images = page.get_images()
           for image in images:
                image_list.append(image)
        return image_list