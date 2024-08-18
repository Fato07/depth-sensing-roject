import matplotlib.pyplot as plt
import numpy as np

def visualize_depth_map_and_objects(depth_map, objects, threshold):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

    # Visualize depth map
    im1 = ax1.imshow(depth_map, cmap='viridis')
    ax1.set_title('Depth Map')
    fig.colorbar(im1, ax=ax1, label='Depth')

    # Visualize detected objects
    ax2.imshow(depth_map, cmap='viridis')
    ax2.set_title('Detected Objects')

    for obj in objects:
        x, y, depth = obj
        circle = plt.Circle((x, y), radius=3, color='red', fill=False)
        ax2.add_artist(circle)
        ax2.text(x, y, f'{depth:.2f}', color='white', fontsize=8, ha='center', va='center')

    # Draw threshold line
    threshold_map = np.full_like(depth_map, threshold)
    ax2.contour(threshold_map, levels=[threshold], colors=['yellow'], linestyles='dashed')

    plt.tight_layout()
    plt.show()

def visualize_depth_map_3d(depth_map):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    x = np.arange(0, depth_map.shape[1], 1)
    y = np.arange(0, depth_map.shape[0], 1)
    X, Y = np.meshgrid(x, y)

    surf = ax.plot_surface(X, Y, depth_map, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Depth')
    ax.set_title('3D Depth Map Visualization')

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()