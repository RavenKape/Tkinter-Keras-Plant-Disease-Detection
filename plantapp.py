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

resultlabel = tk.Label(root)
resultlabel.pack(side=BOTTOM)
def showimage():  
    fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File", filetypes=(("JPG File","*.jpg"),("PNG File","*.png"), ("All Files", "*.*")))
    img = Image.open(fln)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img
    im = convert_image_to_array(fln)
    np_image_li = np.array(im, dtype=np.float16) / 225.0
    npp_image = np.expand_dims(np_image_li, axis=0)
    result = model.predict(npp_image)
    finalresult = Categories[np.argmax(result[0])]
    resultlabel['text'] = "Result: "+ finalresult
    return finalresult



frm = Frame(root)
frm.pack(side=BOTTOM, padx=15, pady=15)

lbl = Label(root)
lbl.pack()

btn = Button(frm, text="Browse Image", command=showimage)
btn.pack(side=tk.LEFT)

btn2 = Button(frm, text="Exit", command=lambda: exit())
btn2.pack(side=tk.LEFT,padx=10)

root.title("Image Browser")
root.geometry("300x350")
root.mainloop()
