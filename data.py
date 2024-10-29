import math


# Representation of a two-dimensional point.
class Point:
    # Initialize a new Point object.
    # input: x-coordinate as a float
    # input: y-coordinate as a float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


    # Provide a developer-friendly string representation of the object.
    # input: Point for which a string representation is desired. 
    # output: string representation
    def __repr__(self) -> str:
        return 'Point({}, {})'.format(self.x, self.y)


    # Compare the Point object with another value to determine equality.
    # input: Point against which to compare
    # input: Another value to compare to the Point
    # output: boolean indicating equality
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Point and
                math.isclose(self.x, other.x) and
                math.isclose(self.y, other.y))


# Representation of a duration as minutes and seconds.
class Duration:
    # Initialize a new Duration object.
    # input: minutes as an integer
    # input: seconds as an integer
    def __init__(self, minutes:int, seconds: int):
        self.minutes = minutes
        self.seconds = seconds

    def total_seconds(self) -> int:
        return self.minutes * 60 + self.seconds

    # Provide a developer-friendly string representation of the object.
    # input: Duration for which a string representation is desired. 
    # output: string representation
    def __repr__(self) -> str:
        return 'Duration({}, {})'.format(self.minutes, self.seconds)


    # Compare the Duration object with another value to determine equality.
    # input: Duration against which to compare
    # input: Another value to compare to the Duration
    # output: boolean indicating equality
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Duration and
                self.minutes == other.minutes and
                self.seconds == other.seconds)


# Representation of a song.
class Song:
    # Initialize a new Song object.
    # input: the song's artist as a string
    # input: the song's title as a string
    # input: the song's duration as a Duration object
    def __init__(self, artist: str, title: str, duration:Duration):
        self.artist = artist
        self.title = title
        self.duration = duration

    # Provide a developer-friendly string representation of the object.
    # input: Song for which a string representation is desired. 
    # output: string representation
    def __repr__(self):
        return "Song('{}', '{}', {})".format(self.artist, self.title,
            self.duration)


    # Compare the Song object with another value to determine equality.
    # input: Song against which to compare
    # input: Another value to compare to the Song
    # output: boolean indicating equality
    def __eq__(self, other):
        return (self is other or
                type(other) == Song and
                self.artist == other.artist and
                self.title == other.title and
                self.duration == other.duration)



# Representation of an axis-aligned rectangle.
class Rectangle:
    # Initialize a new Rectangle object.
    # input: top-left corner as a Point
    # input: bottom-right corner as a Point
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right


    # Provide a developer-friendly string representation of the object.
    # input: Rectangle for which a string representation is desired. 
    # output: string representation
    def __repr__(self) -> str:
        return 'Rectangle({}, {})'.format(self.top_left, self.bottom_right)


    # Compare the Rectangle object with another value to determine equality.
    # input: Rectangle against which to compare
    # input: Another value to compare to the Rectangle
    # output: boolean indicating equality
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Rectangle and
                self.top_left == other.top_left and
                self.bottom_right == other.bottom_right)
