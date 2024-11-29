# Minimum CMake version
cmake_minimum_required(VERSION 3.21)
set(CMAKE_ENABLED_LANGUAGES_COMPILER /usr/local/cuda/bin/nvcc)

project(MyEigenProject LANGUAGES CXX CUDA)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


# Enable compile_commands.json generation
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
# Specify the directory where you want compile_commands.json to be stored
set(CMAKE_COMPILE_COMMANDS_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/build")


# Ensure the custom directory exists
file(MAKE_DIRECTORY ${CMAKE_COMPILE_COMMANDS_OUTPUT_DIRECTORY})

option(BUILD_CPU_GEMM "Build CPU-based GEMM using Eigen" OFF)
option(BUILD_GPU_GEMM "Build GPU-based GEMM using CUTLASS" ON)

# set(GLOG_INCLUDE_DIR "${CMAKE_SOURCE_DIR}/submodules/glog")

# if(NOT EXISTS "${GLOG_INCLUDE_DIR}")
#     message(STATUS "Eigen not found in '${GLOG_INCLUDE_DIR}'. Fetching Eigen from Github...")
#     # Fetch Eigen
#     FetchContent_Declare(
#         glog
#         GIT_REPOSITORY https://github.com/google/glog.git
#         GIT_TAG master # Use 'main' or replace with a specific version like '3.4.0'
#     )
#     FetchContent_MakeAvailable(glog)
    
#     # Set EIGEN_DIR to the fetched content
#     set(GLOG ${glog_SOURCE_DIR})
# else()
#     message(STATUS "Using glog from '${glog_INCLUDE_DIR}'.")
# endif()
# # Google Test

# set(GTEST_INCLUDE_DIR "${CMAKE_SOURCE_DIR}/submodules/googletest")

# if(NOT EXISTS "${GTEST_INCLUDE_DIR}")
#     message(STATUS "Eigen not found in '${GTEST_INCLUDE_DIR}'. Fetching Eigen from Github...")
#     # Fetch Eigen
#     FetchContent_Declare(
#         googletest
#         GIT_REPOSITORY https://github.com/google/googletest.git
#         GIT_TAG master # Use 'main' or replace with a specific version like '3.4.0'
#     )
#     FetchContent_MakeAvailable(googletest)
    
#     # Set EIGEN_DIR to the fetched content
#     set(GTEST ${googletest_SOURCE_DIR})
# else()
#     message(STATUS "Using glog from '${googletest_INCLUDE_DIR}'.")
# endif()

# set(TARGET_LIST)

if (BUILD_GPU_GEMM)
    # Link CUDA libraries (optional if CUTLASS uses specific CUDA features)
    find_package(CUDA REQUIRED)
    # Set CUDA architecture (adjust for your GPU)
    set(CUTLASS_NVCC_ARCHS "89" CACHE STRING "Set GPU artitectures") # For Ampere GPUs; adjust as necessary
    set(CUTLASS_ENABLE_TESTS OFF CACHE BOOL "Disable CUTLASS tests")
    set(CUTLASS_ENABLE_EXAMPLES OFF CACHE BOOL "Disable CUTLASS examples")
    add_subdirectory(${CMAKE_SOURCE_DIR}/submodules/cutlass)
endif()
add_subdirectory(projects)

# # Get all targets in the project
# function(getAllSubdirs dir dirs)
#     # get subdirectories for dir
#     get_property(subdirs DIRECTORY ${dir} PROPERTY SUBDIRECTORIES)
#     # iterate any found subdirectories
#     foreach(subdir ${subdirs})
#         # append each sub directory
#         list(APPEND ${dirs} ${subdir})
#         getAllSubdirs(${subdir} ${dirs})
#     endforeach()
#     set(${dirs} ${${dirs}} PARENT_SCOPE)
# endfunction()

# set(Project_Directories ${CMAKE_SOURCE_DIR})
# getAllSubDirs(. Project_Directories)
# message("all targets " ${Project_Directories})
