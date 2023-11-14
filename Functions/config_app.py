import PIL.Image
import torch
import os

ROOT_PATH = os.getcwd() + "/"
INITIAL_DIR = ROOT_PATH + "Data/Labels_Factory"
IMAGE_PIL = PIL.Image
TITLE_WINDOW = "Visual Baggage Barcode Checker"
ICON_WINDOW = ROOT_PATH + "Icons/ECUST.ico"
PNG_WINDOW = ROOT_PATH + "Icons/ECUST.png"

WINDOW_WIDTH = 650
WINDOW_HEIGHT = 450
WIDTH_HEIGHT_DISPLAY = [416, 416]
WH_SUB_DISPLAY = (300, 150)

COLOR_BLACK = "#000000"
COLOR_BROWN = "#726461"
COLOR_RED = "#ff3333"
COLOR_BLUE = "#53D4F7"
COLOR_GREEN = "#00b359"
COLOR_WHITE = "#ffffff"
COLOR_PURPLE = "#a64dff"
COLOR_YELLOW = "#ffff00"
COLOR_ICE_BLUE = "#99FFFF"
COLOR_RUSSIAN_VIOLET = "#32174D"
COLOR_CHINESE_WHITE = "#e2e5de"
COLOR_LOTION = "#fefdfa"
COLOR_DARK_YELLOW = "#F5F5DC"

COLOR_BACKGROUND = COLOR_LOTION

LABELS = {
    0: "Barcode",
    1: "QR_code"
}
RETURN_RESULT = {
    "origin": "...",
    "OK": "OK",
    "NG": "NG"
}


DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
YOLOv8_IMAGE_INPUT_SIZE = [416, 416]
PATH_MODEL_YOLO_V8 = ROOT_PATH + "Models/YOLO/best.pt"

VIDEO_SOURCE = 0
DELAY_UPDATE_FRAME = 1

PATH_SAVE_INPUT_FILES = ROOT_PATH + "Reports/Save_Inputs" + "/"
PATH_SAVE_OUTPUT_FILES = ROOT_PATH + "Reports/Save_Outputs" + "/"
