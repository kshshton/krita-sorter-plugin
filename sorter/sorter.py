from krita import *
from datetime import date
import os

today = date.today()
today_format = today.strftime("%d-%m-%Y")

date_dir = f"{today_format}"
parent_dir = "C:/Users/%userprofile%/Desktop/Tree/"
path = os.path.join(parent_dir, date_dir)
file_exist = os.path.exists(path)


def save():
    currentDocument = Krita.instance().activeDocument()
    file_name = Krita.instance().activeDocument().name()
    currentDocument.saveAs(f"{path}/{file_name}")


def execute():
    if file_exist:
        save()
    else:
        os.mkdir(path)
        save()
