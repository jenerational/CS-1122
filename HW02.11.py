from PIL import Image, ImageFont, ImageDraw
import random

def first():
    name = input("Name for logo:")
    #Total Size
    size = 240, 300
    
    logo_base = Image.new('RGBA', size, color=0)
    
    #Background
    face = ImageDraw.Draw(logo_base)
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255))

    #Draws mouth
    face.rectangle([(20,20),(220,220)], fill=color)
    face.pieslice([(50,100),(200,150)], 30, 125, fill=(255,255,255,255))
    face.pieslice([(50,100),(200,145)], 30, 125, fill=color)

    #Draws eyes
    face.ellipse((55, 50, 80, 75), fill = 'white')
    face.ellipse((155, 50, 179, 74), fill = 'white')

    #Writes text
    font = ImageFont.truetype("Arial.ttf", 20)
    sizeOfText = face.textsize(name, font = font)
    #Centers text
    leftEdgeOfBox, rightEdgeOfBox = size
    leftEdgeOfText, rightEdgeOfText = sizeOfText
    offset = leftEdgeOfBox - leftEdgeOfText
    face.text((offset/2, 250), name, font = font, fill = 'gray')

    #Saves and outputs text
    logo_base.save("Icon.jpg")
    logo_base.show()

first()
