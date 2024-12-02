ARG VERSION
FROM nvcr.io/nvidia/pytorch:${VERSION}

RUN apt update
RUN apt install apt-transport-https curl gnupg -y
COPY ./bazel-release.pub.gpg /bazel-release.pub.gpg
RUN cat /bazel-release.pub.gpg | gpg --dearmor >bazel-archive-keyring.gpg
RUN mv bazel-archive-keyring.gpg /usr/share/keyrings
RUN mkdir -p /etc/apt/sources.list.d/ && touch /etc/apt/sources.list.d/bazel.list
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/bazel-archive-keyring.gpg] https://storage.googleapis.com/bazel-apt stable jdk1.8"  > /etc/apt/sources.list.d/bazel.list
RUN apt update && apt install -y bazel clangd-12
RUN update-alternatives --install /usr/bin/clangd clangd /usr/bin/clangd-12 100


# Install gtest
RUN apt update && apt install -y libgtest-dev
RUN cd /usr/src/gtest && cmake . && make && cp lib/*.a /usr/lib
 
# Install glog
RUN apt update && apt install -y libgoogle-glog-dev

# Install google benchmark
RUN apt update && apt install -y git cmake
RUN git clone https://github.com/google/benchmark.git /tmp/benchmark
RUN cd /tmp/benchmark && git clone https://github.com/google/googletest.git /tmp/benchmark/googletest
RUN cd /tmp/benchmark && cmake -DCMAKE_BUILD_TYPE=Release -DBENCHMARK_DOWNLOAD_DEPENDENCIES=ON && make && make install