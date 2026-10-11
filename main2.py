from PIL import Image
import turtle
import random
import time
from pathlib import Path

PHRASE = ["ॐ", "दुं", "श्री", "जय", "माँ"]

# Load the image from the same folder as this Python file
image_path = Path(__file__).parent / "durga devi.jpg"
image = Image.open(image_path).convert("L")

# Resize the image for more detail
width = 160
height = int(image.height * width / image.width)
image = image.resize((width, height))

# Find the darker pixels that form the figure
threshold = 200
pixels = []

for y in range(height):
    for x in range(width):
        if image.getpixel((x, y)) < threshold:
            pixels.append((x, y))

# Set up the Turtle window
screen = turtle.Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("जय माता दी")
screen.tracer(0, 0)

# Set the writing color to vivid orange
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("#FF6600")

# Character spacing and artwork position
PIXEL_SIZE = 5
start_x = -(width * PIXEL_SIZE) / 2
start_y = (height * PIXEL_SIZE) / 2

# Animation speed
PIXELS_PER_FRAME = 25
ANIMATION_DELAY = 0.001


def draw_animation():
    pen.clear()

    pixels_to_draw = pixels.copy()
    random.shuffle(pixels_to_draw)

    for i in range(0, len(pixels_to_draw), PIXELS_PER_FRAME):
        group = pixels_to_draw[i:i + PIXELS_PER_FRAME]

        for x, y in group:
            pos_x = start_x + x * PIXEL_SIZE
            pos_y = start_y - y * PIXEL_SIZE

            pen.goto(pos_x, pos_y)
            character = random.choice(PHRASE)
            pen.write(
                character,
                align="center",
                font=("Noto Sans Devanagari", 5, "normal")
            )

        screen.update()
        time.sleep(ANIMATION_DELAY)


def replay(x, y):
    draw_animation()


# Start the animation. Click the window to replay it.
screen.onclick(replay)
draw_animation()
screen.mainloop()