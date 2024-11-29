# Add the main executable
set(src main.cpp)
set(dep Eigen3::Eigen glog::glog)
add_and_run_code(01_simple_example "${src}" "${dep}")