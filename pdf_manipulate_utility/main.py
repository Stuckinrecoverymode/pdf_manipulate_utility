import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * #QFileDialog, QApplication, QInputDialog, QLineEdit, QMainWindow
from PyQt5.QtGui import QIcon, QFont
import fitz
from mainWindow import Ui_MainWindow

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)

class Pdfapp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Pdfapp, self).__init__()
        self.setupUi(self)
        #uic.loadUi('./src/mainWindow_ui.ui', self)
        self.setWindowTitle("Pdf Manipulate Utility")
        self.setWindowOpacity(0.99)
        self.setWindowIcon(QIcon(resource_path('./src/pdf.ico')))
        self.actionimage_to_pdf.triggered.connect(lambda: self.image_to_pdf())
        self.actionConvert.triggered.connect(lambda: self.convert_to_pdf())
        self.encrypt.clicked.connect(lambda: self.encrypt_pdf())
        self.del_metadata.triggered.connect(lambda: self.metadata_del())
        self.about.triggered.connect(lambda: self.about_pdfapp())
        self.merge.clicked.connect(lambda: self.merge_pdf())
        #self.merge.clicked.connect(lambda: self.open_file())
        #self.pushButton.clicked.connect(lambda: self.save_file())
        #self.close.clicked.connect(lambda: self.closeEvent())
        self.show()

    def gettext(self):
        global in_password
        in_password, _ = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your password:')
        return in_password

    def open_images(self):
        global file_path_im
        file_path_im = []
        options = QFileDialog.Options()
        file_path_im, _ = QFileDialog.getOpenFileNames(self, "Open File", "", "image files (*.jpg *.png *.jpeg *.tiff *.bmp)",
                                                  options=options)
       # print(type(file_path))
       # print(type(file_path[0]))
        # filedialog return file names as list.
        return file_path_im

    def open_file(self):
        global file_path
        file_path = []
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileNames(self, "Open File", "", "document file (*.pdf *.docx *.epub)",
                                                  options=options)
       # print(type(file_path))
       # print(type(file_path[0]))
        # filedialog return file names as list.
        return file_path

    def encrypt_pdf(self):
        self.open_file()
        perm = int(
        fitz.PDF_PERM_ACCESSIBILITY
        | fitz.PDF_PERM_PRINT
        | fitz.PDF_PERM_COPY
        | fitz.PDF_PERM_ANNOTATE
        )
        self.gettext()
        owner_pass = in_password  # owner password
        user_pass = owner_pass  # user password
        encrypt_meth = fitz.PDF_ENCRYPT_AES_256
        doc = fitz.open(file_path[0])
        self.save_file()
        doc.save(
            save_path,
            encryption=encrypt_meth,  # set the encryption method
            owner_pw=owner_pass,  # set the owner password
            user_pw=user_pass,  # set the user password
            permissions=perm,  # set permissions
        )
        #docx = fitz.open("pdf", tobytes)
        dialogMessage = QMessageBox()
        dialogMessage.setText('PDF is now encrpyted with your password.')
        dialogMessage.exec_()
        doc.close()

    def image_to_pdf(self):
        self.open_images()
        doc = fitz.open()
        for img in file_path_im:
            imgdoc=fitz.open(img)           # open image as a document
            pdfbytes=imgdoc.convert_to_pdf()  # make a 1-page PDF of it
            imgpdf=fitz.open("pdf", pdfbytes)
            doc.insert_pdf(imgpdf)             # insert the image PDF
        self.save_file()
        doc.save(save_path)
        dialogMessage = QMessageBox()
        dialogMessage.setText('pdf created from images that in list.')
        dialogMessage.exec_()
        doc.close()

        #self.doc = fitz.open(filename[0])
    def metadata_del(self):
        self.open_file()
        docm = fitz.open(file_path[0])
        meta_data = docm.metadata
        #print(meta_data)
        docm.set_metadata({}) # deleting metadata and save it with a new file.
        self.save_file()
        pdffile = save_path
        #print(save_path)
        docm.save(pdffile, garbage=4)
        dialogMessage = QMessageBox()
        dialogMessage.setText('PDF metadata deleting completed!')
        dialogMessage.exec_()
        docm.close()

    def save_file(self):
        global save_path
        options = QFileDialog.Options()
        save_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Pdf Files (*.pdf) ", options=options)
        return save_path

    def merge_pdf(self):
        self.open_file()
        docv = fitz.open()
        for pdf in file_path:
            with fitz.open(pdf) as mfile:
                docv.insert_pdf(mfile)
        self.save_file()
        docv.save(save_path)
        dialogMessage = QMessageBox()
        dialogMessage.setText('PDF merge completed')
        dialogMessage.exec_()
        docv.close()


    def convert_to_pdf(self):
        self.open_file()
        xdh = file_path[0]
        xps = fitz.open(xdh)
        pdfbyte = xps.convert_to_pdf()
        sdfs = fitz.open()
        pdf_output = fitz.open(sdfs, pdfbyte)
        self.save_file()
        #output_pdf = save_path
        pdf_output.save(save_path)
        dialogMessage = QMessageBox()
        dialogMessage.setText('pdf converting completed!')
        dialogMessage.exec_()
        xdh.close()

    #def closeEvent(self, event):
        #event.accept()

    def about_pdfapp(self):
        dialogMessage = QMessageBox()
        dialogMessage.setText('Pdf manipulate program\nV1.0')
        dialogMessage.setWindowTitle('Pdf App')
        dialogMessage.exec_()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Pdfapp()
    app.exec_()
