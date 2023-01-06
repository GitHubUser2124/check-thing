import os
import cv2

path = "Images/"

images = []

for files in os.listdir(path):
    name, ext = os.path.splitext(files)

    if (ext in [".gif", ".png", ".jpeg", ".jpg", ".jfif"]):
        file_name = path+"/"+files
        print(file_name)
        images.append(file_name)

img_num = len(images)
frames = cv2.imread(images[0])
height, width, channels = frames.shape
size = (width, height)

output = cv2.VideoWriter("project.avi", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, img_num-1):
    frames = cv2.imread(images[i])
    output.write(frames)

output.release()

print("done")