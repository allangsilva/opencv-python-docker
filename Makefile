build: 
	docker build -t ovc-image .

run: 
	docker run -it -d --name ocv \
	-v $(PWD):/home/ \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	--net=host --ipc=host \
	--device=/dev/video0:/dev/video0 \
	--network="host" \
	-e DISPLAY=$(DISPLAY) \
	ovc-image 

in: 
	docker exec -it ocv bash

stop:
	docker rm -f ocv