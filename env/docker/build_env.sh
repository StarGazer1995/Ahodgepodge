 #!/bin/bash
image_version=${1:-24.08-py3}
docker build --build-arg VERSION="${image_version}" -t gongzhao1995/pytorch:${image_version} . 
