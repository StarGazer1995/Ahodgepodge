git submodule update
mkdir -p ./build
pushd build
    cmake ${@} ..
popd
