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

def mainPage():
    root.destroy()
    import main

def helpPage():
    root.destroy()
    import helpPage

root = Tk()
wt = root.winfo_screenwidth()
ht = root.winfo_screenheight()
font_size = int(((wt/2.41)-(ht/2))/7)

root.title("Plant List")
root.geometry(str(wt)+"x"+str(ht))
root.resizable(True, True)

canvas1 = Canvas( root, width = wt, height = ht)
canvas1.pack(fill = "both", expand = True)

bg = Image.open("background2.jpg")
resize_bg = bg.resize((wt, ht), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(resize_bg)
background_label = tk.Label(image=bg)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")

canvas1.create_text( wt/2, ht/7.5, text = "List of Plants", font = "Times 60 bold")

canvas1.create_text( wt/3, (ht/6)+(ht/6), text = " - Pepper bell Bacterial spot \n - Pepper bell healthy \n - Potato Early blight  \n - Potato healthy  \n - Potato Late blight  \n - Tomato Bacterial spot", font = "Times " + str(font_size) + " bold")
canvas1.create_text( wt/1.5, (ht/6)+(ht/6), text = " - Tomato Early blight  \n - Tomato healthy  \n - Tomato Late blight  \n - Tomato Leaf Mold  \n - Tomato Septoria leaf spot  \n - Tomato Target Spot", font = "Times " + str(font_size) + " bold")

btn = Button(root, height="3", width="15", text="Back", command=helpPage)
btn2 = Button(root, height="3", width="15", text="Main Page", command=mainPage)

btn_canvas = canvas1.create_window( wt/2.6, ht/1.25, anchor = "nw", window = btn)
btn2_canvas = canvas1.create_window( wt/1.9, ht/1.25, anchor = "nw", window = btn2)

root.mainloop()