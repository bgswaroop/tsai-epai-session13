import numpy as np


class Polygon:
    def __init__(self, num_edges, circum_radius):
        """
        Instantiate a Polygon
        :param num_edges:
        :param circum_radius:
        """
        n = num_edges
        r = circum_radius

        self.circum_radius = r
        self.num_edges = n
        self.num_vertices = n
        self.interior_angle = (n - 2) * (180 / n)
        self.edge_length = 2 * r * np.sin(np.pi / n)
        self.apothem = r * np.cos(np.pi / n)
        self.area = 0.5 * n * self.edge_length * self.apothem
        self.perimeter = n * self.edge_length

    def __repr__(self):
        """
        Representation of a polygon
        :return: str
        """
        representation = [
            f'An object of the Polygon class',
            f'\t Num edges: {self.num_edges}',
            f'\t Num vertices: {self.num_vertices}',
            f'\t Interior angle: {self.interior_angle}',
            f'\t Edge length: {self.edge_length}',
            f'\t Apothem: {self.apothem}',
            f'\t Area: {self.area}',
            f'\t Perimeter: {self.perimeter}',
        ]
        return '\n'.join(representation)

    def __eq__(self, other):
        """
        Check for equality of two polygons
        :param other: Other Polygon
        :return: bool
        """
        if self.num_edges == other.num_edges and self.circum_radius == other.circum_radius:
            return True
        return False

    def __gt__(self, other):
        """
        Verify if the current polygon is greater than the other polygon
        :param other: another polygon
        :return: bool
        """
        if self.num_vertices > other.num_vertices:
            return True
        return False


if __name__ == '__main__':
    p1 = Polygon(5, 10)
    print(p1.__repr__())

    p2 = Polygon(5, 10)
    p3 = Polygon(5, 5)

    print(p1 == p2)
    print(p1 == p3)

    p4 = Polygon(10, 2)
    print(p1 > p4)
    print(p1 < p4)
