# docker pull
```
sudo docker pull openvino/ubuntu20_dev:2022.3.0

```



# docker create

```
xhost local:root

sudo docker run -itd  \
--name tidy-open_model_zoo-2022.3.0 \
--user root \
--privileged \
--ipc=host \
-v /etc/localtime:/etc/localtime \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-e DISPLAY=$DISPLAY \
-v /data/home/tonye/tidy-neuralnetwork/tidy-open_model_zoo/open_model_zoo-2022.3.0:/root/open_model_zoo \
-w /root/open_model_zoo openvino/ubuntu20_dev:2022.3.0


```


# enter docker
```
xhost local:root
sudo docker stop tidy-open_model_zoo-2022.3.0
sudo docker start tidy-open_model_zoo-2022.3.0
sudo docker exec -it tidy-open_model_zoo-2022.3.0 /bin/bash

```

# install 
```
apt -y update
apt install -y iputils-ping
apt install -y inetutils-telnet
apt install -y wget vim
apt install -y ffmpeg


```

# Proxy Network
```
env |grep PROXY

export http_proxy=http://172.17.0.1:58591/
export https_proxy=http://172.17.0.1:58591/
export HTTPS_PROXY=http://172.17.0.1:58591/
export HTTP_PROXY=http://172.17.0.1:58591/


curl cip.cc

```






# docker commit
```
> dlstreamer:2022.2-release
sudo docker commit -a "tonye" -m "install 20200109" dec65d429bac 10.9.36.17:5000/tidy-paddlepaddle/face-recognition:1.0
sudo docker inspect 10.9.36.17:5000/tidy-paddlepaddle/face-recognition:1.0



```
