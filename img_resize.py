import glob
from PIL import Image

imglist = glob.glob("./banana_dataset/*.jpg")

num = 0
for img_path in imglist:
    img = Image.open(img_path)
    print(img_path, img.size, "./resize/resize" + str(num) + ".jpg")
    img.resize((600, 600)).save("./resize_500_square/resize" + str(num) + ".jpg")
    num = num + 1