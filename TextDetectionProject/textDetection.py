import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# pytesseract only accepts RGB values
# While OpenCV accepts BGR values

img = cv2.imread('2.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))


# ### Detecting Characters
# # print(pytesseract.image_to_boxes(img))
# # This returns like:
# # G 229 424 266 472 0
# # Char x y (width height)--> these are of bounding box
#
# hImg,wImg,_ = img.shape
# boxes = pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
#     # print(b)
#     b = b.split(' ')
#     print(b)
#     x1, y1, x2, y2 = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#
#     # Tesseract uses the bottom-left corner as the origin (0, 0) while OpenCV uses the top-left corner as the origin.
#     # pytesseract.image_to_boxes are in the format char x1 y1 x2 y2
#     # where (x1, y1) is the bottom-left corner and (x2, y2) is the top-right corner of the bounding box.
#     # In OpenCV, you will need to adjust y1 and y2.
#
#     # Adjust the y-coordinates
#     y1 = hImg - y1
#     y2 = hImg - y2
#
#     # Draw rectangle
#     cv2.rectangle(img, (x1, y2), (x2, y1), (0, 0, 255), 2)
#     cv2.putText(img,b[0],(x1,y1+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)


# ## Detecting Words
# hImg,wImg,_ = img.shape
# boxes = pytesseract.image_to_data(img)
# for x,b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b = b.split()
#         print(b)
#         if len(b)==12:
#             x1, y1 = int(b[6]), int(b[7])
#             width, height = int(b[8]), int(b[9])
#             x2, y2 = x1 + width, y1 + height
#
#             # Draw rectangle
#             cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
#             cv2.putText(img,b[11],(x1,y1-10),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

#
# ## Detecting words of ONLY NUMBERS
# hImg,wImg,_ = img.shape
# cong = r'--oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_data(img,config=cong)
# for x,b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b = b.split()
#         print(b)
#         if len(b)==12:
#             x1, y1 = int(b[6]), int(b[7])
#             width, height = int(b[8]), int(b[9])
#             x2, y2 = x1 + width, y1 + height
#
#             # Draw rectangle
#             cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
#             cv2.putText(img,b[11],(x1,y1-10),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

### Detecting Characters of ONLY NUMBERS
# print(pytesseract.image_to_boxes(img))
# This returns like:
# G 229 424 266 472 0
# Char x y (width height)--> these are of bounding box

hImg,wImg,_ = img.shape
# For details of this cong , SEE IMAGES UPLOADED IN THIS ALONG WITH 2.png
cong = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_boxes(img,config=cong)
for b in boxes.splitlines():
    # print(b)
    b = b.split(' ')
    print(b)
    x1, y1, x2, y2 = int(b[1]), int(b[2]), int(b[3]), int(b[4])

    # Tesseract uses the bottom-left corner as the origin (0, 0) while OpenCV uses the top-left corner as the origin.
    # pytesseract.image_to_boxes are in the format char x1 y1 x2 y2
    # where (x1, y1) is the bottom-left corner and (x2, y2) is the top-right corner of the bounding box.
    # In OpenCV, you will need to adjust y1 and y2.

    # Adjust the y-coordinates
    y1 = hImg - y1
    y2 = hImg - y2

    # Draw rectangle
    cv2.rectangle(img, (x1, y2), (x2, y1), (0, 0, 255), 2)
    cv2.putText(img,b[0],(x1,y1+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)


cv2.imshow('Result',img)

cv2.waitKey(0)