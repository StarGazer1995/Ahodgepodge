# Minimum CMake version
cmake_minimum_required(VERSION 3.21)

project(MyEigenProject LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
# Enable compile_commands.json generation
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
# Specify the directory where you want compile_commands.json to be stored
set(CMAKE_COMPILE_COMMANDS_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/build")

file(GLOB cmake_files "${CMAKE_SOURCE_DIR}/env/cmakes/*.cmake")
foreach(cmake_file ${cmake_files})
    include(${cmake_file})
endforeach()

# Ensure the custom directory exists
file(MAKE_DIRECTORY ${CMAKE_COMPILE_COMMANDS_OUTPUT_DIRECTORY})

option(BUILD_TESTS "Enable GTests" OFF)
option(BUILD_CPU_GEMM "Build CPU-based GEMM using Eigen" ON)
option(BUILD_GPU_GEMM "Build GPU-based GEMM using CUTLASS" OFF)

add_subdirectory(${CMAKE_SOURCE_DIR}/submodules/glog)
# add_subdirectory(${CMAKE_SOURCE_DIR}/submodules/googletest)

if (BUILD_TESTS)
    add_subdirectory(${CMAKE_SOURCE_DIR}/submodules/googletest)
    enable_testing()
endif()
        
if (BUILD_GPU_GEMM)
    enable_language(CUDA)
    set(CMAKE_ENABLED_LANGUAGES_COMPILER /usr/local/cuda/bin/nvcc)
    # Link CUDA libraries (optional if CUTLASS uses specific CUDA features)
    find_package(CUDA REQUIRED)
    # Set CUDA architecture (adjust for your GPU)
    set(CUTLASS_NVCC_ARCHS "89" CACHE STRING "Set GPU artitectures") # For Ampere GPUs; adjust as necessary
    set(CUTLASS_ENABLE_TESTS OFF CACHE BOOL "Disable CUTLASS tests")
    set(CUTLASS_ENABLE_EXAMPLES OFF CACHE BOOL "Disable CUTLASS examples")
    add_subdirectory(${CMAKE_SOURCE_DIR}/submodules/cutlass)
endif()

if (BUILD_CPU_GEMM)
    set(EIGEN_INCLUDE_DIR "${CMAKE_SOURCE_DIR}/submodules/eigen")
    add_subdirectory(${EIGEN_INCLUDE_DIR})
    message(STATUS "Using Eigen from ${EIGEN_INCLUDE_DIR}.")
endif()

add_subdirectory(projects)

# set(Project_Directories ${CMAKE_SOURCE_DIR}/projects)
# getAllSubDirs(${CMAKE_SOURCE_DIR} Project_Directories)
# message("all targets " ${Project_Directories})
