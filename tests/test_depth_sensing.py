import pytest
import numpy as np
from src.python.depth_simulation import DepthSimulator
from src.python.alert_system import AlertSystem
from object_detection import detect_objects

def test_depth_simulator():
    simulator = DepthSimulator(width=100, height=100, min_depth=0.5, max_depth=5.0)
    depth_map = simulator.simulate()

    assert depth_map.shape == (100, 100)
    assert np.all(depth_map >= 0.5) and np.all(depth_map <= 5.0)

def test_object_detection():
    # Create a simple depth map with known objects
    depth_map = np.ones((10, 10)) * 5.0
    depth_map[2:5, 2:5] = 1.0  # Object at (2,2) to (4,4)
    depth_map[7, 7] = 0.5  # Single point object at (7,7)

    # Convert numpy array to list of lists
    depth_map_list = depth_map.tolist()

    objects = detect_objects(depth_map_list, 2.0)

    print(f"Detected objects: {objects}")  # Add this line for debugging

    assert len(objects) == 2, f"Expected 2 objects, but found {len(objects)}"
    
    # Check for the larger object
    large_object = next((obj for obj in objects if 2 <= obj[0] <= 4 and 2 <= obj[1] <= 4), None)
    assert large_object is not None, "Failed to detect the larger object"
    
    # Check for the single point object
    point_object = next((obj for obj in objects if obj[0] == 7 and obj[1] == 7), None)
    assert point_object is not None, "Failed to detect the single point object"

def test_alert_system():
    alert_system = AlertSystem(critical_distance=1.5)
    
    # Test case 1: No objects within critical distance
    objects = [(0, 0, 2.0), (1, 1, 3.0)]
    alerts = alert_system.check_for_obstacles(objects)
    assert len(alerts) == 0

    # Test case 2: One object within critical distance
    objects = [(0, 0, 2.0), (1, 1, 1.0)]
    alerts = alert_system.check_for_obstacles(objects)
    assert len(alerts) == 1
    assert "Warning: Object detected at (1, 1)" in alerts[0]

def test_end_to_end():
    simulator = DepthSimulator(width=50, height=50, min_depth=0.5, max_depth=5.0)
    alert_system = AlertSystem(critical_distance=1.5)

    depth_map = simulator.simulate()
    # Convert numpy array to list of lists
    depth_map_list = depth_map.tolist()

    objects = detect_objects(depth_map_list, 2.0)
    alerts = alert_system.check_for_obstacles(objects)

    assert isinstance(depth_map, np.ndarray)
    assert len(objects) >= 0
    assert isinstance(alerts, list)

if __name__ == "__main__":
    pytest.main()