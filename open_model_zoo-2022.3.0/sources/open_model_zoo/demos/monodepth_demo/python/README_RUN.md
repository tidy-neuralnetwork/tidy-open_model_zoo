# enter docker
```
xhost local:root
sudo docker stop tidy-open_model_zoo-2022.3.0
sudo docker start tidy-open_model_zoo-2022.3.0
sudo docker exec -it tidy-open_model_zoo-2022.3.0 /bin/bash

```

# download model
```
cd /root/open_model_zoo/sources/open_model_zoo/demos/monodepth_demo/python
omz_downloader --list models.lst

```


# connverter
```
cd /root/open_model_zoo/sources/open_model_zoo/demos/monodepth_demo/python
omz_converter --list models.lst

```

# download test_data
```
cd /root/open_model_zoo/sources/open_model_zoo/demos/monodepth_demo/python
mkdir -p test_data/videos
wget -P test_data/videos/ https://storage.openvinotoolkit.org/data/test_data/videos/classroom.mp4


cd /root/open_model_zoo/sources/open_model_zoo/demos/monodepth_demo/python
mkdir -p test_data/videos
wget -P test_data/videos/ https://storage.openvinotoolkit.org/data/test_data/videos/people-detection.mp4


mkdir -p test_data/images
wget -P test_data/images/ https://storage.openvinotoolkit.org/data/test_data/images/person_detection.png

```

# run
```
export NO_AT_BRIDGE=1
cd /root/open_model_zoo/sources/open_model_zoo/demos/monodepth_demo/python
python3 monodepth_demo.py \
-d CPU \
-i /root/open_model_zoo/sources/open_model_zoo/demos/monodepth_demo/python/test_data/images/person_detection.png \
-m /root/open_model_zoo/sources/open_model_zoo/demos/monodepth_demo/python/public/midasnet/FP32/midasnet.xml \
-o output


export NO_AT_BRIDGE=1
cd /root/open_model_zoo/sources/open_model_zoo/demos/monodepth_demo/python
python3 monodepth_demo.py \
-d CPU \
-i /root/open_model_zoo/sources/open_model_zoo/demos/monodepth_demo/python/test_data/videos/classroom.mp4 \
-m /root/open_model_zoo/sources/open_model_zoo/demos/monodepth_demo/python/public/midasnet/FP16/midasnet.xml


```