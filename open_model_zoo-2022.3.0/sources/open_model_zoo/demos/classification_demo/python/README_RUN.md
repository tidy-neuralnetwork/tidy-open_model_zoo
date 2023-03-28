# enter docker
```
xhost local:root
sudo docker stop tidy-open_model_zoo-2022.3.0
sudo docker start tidy-open_model_zoo-2022.3.0
sudo docker exec -it tidy-open_model_zoo-2022.3.0 /bin/bash

```

# download model
```
cd /root/open_model_zoo/sources/open_model_zoo/demos/classification_demo/python
omz_downloader --list models.lst -o /root/open_model_zoo/models

```


# connverter
```
cd /root/open_model_zoo/sources/open_model_zoo/demos/classification_demo/python
omz_converter --list models.lst -d /root/open_model_zoo/models -o /root/open_model_zoo/models

```

# download test_data
```
cd /root/open_model_zoo/datasets
mkdir -p test_data/images
wget -P test_data/images/ https://storage.openvinotoolkit.org/data/test_data/images/person_detection.png


```

# run
```
cd /root/open_model_zoo/sources/open_model_zoo/demos/classification_demo/python
python3 classification_demo.py \
-d CPU \
-m /root/open_model_zoo/models/public/efficientnet-b0-pytorch/FP16/efficientnet-b0-pytorch.xml \
-i /dev/video0 \
--labels /root/open_model_zoo/sources/open_model_zoo/data/dataset_classes/imagenet_2012.txt


cd /root/open_model_zoo/sources/open_model_zoo/demos/classification_demo/python
python3 classification_demo.py \
-d GPU \
-m /root/open_model_zoo/models/public/efficientnet-b0-pytorch/FP16/efficientnet-b0-pytorch.xml \
-i /dev/video0 \
--labels /root/open_model_zoo/sources/open_model_zoo/data/dataset_classes/imagenet_2012.txt



```

