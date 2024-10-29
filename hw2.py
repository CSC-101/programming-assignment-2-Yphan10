import data
from typing import List, Optional
from data import Point, Rectangle, Duration, Song

# Write your functions for each part in the space below.
# Part 1: create_rectangle
def create_rectangle(p1: Point, p2: Point) -> Rectangle:
# Creates a Rectangle object given two points.

    top_left_x = min(p1.x, p2.x)
    top_left_y = max(p1.y, p2.y)
    bottom_right_x = max(p1.x, p2.x)
    bottom_right_y = min(p1.y, p2.y)

    return Rectangle(Point(top_left_x, top_left_y), Point(bottom_right_x, bottom_right_y))


# Part 2: shorter_duration_than
def shorter_duration_than(d1: Duration, d2: Duration) -> bool:
# Compares two durations to determine if the first is shorter.

    total_seconds_d1 = d1.minutes * 60 + d1.seconds
    total_seconds_d2 = d2.minutes * 60 + d2.seconds

    return total_seconds_d1 < total_seconds_d2

# Part 3: songs_shorter_than
def songs_shorter_than(songs: list[Song], max_duration: Duration) -> list[Song]:
    #Returns a list of songs shorter than the given max_duration.

    return [song for song in songs if song.duration.total_seconds() < max_duration.total_seconds()]
# Part 4: running_time
def running_time(songs: list[Song], playlist: list[int]) -> Duration:
    #Calculates the total running time of the specified songs in the playlist.
    total_seconds = 0
    for index in playlist:
        if 0 <= index < len(songs):  # Check for valid song indices
            total_seconds += songs[index].duration.total_seconds()

    minutes, seconds = divmod(total_seconds, 60)  # Convert total seconds to minutes and seconds
    return Duration(minutes, seconds)  # Return as a Duration object


# Part 5: validate_route
def validate_route(city_links: list[list[str]], route: list[str]) -> bool:
    #Validates a travel route based on city links.

    if len(route) <= 1:  # Empty or single-city routes are valid
        return True

    for i in range(len(route) - 1):
        if not any(route[i] in link and route[i + 1] in link for link in city_links):
            return False

    return True


# Part 6: longest_repetition
def longest_repetition(nums: List[int]) -> Optional[int]:
   # Finds the index of the longest contiguous repetition of a single number in a list.

    if not nums:  # If the list is empty, return None
        return None

    max_index = 0  # To store the starting index of the longest repetition
    max_length = 1  # To store the length of the longest repetition
    current_length = 1  # Current length of repetition
    current_index = 0  # Current starting index of repetition

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:  # If current number is same as previous
            current_length += 1  # Increment the current repetition length
        else:
            # Check if the current repetition is the longest so far
            if current_length > max_length:
                max_length = current_length
                max_index = current_index
            # Reset for the next number
            current_length = 1
            current_index = i  # Update the starting index for the new number

    # Final check at the end of the loop
    if current_length > max_length:
        max_index = current_index

    # Return max_index only if max_length is greater than 1
    return max_index if max_length > 1 else None