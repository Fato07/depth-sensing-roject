cmake_minimum_required(VERSION 3.12)
project(ObjectDetection)

set(CMAKE_CXX_STANDARD 14)

add_subdirectory(extern/pybind11)
include_directories(extern/pybind11/include)

# Find the Python interpreter and include directories
find_package(Python3 REQUIRED COMPONENTS Development)

# Include Python headers
include_directories(${Python3_INCLUDE_DIRS})

# Include the src directory
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/src)

# Create the Python module
pybind11_add_module(object_detection src/object_detection.cpp src/object_detection_bindings.cpp)

# Link against the Python libraries
target_link_libraries(object_detection PRIVATE ${Python3_LIBRARIES})