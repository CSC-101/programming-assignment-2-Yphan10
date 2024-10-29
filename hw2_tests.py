import data
import hw2
from data import Point, Rectangle, Duration, Song
import unittest


# Write your test cases for each part below.
class TestCases(unittest.TestCase):

    # Test for Part 1
    def test_create_rectangle(self):
        p1 = Point(2, 2) # Create a point at (2, 2)
        p2 = Point(10, 10) # Create a point at (10, 10)
        rectangle = hw2.create_rectangle(p1, p2) # Call the function to create a rectangle
        # Assertions to check the properties of the created rectangle
        self.assertEqual(rectangle.top_left.x, 2)
        self.assertEqual(rectangle.top_left.y, 10)
        self.assertEqual(rectangle.bottom_right.x, 10)
        self.assertEqual(rectangle.bottom_right.y, 2)

    # Test for Part 2
    def test_shorter_duration_than(self):
        d1 = Duration(3, 30)  # 3 minutes 30 seconds
        d2 = Duration(4, 0)   # 4 minutes
        self.assertTrue(hw2.shorter_duration_than(d1, d2)) # Check if d1 is shorter than d2
        self.assertFalse(hw2.shorter_duration_than(d2, d1)) # Check if d2 is not shorter than d1

    # Test for Part 3
    def setUp(self):
        #Set up test songs for use in multiple tests.
        self.song1 = Song("Artist1", "Song A", Duration(0, 180))  # 3:00
        self.song2 = Song("Artist2", "Song B", Duration(0, 270))  # 4:30
        self.song3 = Song("Artist3", "Song C", Duration(0, 135))  # 2:15
        self.songs = [self.song1, self.song2, self.song3]  # List of songs for testing

    def test_songs_shorter_than(self):
        """Test case where some songs are shorter than the max duration."""
        max_duration = Duration(0, 210)  # Set max duration to 3:30
        result = hw2.songs_shorter_than(self.songs, max_duration) # Call the function to filter songs
        self.assertEqual(result, [self.song1, self.song3])  # Expect Song A and Song C

    def test_no_songs_shorter_than(self):
        """Test case where no songs are shorter than the max duration."""
        max_duration = Duration(0, 120)  # 2:00
        result = hw2.songs_shorter_than(self.songs, max_duration) # Call the function to filter songs
        self.assertEqual(result, [])  # Expect an empty list

    # Test for Part 4
    def setUp(self):
        #Set up test songs for use in multiple tests.
        self.song1 = Song("Artist1", "Song A", Duration(0, 180))  # 3:00
        self.song2 = Song("Artist2", "Song B", Duration(0, 270))  # 4:30
        self.song3 = Song("Artist3", "Song C", Duration(0, 135))  # 2:15
        self.songs = [self.song1, self.song2, self.song3] # List of songs for testing

    def test_running_time_valid_indices(self):
        #Test case with valid song indices.
        playlist = [0, 2, 1, 0]  # Valid indices for the songs
        total_time = hw2.running_time(self.songs, playlist)
        self.assertEqual(total_time, Duration(12, 45))  # Update the expected duration to 12:45

    def test_running_time_ignore_invalid_indices(self):
        #Test case where some song indices are out of range.
        playlist = [0, 3, -1, 1]  # 3 is out of range, -1 is out of range
        total_time = hw2.running_time(self.songs, playlist) # Call the function to calculate total time
        self.assertEqual(total_time, Duration(11, 15))  # Update this too based on the valid songs

    # Test for Part 5
    def test_validate_route(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        valid_route = ['san luis obispo', 'santa margarita', 'atascadero'] # A valid route
        invalid_route = ['san luis obispo', 'atascadero'] # An invalid route
        self.assertTrue(hw2.validate_route(city_links, valid_route))
        self.assertFalse(hw2.validate_route(city_links, invalid_route))

    # Test for Part 6
    def test_example_case(self):
        self.assertEqual(hw2.longest_repetition([1, 1, 2, 2, 1, 1, 1, 3]), 4) # Expect 4 for the longest repetition of 1s

    def test_empty_list(self):
        self.assertIsNone(hw2.longest_repetition([])) #Empty Lists

    def test_no_repetition(self):
        self.assertIsNone(hw2.longest_repetition([1, 2, 3])) #No repetition

    def test_multiple_same_max_repetitions(self):
        self.assertEqual(hw2.longest_repetition([1, 1, 2, 2, 3, 3]), 0)  # First max repetition of 1s

    def test_single_element(self):
        self.assertEqual(hw2.longest_repetition([5]), None)  # Only one element, no repetition

    def test_long_repetition(self):
        self.assertEqual(hw2.longest_repetition([3, 3, 3, 2, 2, 2, 3]), 0)  # Three 3s at the start


if __name__ == '__main__':
    unittest.main()