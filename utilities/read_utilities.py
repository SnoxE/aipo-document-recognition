import cv2
import matplotlib.pyplot as plt 
import numpy as np
from pytesseract import image_to_string
import pytesseract


def dataUrodzeniaDowodOsobisty(img, height, width):
    cropped_image = img[(int)(height*0.48):(int)(height*0.48+height*0.06), (int)(width*0.62):(int)(width*0.83)]
    output = image_to_string(cropped_image, lang='eng+pol', config='--psm 6')
    return output


def imieDowodOsobisty(img, height, width):
    cropped_image = img[(int)(height*0.35):(int)(height*0.35+height*0.1), (int)(width*0.35):(int)(width*0.75)]
    output = image_to_string(cropped_image, lang='eng+pol', config='--psm 6')
    return output


def nazwiskoDowodOsobisty(img, height, width):
    cropped_image = img[(int)(height*0.235):(int)(height*0.235+height*0.1), (int)(width*0.35):(int)(width*0.75)]
    output = image_to_string(cropped_image, lang='eng+pol', config='--psm 6')
    return output


def wypiszDowodOsobisty(img,height,width):
    print(imieDowodOsobisty(img,height,width))
    print(nazwiskoDowodOsobisty(img,height,width))
    print(dataUrodzeniaDowodOsobisty(img,height,width))


def dataUrodzeniaPaszport(img, height, width):
    cropped_image = img[(int)(height*0.345):(int)(height*0.345+height*0.06), (int)(width*0.29):(int)(width*0.56)]
    output = image_to_string(cropped_image, lang='eng+pol', config='--psm 6')
    return output


def imiePaszport(img, height, width):
    cropped_image = img[(int)(height*0.275):(int)(height*0.275+height*0.05), (int)(width*0.3):(int)(width*0.55)]
    output = image_to_string(cropped_image, lang='eng+pol', config='--psm 6')
    return output


def nazwiskoPaszport(img, height, width):
    cropped_image = img[(int)(height*0.2):(int)(height*0.2+height*0.05), (int)(width*0.3):(int)(width*0.55)]
    output = image_to_string(cropped_image, lang='eng+pol', config='--psm 6')
    return output


def wypiszPaszport(img,height,width):
    print(imiePaszport(img,height,width))
    print(nazwiskoPaszport(img,height,width))
    print(dataUrodzeniaPaszport(img,height,width))


def dataUrodzeniaLegitymacja(img, height, width):
    cropped_image = img[(int)(height*0.755):(int)(height*0.755+height*0.07), (int)(width*0.185):(int)(width*0.35)]
    output = image_to_string(cropped_image, lang='eng+pol', config='--psm 6')
    return output


def imieLegitymacja(img, height, width):
    cropped_image = img[(int)(height*0.4):(int)(height*0.4+height*0.05), (int)(width*0.35):(int)(width*0.65)]
    output = image_to_string(cropped_image, lang='eng+pol', config='--psm 6')
    return output


def nazwiskoLegitymacja(img, height, width):
    cropped_image = img[(int)(height*0.46):(int)(height*0.46+height*0.05), (int)(width*0.35):(int)(width*0.65)]
    output = image_to_string(cropped_image, lang='eng+pol', config='--psm 6')
    return output


def wypiszLegitymacje(img,height,width):
    print(imieLegitymacja(img,height,width))
    print(nazwiskoLegitymacja(img,height,width))
    print(dataUrodzeniaLegitymacja(img,height,width))


def porownajDowod(image):
    template = cv2.imread('DO.jpg')
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    similarity_percentage = max_val * 100
    print("Podobieństwo procentowe:", similarity_percentage)
    return similarity_percentage


def porownajPaszport(image):
    template = cv2.imread('PS.jpg')
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    similarity_percentage = max_val * 100
    print("Podobieństwo procentowe:", similarity_percentage)
    return similarity_percentage


def porownajLegitymacje(image):
    template = cv2.imread('LE.jpg')
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    similarity_percentage = max_val * 100
    print("Podobieństwo procentowe:", similarity_percentage)
    return similarity_percentage


def wypiszDane(image,height,width):
    dow = porownajDowod(image)
    pas = porownajPaszport(image)
    leg = porownajLegitymacje(image)
    if(dow > 80 or pas > 80 or leg > 80):
        if(dow > pas and dow > leg):
            wypiszDowodOsobisty(image,height,width)
        elif((pas > dow and pas > leg)):
            wypiszPaszport(image,height,width)
        else:
            wypiszLegitymacje(image,height,width)     