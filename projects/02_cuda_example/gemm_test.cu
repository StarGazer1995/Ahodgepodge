#include <cutlass/cutlass.h>
#include <cutlass/gemm/device/gemm.h>
#include <cutlass/util/host_tensor.h>
#include <cutlass/util/reference/host/tensor_compare.h>
#include <cutlass/util/reference/device/tensor_fill.h>
#include <cutlass/util/reference/host/gemm.h>
#include <iostream>
#include <vector>

using ElementType = float; // Data type for matrix elements
using LayoutType = cutlass::layout::RowMajor; // Row-major matrix layout
using Tensor = cutlass::HostTensor<ElementType, LayoutType>;

cudaError_t device_gemm(int M, int N, int K,
                        Tensor& A,
                        Tensor& B,
                        Tensor& C,
                        ElementType alpha, ElementType beta){
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
                                    {A.device_view(), K},                // Matrix A and leading dimension
                                    {B.device_view(), N},                // Matrix B and leading dimension
                                    {C.device_view(), N},                // Matrix C and leading dimension
                                    {C.device_view(), N},                // Matrix D (output matrix) and leading dimension
                                    {alpha, beta}                  // Scalars alpha and beta
        );
        cutlass::Status status = gemm_op.can_implement(args);
        if (status != cutlass::Status::kSuccess) {
            return cudaErrorUnknown;
        }
        status = gemm_op(args);
        if (status != cutlass::Status::kSuccess) {
            return cudaErrorUnknown;
        }
        
          return cudaSuccess;
    }

int main() {
    
    // GEMM parameters
    int M = 128; // Rows of A and C
    int N = 128; // Columns of B and C
    int K = 128; // Columns of A and rows of B
    ElementType alpha = 1.0f;
    ElementType beta = 0.0f;
    
    Tensor A{cutlass::MatrixCoord(M, K)};
    Tensor B{cutlass::MatrixCoord(K, N)};
    Tensor C{cutlass::MatrixCoord(M, N)};
    Tensor C_ref{cutlass::MatrixCoord(M, N)};

    cutlass::reference::device::TensorFillRandomGaussian(A.device_view(), 10, 0, 1, 0);
    cutlass::reference::device::TensorFillRandomGaussian(B.device_view(), 10, 0, 1, 0);
    cutlass::reference::device::TensorFillRandomGaussian(C.device_view(), 10, 0, 1, 0);

    auto resutl = device_gemm(M, N, K, A, B, C, alpha, beta);

    A.sync_host();
    B.sync_host();
    C.sync_host();

    cutlass::reference::host::Gemm<
    ElementType,                           // ElementA
    LayoutType,              // LayoutA
    ElementType,                           // ElementB
    LayoutType,              // LayoutB
    ElementType,                           // ElementOutput
    LayoutType,              // LayoutOutput
    ElementType,
    ElementType
  > gemm_ref;

  gemm_ref(
    {M, N, K},                          // problem size (type: cutlass::gemm::GemmCoord)
    alpha,                              // alpha        (type: cutlass::half_t)
    A.host_ref(),                       // A            (type: TensorRef<half_t, ColumnMajor>)
    B.host_ref(),                       // B            (type: TensorRef<half_t, ColumnMajor>)
    beta,                               // beta         (type: cutlass::half_t)
    C_ref.host_ref()              // C            (type: TensorRef<half_t, ColumnMajor>)
  );

  if (!cutlass::reference::host::TensorEquals(
    C_ref.host_view(), 
    C.host_view())) {

    char const *filename = "errors_01_cutlass_utilities.csv";

    std::cerr << "Error - CUTLASS GEMM kernel differs from reference. Wrote computed and reference results to '" << filename << "'" << std::endl;
  } else {
    std::cout<< " The program finished successfully" <<std::endl;
  }

    return 0;
}
