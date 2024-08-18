#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "object_detection.h"

// Namespace alias for convenience
namespace py = pybind11;

// Function to create Python bindings
PYBIND11_MODULE(object_detection, m) {
    m.doc() = "pybind11 example plugin for object detection";  // Optional module docstring

    // Binding the C++ function to be called from Python
    m.def("detect_objects", &detect_objects, "Detect objects in depth map",
          py::arg("depth_map"), py::arg("detection_range"));
}
