#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "object_detection.h"

// Create a namespace alias for pybind11 for convenience
namespace py = pybind11;

// Define the Python module
PYBIND11_MODULE(object_detection, m) {
    // Set the module's docstring
    m.doc() = "Object detection module";

    // Expose the C++ function 'detect_objects' to Python
    // This allows the function to be called from Python code
    m.def("detect_objects", &detect_objects, "Detect objects in depth map");
}