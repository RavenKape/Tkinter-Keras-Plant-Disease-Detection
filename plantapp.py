from cv2 import flann_Index
import numpy as np
from tkinter import *
from tkinter import filedialog
import os 
import cv2
import tkinter as tk
from PIL import Image, ImageTk
from sklearn.preprocessing import LabelBinarizer
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import keras.models
from keras import backend as K
from keras.wrappers.scikit_learn import KerasClassifier

root = Tk()
label_binarizer = LabelBinarizer()
model = keras.models.load_model("diseasedetectmodel9.h5")
default_image_size = tuple((256, 256))

Categories = ["Pepper_bell___Bacterial_spot", 
              "Pepper_bell___healthy",
              "Potato___Early_blight", 
              "Potato___healthy", 
              "Potato___Late_blight", 
              "Tomato___Bacterial_spot",
              "Tomato___Early_blight", 
              "Tomato___healthy", 
              "Tomato___Late_blight",
              "Tomato___Leaf_Mold",
              "Tomato___Septoria_leaf_spot",
              "Tomato___Target_Spot"]

width = 256
height = 256
depth = 3

class MainMenu:
    def __init__(self, master):
        master.title("Interface")

def convert_image_to_array(image_dir):
    try:
        image = cv2.imread(image_dir)
        if image is not None:
            image = cv2.resize(image, default_image_size)
            return img_to_array(image)
        else:
            return np.array([])
    except Exception as e:
        print(f"Error : {e}")
        return None


def showimage():
    global fln
    fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File", filetypes=(("JPG File","*.jpg"),("PNG File","*.png"), ("All Files", "*.*")))
    img = Image.open(fln)
    resize_image = img.resize((256, 256), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resize_image)
    img.image = img
    test_label = tk.Label(image=img)
    canvas1.create_image(180, 525, image = img, anchor = "nw")

    canvas1.delete("result")
    canvas1.delete("result_box")
    im = convert_image_to_array(fln)
    np_image_li = np.array(im, dtype=np.float16) / 225.0
    npp_image = np.expand_dims(np_image_li, axis=0)
    result = model.predict(npp_image)
    finalresult = Categories[np.argmax(result[0])]
    canvas1.create_rectangle(435, 525, 1050, 780, outline = "black", fill = "white", tags = "result_box")
    canvas1.create_text( 720, 650, text = "Result:\n"+ finalresult, font = "Times 36 bold", tags = "result")

root.title("Plant Disease")
root.geometry("1200x900")

bg = Image.open("background.jpg")
bg = ImageTk.PhotoImage(bg)
background_label = tk.Label(image=bg)

canvas1 = Canvas( root, width = 1200, height = 900)
canvas1.pack(fill = "both", expand = True)

canvas1.create_image( 0, 0, image = bg, anchor = "nw")
canvas1.create_text( 610, 200, text = "Plant Disease", font = "Times 60 bold")

btn = Button(root, height="3", width="15", text="Browse Image", command=showimage)
btn2 = Button(root, height="3", width="15", text="Help")
btn3 = Button(root, height="3", width="15", text="Exit", command=lambda: exit())

btn_canvas = canvas1.create_window( 150, 350, anchor = "nw", window = btn)
btn2_canvas = canvas1.create_window( 550, 350, anchor = "nw", window = btn2)
btn3_canvas = canvas1.create_window( 950, 350, anchor = "nw", window = btn3)

root.mainloop()