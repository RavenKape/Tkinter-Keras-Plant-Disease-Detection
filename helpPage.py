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

root = Tk()
wt = root.winfo_screenwidth()
ht = root.winfo_screenheight()
font_size = int(((wt/2.41)-(ht/2))/7)

root.title("Help Page")
root.geometry(str(wt)+"x"+str(ht))
root.resizable(True, True)

canvas1 = Canvas( root, width = wt, height = ht)
canvas1.pack(fill = "both", expand = True)

bg = Image.open("background2.jpg")
resize_bg = bg.resize((wt, ht), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(resize_bg)
background_label = tk.Label(image=bg)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")

canvas1.create_text( wt/2, ht/7.5, text = "How to use the App", font = "Times 60 bold")

canvas1.create_text( wt/6, ht/4, text = "1) Click Browse Image button", font = "Times " + str(font_size) + " bold")
pic1 = Image.open("help_pic1.jpg")
new_width = wt/3
new_height = ht/3
pic1 = pic1.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
pic1 = ImageTk.PhotoImage(pic1)
canvas1.create_image( (wt/10)-(wt/10), ht/3, image = pic1, anchor = "nw")

canvas1.create_text( wt/2, ht/3.8, text = "2) Choose the image of the \n plant you want to predict", font = "Times " + str(font_size) + " bold")
pic2 = Image.open("help_pic2.jpg")
new_width = wt/3
new_height = ht/3
pic2 = pic2.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
pic2 = ImageTk.PhotoImage(pic2)
canvas1.create_image( wt/3, ht/3, image = pic2, anchor = "nw", )

canvas1.create_text( (wt/3)+(wt/2.1), ht/4, text = "3) Check the result", font = "Times " + str(font_size) + " bold")
pic3 = Image.open("help_pic3.jpg")
new_width = wt/3
new_height = ht/3
pic3 = pic3.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
pic3 = ImageTk.PhotoImage(pic3)
canvas1.create_image( (wt/3)+(wt/3), ht/3, image = pic3, anchor = "nw")

btn = Button(root, height="3", width="15", text="List of Plants")
btn2 = Button(root, height="3", width="15", text="Back", command=mainPage)

btn_canvas = canvas1.create_window( wt/2.6, ht/1.25, anchor = "nw", window = btn)
btn2_canvas = canvas1.create_window( wt/1.9, ht/1.25, anchor = "nw", window = btn2)

root.mainloop()