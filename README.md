<h1>Watermark App</h1>

A simple GUI-based watermarking application built with Python, using Tkinter and Pillow (PIL). This app allows users to add custom watermarks to images, position the watermark using mouse drag, and save the edited image to the computer.

<h2>Features:</h2>

- Select Image: Choose a image file from the computer to add the watermark using a filedialog (it can be a .jpg, .jpeg, .png, .bmp, and .gif).

- Custom Watermark text: You can input any text to add as a watermark on the image.
  
- Position the Watermark: The watermark can be dragged with the mouse and positioned anywhere on the image.
  
- Save Image: Save the image with the watermark by specifying a file name.

<h2>Prerequisites:</h2>

  - Python 3.6 or higher installed on your system.
  
  - Pillow library installed. Run the following command to install it:
  ##
      python watermark_app.py

<h2>Running the application:</h2>

1- Clone this repository or download the project files.

2- Install the necessary prerequisites.

3- Run the Python script to start the application.

    python watermark_app.py
  
4- After lauching the app, do the following:

  - Select an Image: Click the "Select Image" button and choose an image from your computer.
    
  - Edit Watermark: Type your desired watermark text into the input box and click "Edit" to update the watermark on the image.
    
  - Position the Watermark: Click and drag the watermark text on the image to position it where you want.
    
  - Save the Image: Enter a name for the output file and click "Save" to save the watermarked image to your computer.
    

<h2>Code Structure:</h2>

  This project is structured using an Object-Oriented Programming (OOP) approach, which makes the code more readable and maintainable. The key components of the application are as follows:
  
  - __init__(self, root): Initializes the GUI elements and canvas.
    
  - setup_ui(self): Sets up the user interface (buttons, text boxes, etc.).
    
  - select_image(self): Opens the file dialog to select an image.
    
  - edit_text(self): Updates the watermark text.
    
  - save_image(self): Saves the watermarked image to the computer.
    
  - drag(self, click) and moving(self, click): Handles dragging and positioning of the watermark.

<h2>Future Improvements:</h2>

  - Font Customization: Allow users to choose the font style, size, and color of the watermark text.
    
  - Transparency: Add the ability to adjust the opacity of the watermark.
    
  - Image Format Options: Save the watermarked image in different file formats (e.g., .png, .jpeg, etc.).
    
  - Multiple Watermarks: Support for adding multiple watermarks to a single image.

<h2>License</h2>
This project is open-source and available under the MIT License.

<h2>Contact</h2>
If you have any questions, feel free to reach out to me at yagopais@id.uff.br.

