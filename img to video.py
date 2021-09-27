import cv2
 
fps = 30 
size = (1920,1080) 
# 이미지 사이즈가 사진과 맞지 않으면 실행 되지
videowriter = cv2.VideoWriter("you.avi",cv2.VideoWriter_fourcc('M','J','P','G'),fps,size)


for i in range(1,925): 
    img = cv2.imread('you (copy)/%d.jpg' % i)
    videowriter.write(img)
    print(i)