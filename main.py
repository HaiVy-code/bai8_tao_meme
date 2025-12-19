from guizero import App, Box, Text, TextBox, ListBox, Combo, ButtonGroup, Slider, PushButton, Drawing, Picture
import os
from PIL import Image

current_images_path = None

def show_picture(selected):
    global current_images_path
    original_path = f"images/{selected}"
    fitted = fit_image(original_path, drawing.width, drawing.height)
    current_images_path = fitted
    drawing.clear()
    drawing.image(0, 0, current_images_path)

def upload_picture():
    picture = []
    for f in os.listdir("images"):
        if f.endswith((".png", ".jpg", ".jpeg")):
            picture.append(f)
    return picture

def update_meme():
    drawing.clear()
    if current_images_path:
        drawing.image(0, 0, current_images_path)
    drawing.text(x = slider1.value, y = slider2.value, text = textbox.value, color = combo1.value, font = buttongroup.value, size = 20)
    if combo2.value == "star": 
        drawing.text(10, 10, "⭐", size = 30) 
    elif combo2.value == "nerd": 
        drawing.text(10, 10, "🤓", size = 30)
    elif combo2.value == "fire": 
        drawing.text(10, 10, "🔥", size = 30)
    else:
        drawing.text(10, 10, "", size = 30)

def fit_image(path, box_w, box_h):
    imgage = Image.open(path)
    imgage.thumbnail((box_w, box_h))
    temp = "temp_fit.png"
    imgage.save(temp)
    return temp

cuaso = App(title = "Meme creator", height = 550, width = 550)
box1 = Box(cuaso, layout = "grid", border = True)
chu1 = Text(box1, text = "Enter text:", grid = [0, 0])
textbox = TextBox(box1, width = 15, grid = [1, 0])
chu2 = Text(box1, text = "Select text color:", grid = [0, 1])
combo1 = Combo(box1, options = ("black", "blue", "green", "yellow", "white"), selected = "black", grid = [1, 1])
chu3 = Text(box1, text = "Select font:", grid = [0, 2])
buttongroup = ButtonGroup(box1, options = ["Arial", "Times New Roman", "Courier"], grid = [1, 2])
box2 = Box(cuaso, layout = "grid")
chu4 = Text(box2, text = "Select meme sticker:", grid = [0, 0])
combo2 = Combo(box2, options = ("star", "nerd", "fire", "none"), grid = [1, 0])
box3 = Box(cuaso, layout = "grid")
chu5 = Text(box3, text = "X", grid = [0, 0])
slider1 = Slider(box3, start = 5, end = 300, grid = [1, 0])
chu6 = Text(box3, text = "Y", grid = [0, 1])
slider2 = Slider(box3, start = 0, end = 220, grid = [1, 1])
pushbutton = PushButton(cuaso, text = "Add meme", command = update_meme)
listbox = ListBox(cuaso, items = upload_picture(), align = "left", command = show_picture)
drawing = Drawing(cuaso, width = 350, height = 260)
cuaso.display()
