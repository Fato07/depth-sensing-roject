#pragma once
#include <vector>
#include <tuple>

std::vector<std::tuple<int, int, float>> detect_objects(const std::vector<std::vector<float>>& depth_map, float threshold);