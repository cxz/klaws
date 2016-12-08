
# Why

Putting the kitchen sink on top of scipy-notebook :-) 

Initially I only needed xgboost + hyperopt on Jupyter following the best practices adopted in scipy-notebook. But then ended up getting stuff from Kaggle's image for opencv, tensorflow, etc.

I'm using this image to run batch jobs on AWS.

# How to upload to Docker Hub

- docker build -t kaggle-batch .
- (in case command above fails with "no space left on device" the reason is that "devicemapper" is currently limit by 10GB and the space is trying to use more than that. need to stop docker daemon, run docker daemon --storage-opt dm.basesize=30GB, and restart docker daemon)
- docker images
- docker tag <image_id> aamaia/kaggle-batch:latest
- docker login
- docker push aamaia/kaggle-batch

# How to use (pending)

- ... 

# Cheat Sheet

- docker images: shows all images.
- docker import: creates an image from a tarball.
- docker build: creates image from Dockerfile.
- docker commit: creates image from a container, pausing it temporarily if it is running.
- docker rmi: removes an image.
- docker load: loads an image from a tar archive as STDIN, including images and tags (as of 0.7).
- docker save: saves an image to a tar archive stream to STDOUT with all parent layers, tags & versions (as of 0.7).
- docker history: shows history of image.
- docker tag: tags an image to a name (local or registry).
- docker commit -m "commit message" -a "author" container_id username/imagename:tag
- docker pull image_name:tag