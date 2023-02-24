# docker pull
```
sudo docker pull nvcr.io/nvidia/pytorch:22.12-py3

```



# docker create

```
xhost local:root

sudo docker run -itd  \
--name tidy-karpathy-nanoGPT \
--user root \
--privileged \
-p 9808:6000 \
-v /etc/localtime:/etc/localtime \
--ipc=host \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-e DISPLAY=$DISPLAY \
-v /data/home/tonye/tidy-neuralnetwork/tidy-karpathy/nanoGPT:/root/nanoGPT \
-w /root/nanoGPT nvcr.io/nvidia/pytorch:22.12-py3


```


# enter docker
```
xhost local:root
sudo docker stop tidy-karpathy-nanoGPT
sudo docker start tidy-karpathy-nanoGPT
sudo docker exec -it tidy-karpathy-nanoGPT /bin/bash

```

# install jupyter
```
pip3 install jupyter -i https://pypi.tuna.tsinghua.edu.cn/simple
cd /root/nanoGPT
nohup jupyter notebook --ip=0.0.0.0 --allow-root --port 6000 &


http://localhost:9808/tree

```

# install lib
```
pip3 install nanoGPT
pip3 install graphviz

apt update
apt install -y graphviz 

```


# docker commit
```
> dlstreamer:2022.2-release
sudo docker commit -a "tonye" -m "install 20200109" dec65d429bac 10.9.36.17:5000/tidy-paddlepaddle/face-recognition:1.0
sudo docker inspect 10.9.36.17:5000/tidy-paddlepaddle/face-recognition:1.0



```
