project_name=${1:-01_simple_example}
pushd build
cmake --build . --target run_${project_name}
popd