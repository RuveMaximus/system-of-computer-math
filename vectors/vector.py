class Vector:
    def __init__(self, points: list) -> None:
        self.points = points
    
    def __str__(self):
        return str(self.points)

    def __add__(self, other: "Vector") -> "Vector":
        if len(self.points) != len(other.points):
            raise ValueError("The dimensions of the given vectors do not match")

        for i in range(len(self.points)):
            self.points[i] += other.points[i]
        return self

    def __sub__(self, other) -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other: "Vector") -> "Vector": 
        return Vector(self.x * other.x, self.y * other.y)

    def __mul__(self, k: int) -> "Vector":
        return Vector(self.x * k, self.y * k)
    