#imports
import qrcode

import PIL as pl
from PIL import Image, ImageTk

from tkinter import *
from tkinter import filedialog as fd

#root
root = Tk()

#window settings
root.title("QR Code Generator")
root.geometry("500x600")
root.resizable(0, 0)

#values
qr = qrcode.QRCode()
qr.add_data("Made by Lennektro")
qr_image = qr.make_image()
qr_image.save("temp.png")

#value label
input_label = Label(root, text = "Value:")
input_label.config(font=("Times New Roman", 16))
input_label.place(x = 215, y = 7)

#value text box
value_box = Text(root, width = 55, height = 1)
value_box.place(x = 25, y = 42)

#genearte button
def click_generate_button():
    qr = qrcode.QRCode()
    qr.add_data(value_box.get("1.0",END))
    qr_image = qr.make_image()
    qr_image.save("temp.png")
    i = pl.Image.open("temp.png").resize((400, 400), pl.Image.ANTIALIAS)
    img = pl.ImageTk.PhotoImage(i)
    display_qrcode.config(image = img)
    display_qrcode.image = img

generate_button = Button(root, text = "Generate", width = 10, height = 2, command = click_generate_button)
generate_button.place(x = 203, y = 75)

#display qrcode
i = pl.Image.open("temp.png").resize((400, 400), pl.Image.ANTIALIAS)
img = pl.ImageTk.PhotoImage(i)
display_qrcode = Label(root, image = img)
display_qrcode.place(x = 45, y = 125)

#save button
def click_save_button():
    dialog = fd.asksaveasfilename(filetypes=(("PNG File", "*.png"), ("Something", "*.*")), title="Select Location where the QR Code should be saved as .png")
    image_outfile = dialog
    if image_outfile.endswith(".png") == False:
        image_outfile = image_outfile + ".png"
    img = pl.Image.open("temp.png")
    img.save(image_outfile)

save_button = Button(root, text = "Save", width = 10, height = 1, command = click_save_button)
save_button.place(x = 203, y = 550)

#mainloop of root
root.mainloop()
