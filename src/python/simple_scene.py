import numpy as np
import matplotlib.pyplot as plt
from depth_simulation import DepthSimulator

def create_simple_room_with_box(simulator):
    """A simple room with a box in the center."""
    depth_map = np.full((simulator.height, simulator.width), simulator.max_depth)

    # Add walls
    wall_depth = simulator.min_depth + 0.5
    wall_thickness = 5
    depth_map[:wall_thickness, :] = wall_depth  # Top wall
    depth_map[-wall_thickness:, :] = wall_depth  # Bottom wall
    depth_map[:, :wall_thickness] = wall_depth  # Left wall
    depth_map[:, -wall_thickness:] = wall_depth  # Right wall

    # Add a box in the center
    box_size = min(simulator.width, simulator.height) // 4
    box_depth = (simulator.min_depth + simulator.max_depth) / 2
    center_x, center_y = simulator.width // 2, simulator.height // 2
    box_start_x = center_x - box_size // 2
    box_start_y = center_y - box_size // 2
    depth_map[box_start_y:box_start_y+box_size, 
              box_start_x:box_start_x+box_size] = box_depth

    return depth_map

def visualize_depth_map(depth_map):
    plt.figure(figsize=(10, 8))
    plt.imshow(depth_map, cmap='viridis')
    plt.colorbar(label='Depth')
    plt.title('Depth Map of a Simple Room with a Box')
    plt.xlabel('Width')
    plt.ylabel('Height')
    plt.show()

# Create a simulator instance
simulator = DepthSimulator(width=100, height=100, min_depth=0.5, max_depth=5.0, seed=42)

# Create the simple room with a box
simple_depth_map = create_simple_room_with_box(simulator)

# Visualize the depth map
visualize_depth_map(simple_depth_map)

# For comparison, also visualize a regular simulated depth map
regular_depth_map = simulator.simulate()
visualize_depth_map(regular_depth_map)