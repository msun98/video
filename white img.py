import cv2
import numpy as np

img1 = np.ones((1080,1920,3),np.uint8)*255
cv2.imshow('img1',img1)

# img1 = cv2.imread('you/1.jpg' )

print(img1.shape)
# cv2.imshow('img1',img1)
cv2.imwrite("you (copy)/755.jpg", img1)

k = cv2.waitKey(0)  # 키보드 눌림 대기
if k == 27:  # ESC키
    cv2.destroyAllWindows();