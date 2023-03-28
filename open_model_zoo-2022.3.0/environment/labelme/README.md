
# docker pull create on HOST
```

sudo docker pull 10.9.36.17:5000/library/labelme:latest

> ubuntu 

sudo docker run \
--name tidy-open_model_zoo-2022.3.0_labelme \
-p 4945:80 \
-v /data/home/tonye/tidy-neuralnetwork/tidy-open_model_zoo/open_model_zoo-2022.3.0/datasets/labelme/Images:/var/www/html/LabelMeAnnotationTool/Images \
-v /data/home/tonye/tidy-neuralnetwork/tidy-open_model_zoo/open_model_zoo-2022.3.0/datasets/labelme/Annotations:/var/www/html/LabelMeAnnotationTool/Annotations \
-d \
--entrypoint "/bin/bash" \
-t 10.9.36.17:5000/library/labelme:latest



```

# start labelme

```

sudo docker start tidy-open_model_zoo-2022.3.0_labelme
sudo docker exec -it tidy-open_model_zoo-2022.3.0_labelme /bin/bash
service apache2 restart
chown -R www-data:www-data /var/www/html/LabelMeAnnotationTool/Annotations
chown -R www-data:www-data /var/www/html/LabelMeAnnotationTool/Images
chmod -R 777 /var/www/html/LabelMeAnnotationTool/Annotations
chmod -R 777 /var/www/html/LabelMeAnnotationTool/Images


## sample url
http://localhost:4945/LabelMeAnnotationTool/tool.html?mode=f&folder=tmp&image=person_detection&actions=a&objects=roi

```

