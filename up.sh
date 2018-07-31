#!/bin/bash
TESTING=""
CTN_NAME="justforfun"
CTN_IMAGE="justforfun_image"
# stop if running
$TESTING docker stop ${CTN_NAME} || true && ${TESTING} docker rm ${CTN_NAME} || true


#build image
$TESTING docker build -t ${CTN_IMAGE}:latest -f Dockerfile .



# spin up container

if [ "$1" = "detach" ]; then
	DETACH_FLAG="-d"
else
	DETACH_FLAG="-it"
fi

$TESTING docker run $DETACH_FLAG -v ${PWD}/files/:/files -p 8080:8080 -p 4443:4443 --name ${CTN_NAME} ${CTN_IMAGE}:latest

