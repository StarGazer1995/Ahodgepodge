

# Add the main executable
add_executable(cutlass_gemm_example gemm_test.cu)
target_link_libraries(cutlass_gemm_example PRIVATE cutlass_library)

# target_include_directories(cutlass_gemm_example
#                             PRIVATE ${CUTLASS_INCLUDE_DIR}
#                             ${CUTLASS_EXAMPLES_UTILS_DIR})
# target_link_libraries(cutlass_gemm_example )