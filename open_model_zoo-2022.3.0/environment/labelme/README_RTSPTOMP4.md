# run 

```

export dir=/data/home/baseuser/zto-workspace/tidy-deepstream/tidy-deepstream-6.1/environment/labelme
export exec_py_name=RtspToMp4

export rtsp_uri=rtsp://admin:ly123456@10.62.90.20:554/Streaming/Channels/3101
export camera_code=10.62.90.20_3101

export center_id=laiyang
export position_code=jingang
export start_time=20220830150000
export end_time=20220830170000
export out_path=/data/home/baseuser/zto-workspace/tidy-deepstream/tidy-deepstream-6.1/datasets/sample-videos/mp4/${center_id}_${position_code}_${camera_code}

mkdir -p ${out_path}


nohup python3 -u ${dir}/${exec_py_name}.py  \
--rtsp_uri ${rtsp_uri} \
--out_path ${out_path} \
--center_id ${center_id} \
--position_code ${position_code} \
--camera_code ${camera_code} \
--start_time ${start_time} \
--end_time ${end_time} > ${out_path}/nohup_${exec_py_name}_${position_code}_${camera_code}.log  2>&1 &




```