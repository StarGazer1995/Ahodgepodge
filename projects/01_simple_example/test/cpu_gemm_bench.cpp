#include <benchmark/benchmark.h>
#include <Eigen/Dense>
#include <random>

// Function to initialize an Eigen matrix with random values
template <typename MatrixType>
MatrixType createRandomMatrix(int rows, int cols) {
    MatrixType mat(rows, cols);
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0.0, 1.0);

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            mat(i, j) = dis(gen);
        }
    }
    return mat;
}

// Benchmark for Eigen GEMM
static void BM_EigenGEMM(benchmark::State& state) {
    // Matrix dimensions (from the state object)
    const int size = state.range(0);
    Eigen::MatrixXd A = createRandomMatrix<Eigen::MatrixXd>(size, size);
    Eigen::MatrixXd B = createRandomMatrix<Eigen::MatrixXd>(size, size);
    Eigen::MatrixXd C(size, size);

    for (auto _ : state) {
        // Perform GEMM (C = A * B)
        C.noalias() = A * B;
        benchmark::DoNotOptimize(C);
    }

    // Optional: report the number of floating-point operations (FLOPs)
    state.counters["FLOPs"] = benchmark::Counter(
        2.0 * size * size * size, benchmark::Counter::kIsIterationInvariantRate);
}

// Register the benchmark with matrix size ranges
BENCHMARK(BM_EigenGEMM)->RangeMultiplier(2)->Range(128, 1024);

// Main function to run benchmarks
BENCHMARK_MAIN();
