import sys
import os

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, project_root)
print(f"Project root added to Python path: {project_root}")

print("Python path:")
for path in sys.path:
    print(path)

from src.python.depth_simulation import DepthSimulator
from src.python.alert_system import AlertSystem
from object_detection import detect_objects
from src.python.visualization import visualize_depth_map_and_objects, visualize_depth_map_3d

import time
import numpy as np

def main():
    # Initialize components
    simulator = DepthSimulator(width=100, height=100, min_depth=0.5, max_depth=5.0)
    alert_system = AlertSystem(critical_distance=1.0)
    
    # Simulation parameters
    threshold = 2.0
    num_frames = 1  # For now, we'll just visualize one frame

    for frame in range(num_frames):
        # Simulate depth map
        depth_map = simulator.simulate()

        # Detect objects
        objects = detect_objects(depth_map.tolist(), threshold)

        # Check for alerts
        alerts = alert_system.check_for_obstacles(objects)

        # Print frame information
        print(f"\nFrame {frame + 1}/{num_frames}")
        print(f"Detected {len(objects)} objects")

        # Print alerts
        alert_system.print_alerts(alerts)

        # Visualize depth map and objects
        visualize_depth_map_and_objects(depth_map, objects, threshold)

        # Visualize 3D depth map
        visualize_depth_map_3d(depth_map)

    print("\nSimulation complete.")

if __name__ == "__main__":
    main()