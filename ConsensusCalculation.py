import os
from shutil import copyfile

def if_statements(i, count, filename):
    if filename in os.listdir("./good_images1"):
        i += 1
        count += 1
    if filename in os.listdir("./good_images2"):
        i += 1
        count += 1
    if filename in os.listdir("./bad_images1"):
        count += 1
    if filename in os.listdir("./bad_images2"):
        count += 1
    return float(i/count)

def main():
    for filename in os.listdir("./good_images"):
        count = 1
        i = 1
        percent = if_statements(i, count, filename)
        if (percent > .5):
            copyfile("./good_images/"+filename, "./final_good/"+filename)
        else:
            copyfile("./good_images/" + filename, "./final_bad/" + filename)

    for filename in os.listdir("./bad_images"):
        count = 1
        i = 0
        percent = if_statements(i, count, filename)
        if (percent > .5):
            copyfile("./bad_images/"+filename, "./final_good/"+filename)
        else:
            copyfile("./bad_images/" + filename, "./final_bad/" + filename)