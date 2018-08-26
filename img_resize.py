import glob
from PIL import Image

imglist = glob.glob("./test/*.jpg")

num = 0
for img_path in imglist:
    try:
        img = Image.open(img_path)
        print(img_path, img.size, str(num) + ".jpg")
        img.resize((250, 250)).save("./o_resize_250_square/resize" + str(num) + ".jpg")
        num = num + 1
    except:
        print("Error Occur")