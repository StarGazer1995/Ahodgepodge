#include <gtest/gtest.h>
#include <Eigen/Dense>


void cpu_gemm(const Eigen::MatrixXd& A, const Eigen::MatrixXd& B, Eigen::MatrixXd& C) {
    C.noalias() = A * B; // Perform matrix multiplication
}

// Test case for CPU GEMM
TEST(CpuGemmTest, MatrixMultiplication) {
    // Define input matrices
    Eigen::MatrixXd A(2, 3);
    A << 1, 2, 3,
         4, 5, 6;

    Eigen::MatrixXd B(3, 2);
    B << 7, 8,
         9, 10,
         11, 12;

    // Expected result
    Eigen::MatrixXd expected(2, 2);
    expected << 58, 64,
                139, 154;

    // Output matrix
    Eigen::MatrixXd C(2, 2);

    // Call the GEMM function
    cpu_gemm(A, B, C);

    // Check the result
    EXPECT_EQ(C.rows(), expected.rows());
    EXPECT_EQ(C.cols(), expected.cols());
    EXPECT_TRUE(C.isApprox(expected, 1e-9)) << "Matrix multiplication failed!";
}