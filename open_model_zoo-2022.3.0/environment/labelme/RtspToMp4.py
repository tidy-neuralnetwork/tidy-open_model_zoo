# -*- coding:utf-8 -*-
import sys

from datetime import datetime

__author__ = 'tonye'

import argparse
import cv2
import time
import os


def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rtsp_uri', type=str)
    parser.add_argument('--out_path', type=str)
    parser.add_argument('--center_id', type=str)
    parser.add_argument('--position_code', type=str)
    parser.add_argument('--camera_code', type=str)
    parser.add_argument('--start_time', type=str)
    parser.add_argument('--end_time', type=str)


    return parser.parse_args()


i_args = init_args()

if __name__ == '__main__':

    basename = i_args.center_id + "-" + i_args.position_code + "-" + i_args.camera_code

    start_time = time.mktime(time.strptime(i_args.start_time, "%Y%m%d%H%M%S"))
    end_time = time.mktime(time.strptime(i_args.end_time, "%Y%m%d%H%M%S"))

    cap = cv2.VideoCapture(i_args.rtsp_uri)

    write_ok = False

    sz = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
          int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fps = 30
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

    vout = cv2.VideoWriter()

    mkdirlambda = lambda x: os.makedirs(x) if not os.path.exists(x) else True  # 目录是否存在,不存在则创建
    mkdirlambda(i_args.out_path)

    vout.open(i_args.out_path + '/' + i_args.start_time + '_' + basename + '.mp4',
              fourcc, fps, sz, True)

    while True:

        time_now = int(time.time())
        print("time_now:"+str(datetime.now().strftime('%Y%m%d%H%M%S')))
        if time_now >= start_time:
            print("save video")
            ret, frame = cap.read()

            datestr = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            if int(datestr.split(":")[-2][-1])%2 == 0 and datestr.split(":")[-1] == "00":
                vout = cv2.VideoWriter()
                vout.open(i_args.out_path + '/' + str(datetime.now().strftime('%Y%m%d%H%M%S')) + '_' + basename + '.mp4',
                          fourcc, fps, sz, True)

            vout.write(frame)

        if time_now > end_time:
            print("stop")
            vout.release()
            sys.exit()



