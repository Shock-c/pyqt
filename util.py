import hashlib
import os
import random

# http://t.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=0&fa=0&fetch_key=&groupid=0&qty=20&time=100&pro=&city=&port=1&format=txt&ss=1&css=&dt=1&specialTxt=3&specialJson=&usertype=2
# http://t.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=0&fa=0&fetch_key=&groupid=0&qty=1&time=1&pro=&city=&port=1&format=txt&ss=1&css=&dt=1&specialTxt=3&specialJson=&usertype=2
# http://t.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=0&fa=0&fetch_key=&groupid=0&qty=20&time=100&pro=&city=&port=1&format=txt&ss=1&css=&dt=1&specialTxt=3&specialJson=&usertype=2
# http://t.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=0&fa=0&fetch_key=&groupid=0&qty=20&time=100&pro=&city=&port=1&format=txt&ss=1&css=&dt=1&specialTxt=3&specialJson=&usertype=2
# http://t.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=0&fa=0&fetch_key=&groupid=0&qty=20&time=100&pro=&city=&port=1&format=txt&ss=1&css=&dt=1&specialTxt=3&specialJson=&usertype=2
#
# http://ip.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=0&fa=0&fetch_key=&groupid=0&qty=5&time=101&pro=&city=&port=1&format=txt&ss=1&css=&dt=1&specialTxt=3&specialJson=&usertype=2
# http://ip.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=0&fa=0&fetch_key=&groupid=0&qty=5&time=100&pro=%E5%B9%BF%E4%B8%9C%E7%9C%81&city=%E7%8F%A0%E6%B5%B7%E5%B8%82&port=1&format=txt&ss=1&css=&dt=1&specialTxt=3&specialJson=&usertype=2


import cv2
import requests

filePath = 'dd.png'

img = cv2.imread(filePath)
h, w, _ = img.shape
img = cv2.resize(img,(w-200, h))
img = cv2.GaussianBlur(img,(5,5),15)
cv2.imwrite('vc1.png', img)


# h, w, _ = img.shape

# for i in range(45500): #生成1000个噪点
#     a = random.randint(0,767)
#     b = random.randint(0,1023)
#     img[a,b] = 255
# print()
# url = 'https://qlogo1.store.qq.com/qzone/1403587760/1403587760/200?0'
# rsp = requests.get(url)
# pic_str = str(random.randint(0,100))+str(1403587760)+'.png'
# file = open(pic_str,'wb')
# file.write(rsp.content)
# file.close()
# cv2.imwrite(pic_str, img)
# img1 = cv2.imread(pic_str)
# img2 = cv2.resize(img1, (w, h), interpolation=cv2.INTER_AREA)
# img = cv2.addWeighted(img2, 0.2, img, 0.8, 0)
#
#
#
# cv2.imwrite(pic_str, img)


# img1 = cv2.imread('vc.png')
# img2 = cv2.imread('dd.png')
# cv2.imwrite('vc1.png',img2)
#
# # I want to put logo on top-left corner, So I create a ROI
# rows,cols,channels = img2.shape
# img1 = cv2.resize(img1,(cols+100,rows+100))
#
# img1[50:rows+50, 50:cols+50 ] = img2
#
# cv2.imwrite("vc1.png", img1)

# filePath = 'vc1.png'
# # img = cv2.imread(filePath)
# # h, w, _ = img.shape
# url = 'https://qlogo1.store.qq.com/qzone/{0}/{0}/100?0'.format(525258607)
# try:
#     rsp = requests.get(url)
# except:
#     pass
# pic_str = str(random.randint(0, 100)) + str(11111) + '.png'
# try:
#     file = open(pic_str, 'wb')
#     file.write(rsp.content)
#     file.close()
# except:
#     if file != None:
#         file.close()
#
# img1 = cv2.imread(pic_str)
# img2 = cv2.imread(filePath)
#
# # I want to put logo on top-left corner, So I create a ROI
# rows, cols, channels = img2.shape
# img1 = cv2.resize(img1, (cols + 200, rows + 200))
# img1[100:rows + 100, 100:cols + 100] = img2
# cv2.imwrite(pic_str, img1)
