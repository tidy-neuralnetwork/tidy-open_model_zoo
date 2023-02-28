import cv2
cap = cv2.VideoCapture('/root/open_model_zoo/sources/open_model_zoo/demos/monodepth_demo/python/test_data/videos/classroom.mp4')

while(cap.isOpened()):
    print("-------------------")
    ret, frame = cap.read()
    print("---shape:", frame.shape)
    #cv2.imshow('image', frame)
    #k = cv2.waitKey(20)
    #if k & 0xff == ord('q'):
    #    break

cap.release()
cv2.destroyAllWindows()
