from docx import Document
import io
import pyautogui
from pynput.keyboard import Listener


doc = Document()  # документ
images = []  # список скриншотов


def add_screenshot(doc):
    img = pyautogui.screenshot()  # screenshot(region=(0, 100, 500, 500))
    imdata = io.BytesIO()
    img.save(imdata, format='png')
    imdata.seek(0)

    doc.add_picture(imdata)
    del imdata


def save_doc(doc):
    doc.save('demo1.docx')


def keypress(Key):
    global doc

    if str(Key) == 'Key.print_screen':
        add_screenshot(doc)
    if str(Key) == 'Key.esc':
        save_doc(doc)
        quit()


with Listener(on_press=keypress) as listener:
    listener.join()
