import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont


class WatermarkApp:
    def __init__(self, window):
        self.type_watermark = None
        self.img_name = None
        self.window = window
        self.window.title('WaterMark App')
        self.window.geometry("1200x800")

        # Canvas setup
        self.canvas = tk.Canvas(self.window, height=800, width=600)
        self.canvas.pack(expand=1)

        # Initialize variables
        self.img_tk = None
        self.selected_image_path = None

        # UI setup
        self.setup_ui()

        # Initialize watermark text object
        self.text_obj = self.canvas.create_text(400, 300, text='default', font=100, fill='black')
        self.canvas.tag_bind(self.text_obj, "<Button-1>", self.drag)
        self.canvas.tag_bind(self.text_obj, '<B1-Motion>', self.moving)

    def setup_ui(self):
        """Set up all the UI components like buttons and text boxes."""
        # Watermark input box
        self.type_watermark = tk.Text(self.window, height=1, width=50)
        self.type_watermark.place(x=490, y=600)

        # Edit watermark button
        edit_button = tk.Button(self.window, height=1, width=10, command=self.edit_text, text='Edit', bg='light blue')
        edit_button.place(x=400, y=600)

        # Image file name input box
        self.img_name = tk.Text(self.window, height=1, width=50)
        self.img_name.place(x=490, y=630)

        # Save image button
        save_button = tk.Button(self.window, height=1, width=10, command=self.save_image, text='Save', bg='light blue')
        save_button.place(x=400, y=630)

        # Select image button
        select_image_button = tk.Button(self.window, height=1, width=10, command=self.select_image, text='Select Image',
                                        bg='light green')
        select_image_button.place(x=400, y=560)

    def drag(self, click):
        """Handle dragging of the watermark text."""
        widget = click.widget
        x, y = widget.coords(self.text_obj)
        widget.dx, widget.dy = click.x - x, click.y - y

    def moving(self, click):
        """Handle moving of the watermark text."""
        widget = click.widget
        widget.coords(self.text_obj, (click.x - widget.dx, click.y - widget.dy))

    def select_image(self):
        """Open file dialog to select an image and display it on the canvas."""
        self.selected_image_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
        )
        if self.selected_image_path:
            image = Image.open(self.selected_image_path)
            image = image.resize((600, 400))  # Resize the image to fit the canvas
            self.img_tk = ImageTk.PhotoImage(image)

            # Remove any previous image and draw the new one
            self.canvas.delete("image")
            self.canvas.create_image(400, 300, anchor='center', image=self.img_tk, tags="image")

            # Ensure watermark text stays on top of the image
            self.canvas.tag_raise(self.text_obj)

    def edit_text(self):
        """Update the watermark text based on user input."""
        watermark = self.type_watermark.get(1.0, "end-1c")
        self.canvas.itemconfig(self.text_obj, text=watermark)

    def save_image(self):
        """Save the watermarked image to a file."""
        if not self.selected_image_path:
            return  # No image selected, do nothing

        name = self.img_name.get(1.0, "end-1c")
        image = Image.open(self.selected_image_path)
        watermark = self.canvas.itemcget(self.text_obj, 'text')

        x, y = self.canvas.coords(self.text_obj)

        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()

        draw.text((x, y), watermark, font=font, fill=(255, 255, 255, 128))

        image.save(name + '.jpg')


if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
