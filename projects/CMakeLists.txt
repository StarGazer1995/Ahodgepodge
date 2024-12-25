
if(BUILD_CPU_GEMM)
    message(STATUS "BUILD CPU BASED GEMM")
    add_subdirectory(01_simple_example)
endif()

if(BUILD_GPU_GEMM)
    message(STATUS "BUILD GPU BASED GEMM")
    add_subdirectory(02_cuda_example)
endif()

if (BUILD_LLAMA)
    add_subdirectory(04_llama_example)
endif()