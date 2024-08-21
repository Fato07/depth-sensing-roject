# Depth Sensing Simulation

This project simulates a depth-sensing application using a combination of Python and C++. It generates a simulated depth map, detects objects within the map, and provides alerts for objects within a critical distance.

## Prerequisites

- Python 3.6+
- C++ compiler with C++11 support
- CMake 3.4+
- NumPy
- Matplotlib
- pybind11

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/Fato07/depth-sensing-simulation.git
   cd depth-sensing-simulation
   ```

2. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip3 install -r requirements.txt
   ```

4. Build the C++ extension:
   ```
   python3 setup.py build_ext --inplace
   ```

## Usage

Run the main script:
```
python3 src/python/main.py
```

This will simulate a depth map, detect objects, and print any alerts for objects within the critical distance.

## Running Tests

To run the tests:
```
pytest tests/
```

## Project Structure

- `src/python/`: Contains the Python source code
  - `depth_simulation.py`: Simulates the depth map
  - `alert_system.py`: Handles alerts for detected objects
  - `main.py`: Main script that ties everything together
- `src/cpp/`: Contains the C++ source code
  - `object_detection.cpp`: Implements the object detection algorithm
  - `object_detection.h`: Header file for the object detection function
  - `bindings.cpp`: pybind11 bindings to expose C++ function to Python
- `tests/`: Contains test cases
- `setup.py`: Build script for the C++ extension
- `CMakeLists.txt`: CMake configuration file
