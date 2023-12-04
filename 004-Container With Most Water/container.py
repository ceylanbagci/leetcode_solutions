def max_area(height):
    left_pointer, right_pointer = 0, len(height) - 1
    max_area = 0

    while left_pointer < right_pointer:
        # Calculate the current area
        h = min(height[left_pointer], height[right_pointer])
        w = right_pointer - left_pointer
        current_area = h * w

        # Update the maximum area
        max_area = max(max_area, current_area)

        # Move the pointers towards each other
        if height[left_pointer] < height[right_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1

    return max_area


# Time unefficient solution:

class Solution:
    def maxArea(self, height: List[int]) -> int:
        volume = 0
        for i in range(1, len(height)):
            for j in range(i-1, -1, -1):
                x, y = (i-j), min(height[i], height[j])
                if x*y >= volume:
                    volume = x*y
        return volume



