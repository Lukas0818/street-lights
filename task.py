ROAD_SEGMENT_LENGTH = 20
MAX_DISTANCE = 100

def calculate_illumination(distance: float) -> float:
    return 3 ** -((distance / MAX_DISTANCE) ** 2)

def find_index_of_darkest_street_light(road_length: int, not_working_street_lights: list[int]) -> tuple[int, int]:
    if not not_working_street_lights:
        return None, 0

    working_set = set(range(road_length // ROAD_SEGMENT_LENGTH + 1)) - set(not_working_street_lights)
    darkest_light_index = None
    darkest_light_illumination = 1.0
    bulbs_to_replace = 0

    for light_index in not_working_street_lights:
        left_working_light = next((x for x in range(light_index - 1, -1, -1) if x in working_set), None)
        right_working_light = next((x for x in range(light_index + 1, road_length // ROAD_SEGMENT_LENGTH + 1) if x in working_set), None)

        if left_working_light is not None and right_working_light is not None:
            distance_to_left_light = abs(light_index * ROAD_SEGMENT_LENGTH - left_working_light * ROAD_SEGMENT_LENGTH)
            distance_to_right_light = abs(right_working_light * ROAD_SEGMENT_LENGTH - light_index * ROAD_SEGMENT_LENGTH)
            distance_to_nearest_working = min(distance_to_left_light, distance_to_right_light) * ROAD_SEGMENT_LENGTH
        else:
            distance_to_nearest_working = road_length

        illumination = calculate_illumination(distance_to_nearest_working)

        if illumination < darkest_light_illumination:
            darkest_light_illumination = illumination
            darkest_light_index = light_index

    if darkest_light_index is not None:
        bulbs_to_replace = 1

    return darkest_light_index, bulbs_to_replace

def run_tests():
    test_cases = [
        (200, [4, 5, 6], 5, 1),
        (500, [15, 16, 17], 16, 1),
        (300, [10, 20, 30], 10, 1),
        (20, [0, 1], 0, 1),
        (1200, [21, 99, 100], 99, 1),
        (0, [], None, 0),
    ]

    for idx, (road_length, not_working_street_lights, expected_darkest_light, expected_bulbs_to_replace) in enumerate(test_cases):
        darkest_light, bulbs_to_replace = find_index_of_darkest_street_light(road_length, not_working_street_lights)
        assert darkest_light == expected_darkest_light, f"Test case {idx+1} failed. Expected darkest light: {expected_darkest_light}, but got {darkest_light}."
        assert bulbs_to_replace == expected_bulbs_to_replace, f"Test case {idx+1} failed. Expected bulbs to replace: {expected_bulbs_to_replace}, but got {bulbs_to_replace}."

    print("ALL TESTS PASSED")

if __name__ == "__main__":
    run_tests()
