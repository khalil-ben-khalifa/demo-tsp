from typing import List, Tuple
from math import sqrt
import csv

Vertex = Tuple[float, float]
Vertices = List[Vertex]


class Path:
    """Path on a plane

    Path is representing a path in a graph of points on a plane.
    """

    def __init__(self, vertices: Vertices = []):
        """Inits Path with vertices

        Args:
            vertices: list of vertices represented by tuples (float, float)
        """
        self._vertices = vertices

    def load(self, filepath: str):
        """Loads vertices from file

        Args:
            filepath: file path string
        """
        with open(filepath) as tsv:
            reader = csv.reader(tsv, delimiter=' ')
            self._vertices = [(float(x), float(y)) for x, y in reader]

    def get_vertices(self) -> Vertices:
        """Returns vertices list"""
        return self._vertices

    def get_cycle_length(self) -> float:
        """Returns cycle length

        Calculates length of cycle created by connecting first and last vertex
        from the vertices.
        """
        if len(self._vertices) < 2:
            return 0
        return sum([Path._distance(self._vertices[i], self._vertices[i + 1])
                    for i in range(len(self._vertices) - 1)])\
            + Path._distance(self._vertices[-1], self._vertices[0])

    def _distance(v0: Vertex, v1: Vertex) -> float:
        """Calculates euclidean distance between points

        Args:
            v0 : Vertex representing first point.
            v1 : Vertex representing second point.

        Returns:
            Euclidean distance between points.
        """
        return sqrt((v1[0] - v0[0])**2 + (v1[1] - v0[1])**2)