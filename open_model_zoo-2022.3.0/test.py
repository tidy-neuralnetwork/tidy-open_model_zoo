import cv2
cap = cv2.VideoCapture('/data/home/tonye/tidy-neuralnetwork/tidy-open_model_zoo/open_model_zoo-2022.3.0/sources/open_model_zoo/demos/monodepth_demo/python/test_data/videos/classroom.mp4')
while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('image', frame)
    k = cv2.waitKey(20)
    if k & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
