import os
import cv2

for filename in os.listdir("./images_test"):
    #print(filename)
    img = cv2.imread("./images_test/"+filename)
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image',1400,1400)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("'q' to quit\n'b' to throw out image\n'y' for good image")
    cont = input("'n' or any other key for bad image")
    if cont == "q":
        break
    elif cont == 'b':
        os.rename("./images_test/"+filename, "./garbage/"+filename)
    elif cont != "y":
        os.rename("./images_test/"+filename, "./bad_images2/"+filename)
    else:
        os.rename("./images_test/"+filename, "./good_images2/"+filename)

