# Python program to take
# screenshots


import numpy as np
import cv2
import pyautogui


# take screenshot using pyautogui
image = pyautogui.screenshot()
# image.save(r'C:\Users\Yaswanthi\PycharmProjects\screenshot\myimage.png')
# since the pyautogui takes as a
# PIL(pillow) and in RGB we need to
# convert it to numpy array and BGR
# so we can write it to the disk

# image = cv2.cvtColor(np.array(image),
# 					cv2.COLOR_RGB2BGR)
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# folder = '/Users/jia/someFolder';
# imwrite(imedge,fullfile(folder,'binaryeye.jpg'));
# writing it to the disk using opencv

# image.save(r'C:\Users\Yaswanthi\PycharmProjects\screenshot\myimage.png')-----
cv2.imwrite('C:\\Users\\Yaswanthi\\PycharmProjects\\screenshot\\myimage.png', image)
# cv2.imwrite(os.path.join(path, '/hall.jpg'), image)
# working_path = os.getcwd()
# # sub_directory = "Image"
# # path = os.path.join(working_path, sub_directory)
# path = working_path
# os.makedirs(path, exist_ok = True)