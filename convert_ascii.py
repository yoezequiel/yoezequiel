import urllib.request
from PIL import Image
import io

url = "https://avatars.githubusercontent.com/u/94125820?v=4"
req = urllib.request.urlopen(url)
img = Image.open(io.BytesIO(req.read()))

width = 44
height = 25
img = img.resize((width, height), Image.Resampling.LANCZOS)
img = img.convert("L")

chars = "@%#*+=-:. " # 10 chars, from dark to light

lines = []
y_pos = 30
for y in range(height):
    line = ""
    for x in range(width):
        pixel = img.getpixel((x, y))
        # pixel is 0 to 255. 
        idx = int((pixel / 255) * (len(chars) - 1))
        line += chars[idx]
    lines.append(f'<tspan x="15" y="{y_pos}">{line}</tspan>')
    y_pos += 20

print("\n".join(lines))
