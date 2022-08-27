from logging import raiseExceptions


from exception import InvalidTreeException


class Graph:
    def __init__(self, peaks, edges):
        self.peaks = peaks
        self.edges = edges

    def __str__(self):
        return f"peaks={self.peaks}\nedges={self.edges}"

class Tree(Graph):
    def __init__(self, peaks, edges):
        if len(peaks) != len(edges) - 1:
            raise InvalidTreeException("Not a valid tree")
        super().__init__(self, peaks, edges)