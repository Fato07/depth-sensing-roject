from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "object_detection",
        ["src/cpp/object_detection.cpp", "src/cpp/bindings.cpp"],
        include_dirs=["src/cpp"],
    ),
]

setup(
    name="depth_sensing_simulation",
    version="0.0.1",
    author="Fathin Dosunmu",
    author_email="Fathindos.fd@gmail.com",
    description="A depth sensing simulation with object detection",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=['numpy', 'pybind11'],
)