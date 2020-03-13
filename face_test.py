from PIL import Image, ImageDraw
import face_recognition
from sys import argv, exit

f = "./images/kate.jpg"
if len(argv) == 2:
    f = f"./images/{argv[1]}.jpg"
else:
    exit(1)

image = face_recognition.load_image_file(f)
pil_image = Image.open(f).convert("RGBA")

faces = face_recognition.face_locations(image)

for face in faces:
    top, right, bottom, left = face

    # Output all the found faces
    # face_image = image[top:bottom, left:right]
    # pil_image = Image.fromarray(face_image)
    # pil_image.show()

    draw = ImageDraw.Draw(pil_image)
    # draw.rectangle(((left, bottom), (right, top)), outline='red')
    draw.line([(right, top), (right, bottom), (left, bottom), (left, top), (right, top)], fill='red', width=10)

pil_image.show()