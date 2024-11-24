CONTAINER_HOSTNAME=$(whoami)_$(date "+%Y%m%d_%H%M%S")
TEST_MODE=${1:-false}
DOCKER_IMAGE=gongzhao1995/tensorrt/
TAG=${2:-23.08-py3}

if [ ${TEST_MODE} = false ]; then
    docker run \
        --shm-size 30g \
        --gpus=all \
        -e USER=$(whoami) \
        -e TERM=xterm-256color \
        -u $(id -u):$(id -g) \
        -v /etc/shadow:/etc/shadow \
        -v /etc/passwd:/etc/passwd \
        --group-add sudo \
        --name=${CONTAINER_HOSTNAME}\
        --hostname=$(hostname) \
        -v /home:/home \
        --workdir  ${HOME} \
        -it ${DOCKER_IMAGE}:${TAG} /bin/bash
else
    docker run \
        --rm \
        --shm-size 30g \
        --gpus=all \
        -e USER=$(whoami) \
        -e TERM=xterm-256color \
        -u $(id -u):$(id -g) \
        -v /etc/shadow:/etc/shadow \
        -v /etc/passwd:/etc/passwd \
        --group-add sudo \
        --name=${CONTAINER_HOSTNAME}\
        --hostname=$(hostname) \
        -v /home:/home \
        --workdir  ${HOME} \
        -it ${DOCKER_IMAGE}:${TAG} /bin/bash
fi
