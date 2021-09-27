import numpy as np
import cv2 as cv
import time
# from utils import CvFpsCalc

cap = cv.VideoCapture('you.mp4')
# cap = cv.VideoCapture(0)
# cvFpsCalc = CvFpsCalc(buffer_len=10)

width = cap.get(cv.CAP_PROP_FRAME_WIDTH) # 또는 cap.get(3)
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT) # 또는 cap.get(4)
prevTime = 0 #이전 시간을 저장할 변수
# fps = cap.get(cv.CAP_PROP_FPS) # 또는 cap.get(5)
print('프레임 너비: %d, 프레임 높이: %d' %(width, height))

while cap.isOpened(): # cap 정상동작 확인
    ret, frame = cap.read()
    # display_fps = cvFpsCalc.get()
    # prevTime = time.time()
    # 프레임이 올바르게 읽히면 ret은 True
    if not ret:
        print("프레임을 수신할 수 없습니다(스트림 끝?). 종료 중 ...")
        break
    # frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #현재 시간 가져오기 (초단위로 가져옴)
    curTime = time.time()

    #현재 시간에서 이전 시간을 빼면?
    #한번 돌아온 시간!!
    sec = curTime - prevTime
    #이전 시간을 현재시간으로 다시 저장시킴
    prevTime = curTime
    FPS =  round(1/(sec),2)

    cv.putText(frame, "FPS:" + str(FPS), (10, 30),
               cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv.LINE_AA)
    cv.imshow('Otter', frame)
    # if cv.waitKey(42) == ord('q'):
    #     break
    # if cv.waitKey(10) >= 0:
    #    break
    key = cv.waitKey(30)
    if key == 27:  # ESC
        break
# 작업 완료 후 해제
cap.release()
cv.destroyAllWindows()

# #!/opt/local/bin/python
# # -*- coding: utf-8 -*-
# import cv2

# ########### 추가 ##################
# import time # time 라이브러리
# ###################################

# CAM_ID = 0

# cam = cv2.VideoCapture(CAM_ID) #카메라 생성
# if cam.isOpened() == False: #카메라 생성 확인
#     print('Can\'t open the CAM(%d)' % (CAM_ID)) 
#     exit()

# #윈도우 생성 및 사이즈 변경
# cv2.namedWindow('CAM_Window')

# ########### 추가 ##################
# prevTime = 0 #이전 시간을 저장할 변수
# ###################################
# while(True):

#     #카메라에서 이미지 얻기
#     ret, frame = cam.read()
     

#     ########### 추가 ##################
#     #현재 시간 가져오기 (초단위로 가져옴)
#     curTime = time.time()

#     #현재 시간에서 이전 시간을 빼면?
#     #한번 돌아온 시간!!
#     sec = curTime - prevTime
#     #이전 시간을 현재시간으로 다시 저장시킴
#     prevTime = curTime

#     # 프레임 계산 한바퀴 돌아온 시간을 1초로 나누면 된다.
#     # 1 / time per frame
#     fps = 1/(sec)

#     # 디버그 메시지로 확인해보기
#     print ("Time {0} " . format(sec))
#     print ("Estimated fps {0} " . format(fps))

#     # 프레임 수를 문자열에 저장
#     str = "FPS : %0.1f" % fps

#     # 표시
#     cv2.putText(frame, str, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
#     ###################################


#     #얻어온 이미지 윈도우에 표시
#     cv2.imshow('CAM_Window', frame)


#     #10ms 동안 키입력 대기
#     if cv2.waitKey(10) >= 0:
#        break;

# #윈도우 종려
# cam.release()
# cv2.destroyWindow('CAM_Window')