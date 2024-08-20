import numpy as np

class DepthSimulator:
    def __init__(self, width, height, min_depth=0.5, max_depth=5.0, seed=None):
        # Initialize the simulator with dimensions and depth range
        self.width = width
        self.height = height
        self.min_depth = min_depth
        self.max_depth = max_depth
        
        # Create a numpy random number generator
        self.rng = np.random.default_rng(seed)

    def generate_depth_map(self):
        """Generate a random depth map."""
        # Create a 2D array of random depth values within the specified range
        return self.rng.uniform(self.min_depth, self.max_depth, (self.height, self.width))

    def add_objects(self, depth_map, num_objects=5):
        """Add random objects to the depth map."""
        for _ in range(num_objects):
            # Randomly choose object location
            x = self.rng.integers(0, self.width)
            y = self.rng.integers(0, self.height)
            # Randomly choose object size and depth
            radius = self.rng.integers(10, 51)
            depth = self.rng.uniform(self.min_depth, self.max_depth)

            # Create a circular mask for the object
            y_grid, x_grid = np.ogrid[-radius: radius, -radius: radius]
            mask = x_grid**2 + y_grid**2 <= radius**2

            # Find coordinates of the circular mask
            y_indices, x_indices = np.where(mask)
            # Adjust coordinates to center the object at (x, y)
            y_coords = y + y_indices - radius
            x_coords = x + x_indices - radius

            # Ensure coordinates are within the depth map bounds
            valid_coords = (y_coords >= 0) & (y_coords < self.height) & (x_coords >= 0) & (x_coords < self.width)
            # Set the depth values for the object
            depth_map[y_coords[valid_coords], x_coords[valid_coords]] = depth

        return depth_map

    def simulate(self):
        """Simulate a depth map with objects."""
        # Generate a base depth map and add objects to it
        depth_map = self.generate_depth_map()
        return self.add_objects(depth_map)