import argparse

def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='rtsp://admin:ly123456@10.62.90.20:554/Streaming/Channels/3101')
    parser.add_argument('--output', type=str, default='/data/home/baseuser/zto-workspace/tidy-deepstream/tidy-deepstream-6.1/datasets/labelme/Images/laiyang/10_62_90_20_3101.jpg')

    return parser.parse_args()

args = init_args()

import cv2
cap = cv2.VideoCapture(args.input)

if cap.isOpened():
        open,frame = cap.read()
else:
        open = False

while open :
    ret,frame=cap.read()
    if  frame is None:
        break
    if ret == True:
        #RGB=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        print(frame.shape)
        cv2.imwrite(args.output, frame)
        #cv2.imshow("video",frame)
        # if cv2.waitKey(20) & 0xFF == 27:
        #     break
cap.release()
cv2.destroyAllWindows()
