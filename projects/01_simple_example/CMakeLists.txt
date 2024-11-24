# Option 1: Include Eigen as a local header-only dependency
set(EIGEN_INCLUDE_DIR "${CMAKE_SOURCE_DIR}/submodules/eigen")

if(NOT EXISTS "${EIGEN_INCLUDE_DIR}/Eigen")
    message(STATUS "Eigen not found in '${EIGEN_INCLUDE_DIR}'. Fetching Eigen from GitLab...")
    # Fetch Eigen
    FetchContent_Declare(
        Eigen
        GIT_REPOSITORY https://gitlab.com/libeigen/eigen.git
        GIT_TAG main # Use 'main' or replace with a specific version like '3.4.0'
    )
    FetchContent_MakeAvailable(Eigen)
    
    # Set EIGEN_DIR to the fetched content
    set(EIGEN_DIR ${eigen_SOURCE_DIR})
else()
    message(STATUS "Using Eigen from '${EIGEN_INCLUDE_DIR}'.")
endif()

# Option 2: Use find_package for system-installed Eigen (if available)
# Uncomment the following lines if you want to use a system-installed version of Eigen instead
# find_package(Eigen3 3.3 REQUIRED NO_MODULE)

# Specify your executable
add_executable(my_eigen_app main.cpp)

# Add Eigen include directories to the target
# Use EIGEN_INCLUDE_DIR for the local version or Eigen3::Eigen for system-installed
target_include_directories(my_eigen_app PRIVATE ${EIGEN_INCLUDE_DIR})
# Uncomment the line below if using find_package
# target_link_libraries(my_eigen_app PRIVATE Eigen3::Eigen)

list(APPEND TARGET_LIST my_eigen_app)