# Minimum CMake version
cmake_minimum_required(VERSION 3.10)

# Option 2: Use find_package for system-installed Eigen (if available)
# Uncomment the following lines if you want to use a system-installed version of Eigen instead
# find_package(Eigen3 3.3 REQUIRED NO_MODULE)

# Specify your executable
add_executable(my_eigen_app main.cpp)

# Add Eigen include directories to the target
# Use EIGEN_INCLUDE_DIR for the local version or Eigen3::Eigen for system-installed
target_include_directories(my_eigen_app PRIVATE ${EIGEN_INCLUDE_DIR})
# Uncomment the line below if using find_package
# target_link_libraries(my_eigen_app PRIVATE Eigen3::Eigen)

add_custom_command(TARGET my_eigen_app POST_BUILD
                   COMMAND ${CMAKE_COMMAND} -E copy
                   ${CMAKE_BINARY_DIR}/compile_commands.json
                   ${CMAKE_COMPILE_COMMANDS_OUTPUT_DIRECTORY}/${EXECUTABLE_NAME}.json)