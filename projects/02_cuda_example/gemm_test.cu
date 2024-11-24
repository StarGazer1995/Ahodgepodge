#include <cutlass/cutlass.h>
#include <cutlass/gemm/device/gemm.h>
#include <iostream>
#include <vector>

// Check for CUDA errors
#define CHECK_CUDA(call)                                                              \
    {                                                                                 \
        cudaError_t err = call;                                                       \
        if (err != cudaSuccess) {                                                     \
            std::cerr << "CUDA error at " << __FILE__ << ":" << __LINE__ << " : "     \
                      << cudaGetErrorString(err) << std::endl;                        \
            exit(EXIT_FAILURE);                                                       \
        }                                                                             \
    }

int main() {
    using ElementType = float; // Data type for matrix elements
    using LayoutType = cutlass::layout::RowMajor; // Row-major matrix layout

    // GEMM parameters
    int M = 128; // Rows of A and C
    int N = 128; // Columns of B and C
    int K = 128; // Columns of A and rows of B

    // Host matrices
    std::vector<ElementType> host_A(M * K, 1.0f); // Initialize A with 1.0f
    std::vector<ElementType> host_B(K * N, 1.0f); // Initialize B with 1.0f
    std::vector<ElementType> host_C(M * N, 0.0f); // Initialize C with 0.0f

    // Device matrices
    ElementType *device_A, *device_B, *device_C;
    CHECK_CUDA(cudaMalloc(&device_A, M * K * sizeof(ElementType)));
    CHECK_CUDA(cudaMalloc(&device_B, K * N * sizeof(ElementType)));
    CHECK_CUDA(cudaMalloc(&device_C, M * N * sizeof(ElementType)));

    // Copy data from host to device
    CHECK_CUDA(cudaMemcpy(device_A, host_A.data(), M * K * sizeof(ElementType), cudaMemcpyHostToDevice));
    CHECK_CUDA(cudaMemcpy(device_B, host_B.data(), K * N * sizeof(ElementType), cudaMemcpyHostToDevice));

    // Define CUTLASS GEMM kernel
    using Gemm = cutlass::gemm::device::Gemm<
        ElementType, LayoutType, // Matrix A: element type and layout
        ElementType, LayoutType, // Matrix B: element type and layout
        ElementType, LayoutType, // Matrix C: element type and layout
        ElementType>;            // Accumulator type

    // Configure GEMM operation
    Gemm gemm_op;
    cutlass::gemm::GemmCoord problem_size(M, N, K);

    // Define arguments
    typename Gemm::Arguments args(
        problem_size,                 // Problem size (M, N, K)
        {device_A, K},                // Matrix A and leading dimension
        {device_B, N},                // Matrix B and leading dimension
        {device_C, N},                // Matrix C and leading dimension
        {device_C, N},                // Matrix D (output matrix) and leading dimension
        {1.0f, 0.0f}                  // Scalars alpha and beta
    );

    // Check if the kernel is supported
    cutlass::Status status = gemm_op.can_implement(args);
    if (status != cutlass::Status::kSuccess) {
        std::cerr << "GEMM operation is not supported." << std::endl;
        return -1;
    }

    // Launch the GEMM kernel
    status = gemm_op(args);
    if (status != cutlass::Status::kSuccess) {
        std::cerr << "GEMM operation failed." << std::endl;
        return -1;
    }

    // Copy result back to host
    CHECK_CUDA(cudaMemcpy(host_C.data(), device_C, M * N * sizeof(ElementType), cudaMemcpyDeviceToHost));

    // Verify the results
    bool correct = true;
    for (int i = 0; i < M * N; ++i) {
        if (host_C[i] != K) { // Each element should be K (since A and B were filled with 1.0)
            correct = false;
            break;
        }
    }

    if (correct) {
        std::cout << "GEMM operation completed successfully!" << std::endl;
    } else {
        std::cerr << "GEMM operation failed verification!" << std::endl;
    }

    // Free device memory
    CHECK_CUDA(cudaFree(device_A));
    CHECK_CUDA(cudaFree(device_B));
    CHECK_CUDA(cudaFree(device_C));

    return 0;
}
