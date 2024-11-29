#include <Eigen/Dense>
#include <iostream>
#include <glog/logging.h>

int main() {
    google::InitGoogleLogging(__FILE__);
    // Define the dimensions
    const int rowsA = 3, colsA = 2;
    const int rowsB = 2, colsB = 3;

    // Check if dimensions match for matrix multiplication (colsA == rowsB)
    if (colsA != rowsB) {
        LOG(FATAL) << "Matrix dimensions do not match for multiplication!";
        return -1;
    }

    // Initialize matrices A and B
    Eigen::MatrixXd A(rowsA, colsA);
    Eigen::MatrixXd B(rowsB, colsB);

    // Fill matrices with values (you can replace this with your data)
    A << 1, 2,
         3, 4,
         5, 6;
    B << 7, 8, 9,
         10, 11, 12;

    // Perform GEMM operation: C = A * B
    Eigen::MatrixXd C = A * B;

    // Print matrices and result
    std::cout << "Matrix A:\n" << A << std::endl;
    std::cout << "Matrix B:\n" << B << std::endl;
    std::cout << "Matrix C (A * B):\n" << C << std::endl;

    return 0;
}
