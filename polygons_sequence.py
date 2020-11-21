from polygon import Polygon


class PolygonSequence(object):
    def __init__(self, max_verties, circum_radius):
        """
        Initialize the polynomial sequence
        :param max_verties: int
        :param circum_radius: float
        """
        self.max_vertices = max_verties
        self.circum_radius = circum_radius
        self.sequence = [Polygon(num_edges, self.circum_radius) for num_edges in range(3, self.max_vertices + 1)]

    def max_efficiency_polygon(self):
        """
        determine the polynomial with maximum efficiency
        :return: Polynomial
        """
        max_efficient_poly = max(self.sequence, key=lambda p: p.area / p.perimeter)
        return max_efficient_poly

    def __getitem__(self, item):
        """
        Implementing getitem to make this Class a sequence
        :param item: index for the sequence
        :return: the polynomial element
        """
        if -(self.max_vertices - 2) <= item <= self.max_vertices - 3:
            return self.sequence[item]
        else:
            raise ValueError(f'Invalid item index. Allowed item value must be in the range: '
                             f'[0, {self.max_vertices - 3}], but item = {item}')

    def __len__(self):
        """
        Determine the length of the sequence
        :return: int
        """
        return self.max_vertices - 2

    def __repr__(self):
        """
        Formatted representation of the poly sequence
        :return: str
        """
        representation = [
            f'A sequence of element of Polygon class',
            f'\t Num elements: {self.__len__()}',
            f'\t Radius: {self.circum_radius}',
        ]
        return '\n'.join(representation)
