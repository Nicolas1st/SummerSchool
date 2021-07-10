FROM alpine:latest
RUN apk add firefox
CMD ["/usr/bin/firefox"]
# X-server mount cmd:
#$ docker container run -e DISPLAY -v /tmp/.X11-unix:/tmp/X11-unix --net=host firefox
