ARG VERSION
FROM nvcr.io/nvidia/tensorrt:${VERSION}

RUN apt update
RUN apt install apt-transport-https curl gnupg -y
COPY ./bazel-release.pub.gpg /bazel-release.pub.gpg
RUN cat /bazel-release.pub.gpg | gpg --dearmor >bazel-archive-keyring.gpg
RUN mv bazel-archive-keyring.gpg /usr/share/keyrings
RUN mkdir -p /etc/apt/sources.list.d/ && touch /etc/apt/sources.list.d/bazel.list
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/bazel-archive-keyring.gpg] https://storage.googleapis.com/bazel-apt stable jdk1.8"  > /etc/apt/sources.list.d/bazel.list
RUN apt update && apt install -y bazel
