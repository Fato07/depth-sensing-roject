import numpy as np
from object_detection import detect_objects

def test_detect_objects():
    # Create a simple depth map
    depth_map = np.array([
        [1.0, 2.0, 3.0],
        [0.5, 1.5, 2.5],
        [3.0, 2.0, 1.0]
    ])

    # Convert to list of lists for C++ function
    depth_map_list = depth_map.tolist()

    # Detect objects
    objects = detect_objects(depth_map_list, 2.0)

    print(f"Detected {len(objects)} objects:")
    for obj in objects:
        print(f"Object at ({obj[0]}, {obj[1]}) with depth {obj[2]}")

if __name__ == "__main__":
    test_detect_objects()