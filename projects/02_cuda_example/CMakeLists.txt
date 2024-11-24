# Enable Clangd support by generating compile_commands.json
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Option 1: Include Cutlass as a local header-only dependency
set(CUTLASS_INCLUDE_DIR "${CMAKE_SOURCE_DIR}/submodules/cutlass")
# Set CUDA architecture (adjust for your GPU)
set(CMAKE_CUDA_ARCHITECTURES 80) # For Ampere GPUs; adjust as necessary

if(NOT EXISTS "${CUTLASS_INCLUDE_DIR}")
    message(STATUS "Cutlass not found in '${EIGEN_INCLUDE_DIR}'. Fetching Cutlass from github submodule...")
    # Fetch Cutlass
    FetchContent_Declare(
        cutlass
        GIT_REPOSITORY git@github.com:StarGazer1995/cutlass.git
        GIT_TAG main # Use 'main' or replace with a specific version like '3.4.0'
    )
    FetchContent_MakeAvailable(Cutlass)
    
    # Set EIGEN_DIR to the fetched content
    set(EIGEN_DIR ${eigen_SOURCE_DIR})
else()
    message(STATUS "Using Cutlass from '${EIGEN_INCLUDE_DIR}'.")
endif()

# Add the main executable
add_executable(cutlass_gemm_example gemm_test.cu)

# Link CUDA libraries (optional if CUTLASS uses specific CUDA features)
find_package(CUDA REQUIRED)
target_link_libraries(cutlass_gemm_example CUDA::cudart)