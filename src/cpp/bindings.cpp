#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "object_detection.h"

namespace py = pybind11;

PYBIND11_MODULE(object_detection, m) {
    m.doc() = "Object detection module";
    m.def("detect_objects", &detect_objects, "Detect objects in depth map");
}