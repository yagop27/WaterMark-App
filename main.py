import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont

window = tk.Tk()
window.title('WaterMark App')
window.geometry("1200x800")

canvas = tk.Canvas(window, height=800, width=600)
canvas.pack(expand=1)


# Functions to drag and move the watermark above the image
def drag(click):
    widget = click.widget
    x, y = widget.coords(text_obj)

    widget.dx, widget.dy = click.x-x, click.y-y


def moving(click):
    widget = click.widget
    widget.coords(text_obj, (click.x-widget.dx, click.y-widget.dy))


# Saving the watermarked image as a file
def save():
    name = img_name.get(1.0, "end-1c")

    image = Image.open('Red_Bunny_Petland_Puppy.jpg')
    watermark = canvas.itemcget(text_obj, 'text')

    x, y = canvas.coords(text_obj)

    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()

    draw.text((x, y), watermark, font=font, fill=(255, 255, 255, 128))

    image.save(name + '.jpg')


# Function to edit the watermark text
def edit_text():
    watermark = type_watermark.get(1.0, "end-1c")
    canvas.itemconfig(text_obj, text=watermark)


# Opening and creating the label do display the image o tkinter
img_tk = ImageTk.PhotoImage(file='Red_Bunny_Petland_Puppy.jpg')
canvas.create_image(400, 300, anchor='center', image=img_tk)

# Creating text box to add a watermark to the image

type_watermark = tk.Text(window, height=1, width=50)
type_watermark.place(x=490, y=600)

text_obj = canvas.create_text(400, 300, text='default', font=60)

# Button to edit the watermark text
edit_button = tk.Button(window, height=1, width=10, command=edit_text, text='Edit', bg='blue')
edit_button.place(x=400, y=600)

# Text box for the image file name
img_name = tk.Text(window, height=1, width=50)
img_name.place(x=490, y=630)

# Button to save the image
save_button = tk.Button(window, height=1, width=10, command=save, text='Save', bg='blue')
save_button.place(x=400, y=630)


canvas.tag_bind(text_obj, "<Button-1>", drag)
canvas.tag_bind(text_obj, '<B1-Motion>', moving)

window.mainloop()
