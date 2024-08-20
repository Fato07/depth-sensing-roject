#include "object_detection.h"
#include <algorithm>
#include <cmath>

std::vector<std::tuple<int, int, float>> detect_objects(const std::vector<std::vector<float>>& depth_map, float threshold) {
    // Vector to store detected objects (x, y, depth)
    std::vector<std::tuple<int, int, float>> objects;
    
    // Get dimensions of the depth map
    int height = depth_map.size();
    int width = height > 0 ? depth_map[0].size() : 0;

    // Iterate through each pixel in the depth map
    for (int y = 0; y < height; ++y) {
        for (int x = 0; x < width; ++x) {
            // If depth is less than threshold, consider it an object
            if (depth_map[y][x] < threshold) {
                objects.emplace_back(x, y, depth_map[y][x]);
            }
        }
    }

    // Simple clustering to group nearby points
    std::vector<std::tuple<int, int, float>> clustered_objects;
    for (const auto& obj : objects) {
        bool added = false;
        // Check if the current object is close to any existing cluster
        for (auto& cluster : clustered_objects) {
            // Calculate Manhattan distance between object and cluster
            int dx = std::abs(std::get<0>(obj) - std::get<0>(cluster));
            int dy = std::abs(std::get<1>(obj) - std::get<1>(cluster));
            // If object is within clustering threshold, add to cluster
            if (dx <= 2 && dy <= 2) {  // Reduced clustering threshold
                // Update cluster depth to the minimum depth found
                std::get<2>(cluster) = std::min(std::get<2>(cluster), std::get<2>(obj));
                added = true;
                break;
            }
        }
        // If object wasn't added to any cluster, create a new cluster
        if (!added) {
            clustered_objects.push_back(obj);
        }
    }

    // Return the list of clustered objects
    return clustered_objects;
}