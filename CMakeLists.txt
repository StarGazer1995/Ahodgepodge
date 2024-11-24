# Minimum CMake version
cmake_minimum_required(VERSION 3.10)
project(MyEigenProject)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Enable compile_commands.json generation
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
# Specify the directory where you want compile_commands.json to be stored
set(CMAKE_COMPILE_COMMANDS_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/build")
message("${CMAKE_SOURCE_DIR}/build")
# Ensure the custom directory exists
file(MAKE_DIRECTORY ${CMAKE_COMPILE_COMMANDS_OUTPUT_DIRECTORY})

# Option 1: Include Eigen as a local header-only dependency
set(EIGEN_INCLUDE_DIR "${CMAKE_SOURCE_DIR}/submodules/eigen")

message("${EIGEN_INCLUDE_DIR}")

if(NOT EXISTS "${EIGEN_INCLUDE_DIR}/Eigen")
    message(STATUS "Eigen not found in '${EIGEN_INCLUDE_DIR}'. Fetching Eigen from GitLab...")
    # Fetch Eigen
    FetchContent_Declare(
        Eigen
        GIT_REPOSITORY https://gitlab.com/libeigen/eigen.git
        GIT_TAG main # Use 'main' or replace with a specific version like '3.4.0'
    )
    FetchContent_MakeAvailable(Eigen)
    
    # Set EIGEN_DIR to the fetched content
    set(EIGEN_DIR ${eigen_SOURCE_DIR})
else()
    message(STATUS "Using Eigen from '${EIGEN_INCLUDE_DIR}'.")
endif()


add_subdirectory(projects)