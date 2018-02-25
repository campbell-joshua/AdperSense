import os
from PIL import Image
import psutil
import time

for filename in os.listdir("./images_test"):
    print(filename)
    img = Image.open("./images_test/"+filename)
    img.show()

    time.sleep(2)

    for proc in psutil.process_iter():
        if proc.name()=="display":
            proc.kill()

    cont = input("Continue?")
    if cont == "q":
        break
    elif cont == 'b':
        os.rename("./images_test/"+filename, "./garbage/0001"+filename)
    elif cont != "y":
        os.rename("./images_test/"+filename, "./bad_images/0001"+filename)
    else:
        os.rename("./images_test/"+filename, "./good_images/0001"+filename)
