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
omz_downloader --list models.lst -o /root/open_model_zoo/models

```


# connverter
```
cd /root/open_model_zoo/sources/open_model_zoo/demos/monodepth_demo/python
omz_converter --list models.lst -d /root/open_model_zoo/models -o /root/open_model_zoo/models

```

# download test_data
```
cd /root/open_model_zoo/datasets
mkdir -p test_data/videos
wget -P test_data/videos/ https://storage.openvinotoolkit.org/data/test_data/videos/classroom.mp4


cd /root/open_model_zoo/datasets
mkdir -p test_data/videos
wget -P test_data/videos/ https://storage.openvinotoolkit.org/data/test_data/videos/people-detection.mp4


cd /root/open_model_zoo/datasets
mkdir -p test_data/images
wget -P test_data/images https://storage.openvinotoolkit.org/data/test_data/images/person_detection.png

```

# run
```

cd /root/open_model_zoo/sources/open_model_zoo/demos/monodepth_demo/python
python3 monodepth_demo.py \
-d CPU \
-i /root/open_model_zoo/datasets/test_data/images/test_object1.jpg \
-m /root/open_model_zoo/models/public/midasnet/FP16/midasnet.xml \
--output_resolution 640x360 \
-o /root/open_model_zoo/datasets/test_data/images/test_object1_out.jpg



cd /root/open_model_zoo/sources/open_model_zoo/demos/monodepth_demo/python
python3 monodepth_demo.py \
-d GPU \
-i /root/open_model_zoo/datasets/test_data/images/test_object1.jpg \
-m /root/open_model_zoo/models/public/midasnet/FP16/midasnet.xml \
--output_resolution 640x360 \
-o /root/open_model_zoo/datasets/test_data/images/test_object1_out.jpg




```

