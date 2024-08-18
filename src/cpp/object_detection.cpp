#include "object_detection.h"
#include <algorithm>
#include <cmath>

std::vector<std::tuple<int, int, float>> detect_objects(const std::vector<std::vector<float>>& depth_map, float threshold) {
    std::vector<std::tuple<int, int, float>> objects;
    int height = depth_map.size();
    int width = height > 0 ? depth_map[0].size() : 0;

    for (int y = 0; y < height; ++y) {
        for (int x = 0; x < width; ++x) {
            if (depth_map[y][x] < threshold) {
                objects.emplace_back(x, y, depth_map[y][x]);
            }
        }
    }

    // Simple clustering to group nearby points
    std::vector<std::tuple<int, int, float>> clustered_objects;
    for (const auto& obj : objects) {
        bool added = false;
        for (auto& cluster : clustered_objects) {
            int dx = std::abs(std::get<0>(obj) - std::get<0>(cluster));
            int dy = std::abs(std::get<1>(obj) - std::get<1>(cluster));
            if (dx <= 2 && dy <= 2) {  // Reduced clustering threshold
                std::get<2>(cluster) = std::min(std::get<2>(cluster), std::get<2>(obj));
                added = true;
                break;
            }
        }
        if (!added) {
            clustered_objects.push_back(obj);
        }
    }

    return clustered_objects;
}