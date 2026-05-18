# core packages -> https://docs.python.forg/3/library

import turtle
from PIL import Image

# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(2)
# t.circle(150)
# turtle.done()

# my_file = open("material/message.txt", "r")
# try:
#     content = my_file.read()
#     print("content:", content)
# finally:
#     my_file.close()

# with open("material/message.txt", "r") as file:
#     content = file.read()
#     print("(with) content:", content)


# with Image.open("material/person.JPG") as img:
#     resized_img = img.resize((200, 200))
#     resized_img.show()
#     resized_img.save("material/sample.png")


def get_sum(*args):
    total = 0
    for x in args:
        total += x
    return total


sum = get_sum(1, 2, 3, 4)
print("sum:", sum)
