# Durga Devi Python Art Animation

This project creates an animated text-art version of a Durga Devi image using Python. It uses orange Devanagari characters on a black background.

## Requirements

- Python
- Pillow library

Install Pillow in the VS Code terminal:

```powershell
python -m pip install Pillow
```

## Image file

The Python code is set to use this image:

```text
C:\Users\madhu\OneDrive\Desktop\durga devi.jpg
```

If you move the image, update the `image_path` line in `main1.py`.

## Run the animation

Open the project folder in VS Code. In the terminal, run:

```powershell
python main1.py
```

A Turtle window will open and draw the image using characters. Click inside the window to replay the animation.

## Adjust the animation

In `main1.py`:

- Change `PHRASE` to use different characters.
- Change `threshold` to include more or fewer image details.
- Change `ANIMATION_DELAY` to adjust the animation speed.
- Change `PIXEL_SIZE` to adjust character spacing.