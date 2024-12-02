# Add the main executable
set(src gemm_test.cu)
set(dep cutlass_library)
add_and_run_code(02_cuda_example "${src}" "${dep}")