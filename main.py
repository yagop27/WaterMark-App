import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

window = tk.Tk()
window.title('WaterMark App')
window.geometry("1200x800")

canvas = tk.Canvas(window, height=800, width=600)
canvas.pack(expand=1)

# Variables to hold the current image and image path
img_tk = None
selected_image_path = None


# Functions to drag and move the watermark above the image
def drag(click):
    widget = click.widget
    x, y = widget.coords(text_obj)

    widget.dx, widget.dy = click.x-x, click.y-y


def moving(click):
    widget = click.widget
    widget.coords(text_obj, (click.x-widget.dx, click.y-widget.dy))


# Function to open a file dialog to select an image
def select_image():
    global img_tk, selected_image_path
    selected_image_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )
    if selected_image_path:
        # Open the selected image and display it on the canvas
        image = Image.open(selected_image_path)
        image = image.resize((600, 400))  # Resize the image to fit the canvas
        img_tk = ImageTk.PhotoImage(image)
        canvas.create_image(400, 300, anchor='center', image=img_tk)

        # Remove any previous image and draw the new one
        canvas.delete("image")  # Delete the previous image (tagged as "image")
        canvas.create_image(400, 300, anchor='center', image=img_tk, tags="image")

        # Ensure watermark text stays on top of the image
        canvas.tag_raise(text_obj)


# Saving the watermarked image as a file
def save():
    if not selected_image_path:
        return  # If no image has been selected, do nothing

    name = img_name.get(1.0, "end-1c")
    image = Image.open(selected_image_path)
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


# Creating text box to add a watermark to the image
type_watermark = tk.Text(window, height=1, width=50)
type_watermark.place(x=490, y=600)

text_obj = canvas.create_text(400, 300, text='default', font=100, fill='black')

# Button to edit the watermark text
edit_button = tk.Button(window, height=1, width=10, command=edit_text, text='Edit', bg='light blue')
edit_button.place(x=400, y=600)

# Text box for the image file name
img_name = tk.Text(window, height=1, width=50)
img_name.place(x=490, y=630)

# Button to save the image
save_button = tk.Button(window, height=1, width=10, command=save, text='Save', bg='light blue')
save_button.place(x=400, y=630)

# Button to select an image
select_image_button = tk.Button(window, height=1, width=10, command=select_image, text='Select Image', bg='light green')
select_image_button.place(x=400, y=560)

canvas.tag_bind(text_obj, "<Button-1>", drag)
canvas.tag_bind(text_obj, '<B1-Motion>', moving)

window.mainloop()
