
import cv2
import RealTimeRead #as RealTime
import time

#PC Cameraで写真取得

CapCam0 = cv2.VideoCapture(0)

# フレームレートの取得
CheckFps = CapCam0.get(cv2.CAP_PROP_FPS)

# フレームサイズの取得

PicWidth = CapCam0.get(cv2.CAP_PROP_FRAME_WIDTH)
PicHeight = CapCam0.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(CheckFps,"CheckFps")
print(PicWidth,"*",PicHeight)
#print(RealTime.strtime)
#キャプチャと表示
CapFlag=0
Cnttime=0

while True:

    (ReturnVal,Picture)=CapCam0.read()
    if ReturnVal:
        #Camera Live
        cv2.imshow("CamOn: 0", Picture)
        k=cv2.waitKey(1)
        if k==27:
            break
        elif k==67 or k==99:
            PersonNameInput = input("Let input Name: ")
            PersonNameOutput=str(PersonNameInput) + ".png"
            cv2.imwrite("BaseData/"+PersonNameOutput,Picture,[cv2.IMWRITE_PNG_COMPRESSION,3])
    else:
        print("Camera is not ready")
        break

    GetSecTime=int(time.mktime(time.localtime(time.time())))
    if CapFlag==0:
        Cnttime=GetSecTime + 30
        CapFlag=1
    elif Cnttime<=GetSecTime:
        PictureOutput="P"+str(GetSecTime)+ ".png"
        cv2.imwrite("PictureOut/" + PictureOutput,Picture,[cv2.IMWRITE_PNG_COMPRESSION,3])
        CapFlag=0

        # print(cv2.waitKey(30000))
#         while k!=27: # Key=ESC
#             if k==83 or k==115:
#                 PersonNameInput = input("Let input Name: ")
#                 PersonNameOutput=str(PersonNameInput) + ".png"
#                 cv2.imwrite("BaseData//"+PersonNameOutput,Picture,[cv2.IMWRITE_PNG_COMPRESSION,3])
# #                cv2.waitKey(30000)
#             elif k==67 or k==99:
#                 PictureOutput="P"+RealTime.strtime + ".png"
#                 cv2.imwrite("PictureOut//" + PictureOutput,Picture,[cv2.IMWRITE_PNG_COMPRESSION,3])
#  #               cv2.waitKey(30000)
    # else:
    #     print("Camera is not ready")
    #     break

CapCam0.release()
cv2.destroyAllWindows()

