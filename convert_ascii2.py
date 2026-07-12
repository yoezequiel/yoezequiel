import urllib.request
from PIL import Image
import io
import ssl

url = "https://media.licdn.com/dms/image/v2/D4D03AQEdiLF1XAbXoA/profile-displayphoto-scale_400_400/B4DZ85PCFvK0Ag-/0/1783371673295?e=1785369600&v=beta&t=DS8sJ-v8dF-ghjkgjvEbCCEC5GSqL22eJ2u1Gm21db8"
context = ssl._create_unverified_context()
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req, context=context)
img = Image.open(io.BytesIO(resp.read()))

width = 44
height = 25
img = img.resize((width, height), Image.Resampling.LANCZOS)
img = img.convert("L")

chars = "@%#*+=-:. "

lines = []
y_pos = 30
for y in range(height):
    line = ""
    for x in range(width):
        pixel = img.getpixel((x, y))
        idx = int((pixel / 255) * (len(chars) - 1))
        line += chars[idx]
    lines.append(f'<tspan x="15" y="{y_pos}">{line}</tspan>')
    y_pos += 20

print("\n".join(lines))
