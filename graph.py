from math import pow
from logging import raiseExceptions
from exception import InvalidTreeException, PeakNotFoundException


class Graph:
    def __init__(self, peaks, edges):
        self.peaks = peaks
        self.edges = edges

    def __str__(self):
        return f"G(X,E) = {{\n  X = {self.peaks}\n  E = {self.edges}\n}}"

    def deg(self, peak: str) -> int:
        """
        Get the given peak degree in the graph

        :return:
            The peak degree as an integer

        :raise:
            <b>PeakNotFoundException</b> when looking at a peak that's not present in the graph
        """
        deg = 0

        if peak not in self.peaks:
            raise PeakNotFoundException(f"Not peak {peak} present in the current graph")

        for e in self.edges:
            if e.__contains__(peak):
                deg += 1
        return deg

    def is_complete(self) -> bool:
        """
        Check if a graph is complete or not

        :return:
            <b>True</b>: Complete<br>
            <b>False</b>: Not complete<br>
        """
        edges = set()
        peaks_len = len(self.peaks)

        for e in self.edges:
            for p in self.peaks:
                if e.__contains__(p):
                    edges.add(e)
        return len(edges) == (peaks_len * (peaks_len - 1)) / 2

    def has_cycle(self) -> bool:
        """
        Check if the graph gets at least one cycle

        :return:
            <b>True</b>: There's a cycle
            <b>False</b>: There's no cycle
        """
        if len(self.peaks) < 3:
            return False
        return None

    def size(self):
        return len(self.peaks)

    def order(self):
        return len(self.edges)

class Tree(Graph):
    def __init__(self, peaks, edges):
        if len(peaks) - 1 != len(edges):
            raise InvalidTreeException("Not a valid tree. Please make sure |E| = |X|-1")
        super().__init__(peaks, edges)

    def is_complete(self):
        return False