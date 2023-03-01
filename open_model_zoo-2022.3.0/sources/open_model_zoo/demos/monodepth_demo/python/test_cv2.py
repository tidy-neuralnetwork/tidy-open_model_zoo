import cv2
import os 

testVideo=r'/root/open_model_zoo/sources/open_model_zoo/demos/monodepth_demo/python/test_data/videos/classroom.mp4'
assert os.path.exists(testVideo)
cap = cv2.VideoCapture(testVideo)
# 获取编码器
fourcc = cap.get(cv2.CAP_PROP_FOURCC)
# 输出编码器信息 如果返回 0.0 则说明没有设置编码器 安装ffmpeg解决 apt-get install ffmpeg
print('FourCC: {}'.format(fourcc))

print(f'----cap.isOpened():{cap.isOpened()}')
while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1280, 720))
    print("---shape:", frame.shape)
    cv2.imshow('image', frame)
    k = cv2.waitKey(20)
    if k & 0xff == ord('q'):
       break

cap.release()
cv2.destroyAllWindows()
