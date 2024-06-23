import cv2
from pytesseract import image_to_string
import os

def dataUrodzeniaDowodOsobisty(img, height, width):
    cropped_image = img[(int)(height*0.48):(int)(height*0.48+height*0.06), (int)(width*0.62):(int)(width*0.83)]
    output = image_to_string(cropped_image, lang='eng+pol', config='--psm 6')
    return output.strip()


def imieDowodOsobisty(img, height, width):
    cropped_image = img[(int)(height*0.35):(int)(height*0.35+height*0.1), (int)(width*0.35):(int)(width*0.75)]
    output = image_to_string(cropped_image, lang='eng+pol', config='--psm 6')
    return output.strip()


def nazwiskoDowodOsobisty(img, height, width):
    cropped_image = img[(int)(height*0.235):(int)(height*0.235+height*0.1), (int)(width*0.35):(int)(width*0.75)]
    output = image_to_string(cropped_image, lang='eng+pol', config='--psm 6')
    return output.strip()


def wypiszDowodOsobisty(img,height,width):
    print(imieDowodOsobisty(img,height,width))
    print(nazwiskoDowodOsobisty(img,height,width))
    print(dataUrodzeniaDowodOsobisty(img,height,width))

def wygenerujDaneDowodOsobisty(img,height,width):
    return (imieDowodOsobisty(img,height,width),  
           nazwiskoDowodOsobisty(img,height,width),  
           dataUrodzeniaDowodOsobisty(img,height,width),   
           "Dowód Osobisty")


def dataUrodzeniaPaszport(img, height, width):
    cropped_image = img[(int)(height*0.345):(int)(height*0.345+height*0.06), (int)(width*0.29):(int)(width*0.56)]
    output = image_to_string(cropped_image, lang='eng+pol', config='--psm 6')
    return output.strip()


def imiePaszport(img, height, width):
    cropped_image = img[(int)(height*0.275):(int)(height*0.275+height*0.05), (int)(width*0.3):(int)(width*0.55)]
    output = image_to_string(cropped_image, lang='eng+pol', config='--psm 6')
    return output.strip()


def nazwiskoPaszport(img, height, width):
    cropped_image = img[(int)(height*0.2):(int)(height*0.2+height*0.05), (int)(width*0.3):(int)(width*0.55)]
    output = image_to_string(cropped_image, lang='eng+pol', config='--psm 6')
    return output.strip()


def wypiszPaszport(img,height,width):
    print(imiePaszport(img,height,width))
    print(nazwiskoPaszport(img,height,width))
    print(dataUrodzeniaPaszport(img,height,width))

def wygenerujDanePaszport(img,height,width):
    return (imiePaszport(img,height,width), 
            nazwiskoPaszport(img,height,width), 
            dataUrodzeniaPaszport(img,height,width), 
            "Paszport")


def dataUrodzeniaLegitymacja(img, height, width):
    cropped_image = img[(int)(height*0.755):(int)(height*0.755+height*0.07), (int)(width*0.185):(int)(width*0.35)]
    output = image_to_string(cropped_image, lang='eng+pol', config='--psm 6')
    return output.strip()


def imieLegitymacja(img, height, width):
    cropped_image = img[(int)(height*0.4):(int)(height*0.4+height*0.05), (int)(width*0.35):(int)(width*0.65)]
    output = image_to_string(cropped_image, lang='eng+pol', config='--psm 6')
    return output.strip()


def nazwiskoLegitymacja(img, height, width):
    cropped_image = img[(int)(height*0.46):(int)(height*0.46+height*0.05), (int)(width*0.35):(int)(width*0.65)]
    output = image_to_string(cropped_image, lang='eng+pol', config='--psm 6')
    return output.strip()


def wypiszLegitymacje(img,height,width):
    print(imieLegitymacja(img,height,width))
    print(nazwiskoLegitymacja(img,height,width))
    print(dataUrodzeniaLegitymacja(img,height,width))

def wygenerujDaneLegitymacja(img,height,width):
    return (imieLegitymacja(img,height,width), 
            nazwiskoLegitymacja(img,height,width), 
            dataUrodzeniaLegitymacja(img,height,width),
            "Legitymacja")

def porownajDowod(image):
    template_path = os.path.join(os.path.dirname(__file__), 'DO.jpg')
    template = cv2.imread(template_path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    similarity_percentage = max_val * 100
    print("Podobieństwo procentowe:", similarity_percentage)
    return similarity_percentage


def porownajPaszport(image):
    template_path = os.path.join(os.path.dirname(__file__), 'PS.jpg')
    template = cv2.imread(template_path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    similarity_percentage = max_val * 100
    print("Podobieństwo procentowe:", similarity_percentage)
    return similarity_percentage


def porownajLegitymacje(image):
    template_path = os.path.join(os.path.dirname(__file__), 'LE.jpg')
    template = cv2.imread(template_path)
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


def generateData(image,height,width):
    dow = porownajDowod(image)
    pas = porownajPaszport(image)
    leg = porownajLegitymacje(image)
    if(dow > 80 or pas > 80 or leg > 80):
        if(dow > pas and dow > leg):
            return wygenerujDaneDowodOsobisty(image,height,width)
        elif((pas > dow and pas > leg)):
            return wygenerujDanePaszport(image,height,width)
        else:
            return wygenerujDaneLegitymacja(image,height,width)
            