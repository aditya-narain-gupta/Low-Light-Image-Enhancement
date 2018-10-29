import tkinter as tk
from tkinter import filedialog
from PIL import Image as image
from PIL import ImageTk
from tkinter import *
import rawpy
import imageio

path1 = "Images/image1.jpg"
path2 = "Images/image2.jpg"

def convert_raw_to_jpg(path_name):
	raw = rawpy.imread(path_name)
	rgb = raw.postprocess()
	imageio.imsave('Images/input.jpg',rgb)
	
def upload_image(e):
	path2 = tk.filedialog.askopenfile(parent=frame3,mode='rb',title='Choose a file')
	convert_raw_to_jpg(path2)
	img2 = image.open('Images/input.jpg')
	print(str(scale_w) + " " + str(scale_h))
	img2 = img2.resize((scale_w , scale_h));
	logo2 = ImageTk.PhotoImage(img2)
	w2.configure(image=logo2)
	w2.image = logo2





root = tk.Tk()

root.geometry("1000x550")	

root.title("Low Light Image Enhancement")

frame1 = Frame(master=root,height=200)
frame1.pack(fill=X)

frame2 = Frame(master=root,height=300)
frame2.pack(fill=X)

frame3 = Frame(master=root,height=200)
frame3.pack(fill=X)

frame4 = Frame(master=root,height=200)
frame4.pack(fill=X)

label1 = tk.Label(frame1,text="Original image",fg="red").pack(side = "left",padx=150,pady=50)

label2 = tk.Label(frame1,text="Converted image",fg="red").pack(side = "right",padx=150,pady=50)

scale_w = 400
scale_h = 250

img1 = image.open(path1)
img1 = img1.resize((scale_w , scale_h));

logo = ImageTk.PhotoImage(img1)
w1 = tk.Label(frame2, image=logo).pack(side="right",padx=10,pady=0)
img2 = image.open(path2)
img2 = img2.resize((scale_w , scale_h));

logo2 = ImageTk.PhotoImage(img2)
w2 = tk.Label(frame2, image=logo2)
w2.pack(side="left",padx=10,pady=20)

print(w2)

button_select = tk.Button(frame3,text='choose a file',fg="red",width=25,height=2)
button_select.bind('<Button>', upload_image)
button_select.pack(side="left",padx=115)

button = tk.Button(frame4,text='convert',fg="red",width=25,height=2,command=quit)
button.pack(side="bottom",pady=30)

root.mainloop()