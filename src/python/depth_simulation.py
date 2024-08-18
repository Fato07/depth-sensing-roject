import numpy as np

class DepthSimulator:
    def __init__(self, width, height, min_depth=0.5, max_depth=5.0):
        self.width = width
        self.height = height
        self.min_depth = min_depth
        self.max_depth = max_depth

    def generate_depth_map(self):
        """Generate a random depth map."""
        return np.random.uniform(self.min_depth, self.max_depth, (self.height, self.width))

    def add_objects(self, depth_map, num_objects=5):
        """Add random objects to the depth map."""
        for _ in range(num_objects):
            x = np.random.randint(0, self.width)
            y = np.random.randint(0, self.height)
            radius = np.random.randint(10, 50)
            depth = np.random.uniform(self.min_depth, self.max_depth)

            y_grid, x_grid = np.ogrid[-radius: radius, -radius: radius]
            mask = x_grid**2 + y_grid**2 <= radius**2

            y_indices, x_indices = np.where(mask)
            y_coords = y + y_indices - radius
            x_coords = x + x_indices - radius

            valid_coords = (y_coords >= 0) & (y_coords < self.height) & (x_coords >= 0) & (x_coords < self.width)
            depth_map[y_coords[valid_coords], x_coords[valid_coords]] = depth

        return depth_map

    def simulate(self):
        """Simulate a depth map with objects."""
        depth_map = self.generate_depth_map()
        return self.add_objects(depth_map)