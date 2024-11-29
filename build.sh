mkdir -p ./build
pushd build
    cmake ${@} ..
    make -j16
popd
