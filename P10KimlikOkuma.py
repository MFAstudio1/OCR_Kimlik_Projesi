import pytesseract
import cv2
from PIL import Image
import numpy as np
import imutils
import sqlite3

import tkinter as tk




def IdSurnameConvert() -> list:
    
    pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\user\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

    yol = "C:\\Users\\user\\Documents\\Py_MFAstudio\\PyCmtKurs\\resim\\kimlik.png"
    
    resim = cv2.imread(yol)

    #cv2.imshow("base", resim)

    #########Printin ID number ###############
    # create a mask

    mask = np.zeros(resim.shape[:2], np.uint8)
    mask[160:210, 60:360] = 255

    # compute the bitwise AND using the mask
    masked_img = cv2.bitwise_and(resim,resim,mask = mask)
    masked_img_metin_tc = pytesseract.image_to_string(masked_img)
    print("TC numarası:"+masked_img_metin_tc)

    # display the mask, and the output image
    """cv2.imshow('Masked Image',masked_img)
    cv2.waitKey(0)"""

    #############Printing Surname #################

    # create a mask
    mask = np.zeros(resim.shape[:2], np.uint8)
    mask[270:325, 360:605] = 255

    # compute the bitwise AND using the mask
    masked_img = cv2.bitwise_and(resim,resim,mask = mask)
    masked_img_metin_soyisim = pytesseract.image_to_string(masked_img, lang="tur")
    print("soyisim: "+masked_img_metin_soyisim)

    # display the mask, and the output image
    """cv2.imshow('Masked Image',masked_img)
    cv2.waitKey(0)"""


    #############Printing Seri no #################

    # create a mask
    mask = np.zeros(resim.shape[:2], np.uint8)
    mask[480:550, 340:600] = 255

    # compute the bitwise AND using the mask
    masked_img = cv2.bitwise_and(resim,resim,mask = mask)
    masked_img_metin_serino = pytesseract.image_to_string(masked_img, lang="tur")
    print("Seri no: "+masked_img_metin_serino)

    # display the mask, and the output image
    """cv2.imshow('Masked Image',masked_img)
    cv2.waitKey(0)"""

    #############Printing name #################
    """
    # create a mask
    mask = np.zeros(resim.shape[:2], np.uint8)
    mask[190:240, 80:380] = 255

    # compute the bitwise AND using the mask
    masked_img = cv2.bitwise_and(resim,resim,mask = mask)
    masked_img_metin = pytesseract.image_to_string(masked_img)
    print("TC numarası:"+masked_img_metin)


    # display the mask, and the output image
    cv2.imshow('Masked Image',masked_img)
    cv2.waitKey(0)
    """
    return masked_img_metin_tc, masked_img_metin_soyisim

########SQL bağlantısı###############

def tc_isim_kontrol(masked_img_metin_tc : str, masked_img_metin_soyisim : str) -> bool:
    # Veritabanı bağlantısı oluşturma
    conn = sqlite3.connect('veritabani.db')
    cursor = conn.cursor()

    # TC ve isim değerlerini veritabanında kontrol etme
    
    cursor.execute("SELECT * FROM kisiler WHERE tc =? AND isim =?", (int(masked_img_metin_tc.strip()), masked_img_metin_soyisim.strip()))
    kayit = cursor.fetchone()
    print(kayit)
    
    
    # Veritabanında kayıt varsa True, yoksa False döndürme
    if kayit:
        return True
    else:
        return False
    
    # Bağlantıyı kapat
    conn.close()

tc, soyisim= IdSurnameConvert()
print(tc_isim_kontrol(tc, soyisim))