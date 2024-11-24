
if(BUILD_CPU_GEMM)
    add_subdirectory(01_simple_example)
endif()

if(BUILD_GPU_GEMM)
    add_subdirectory(02_cuda_example)
endif()