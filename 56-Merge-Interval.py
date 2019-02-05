# Mehod 1 linear scan
# Time:  O(nlogn)
# Space: O(1) or O(n) as no overlaps
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
#
class Interval:
    def __init__(self, s=0, e=0):
         self.start = s
         self.end = e
    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)
class Solution1:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged

if __name__ == "__main__":
    print (Solution1().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15,18)]))
    print (Solution1().merge([Interval(1, 4), Interval(0, 4)]))

# Mehod 2 Connected Components
# Time:  O(n^2)
# Space: O(n^2) all overlaps
#

#
"""
class Solution2:
    def overlap(self, a, b):
        return a.start <= b.end and b.start <= a.end

    # generate graph where there is an undirected edge between intervals u
    # and v iff u and v overlap.
    def build_graph(self, intervals):
        graph = collections.defaultdict(list)

        for i, interval_i in enumerate(intervals):
            for j in range(i+1, len(intervals)):
                if self.overlap(interval_i, intervals[j]):
                    graph[interval_i].append(intervals[j])
                    graph[intervals[j]].append(interval_i)

        return graph

    # merges all of the nodes in this connected component into one interval.
    def merge_nodes(self, nodes):
        min_start = min(node.start for node in nodes)
        max_end = max(node.end for node in nodes)
        return Interval(min_start, max_end)

    # gets the connected components of the interval overlap graph.
    def get_components(self, graph, intervals):
        visited = set()
        comp_number = 0
        nodes_in_comp = collections.defaultdict(list)

        def mark_component_dfs(start):
            stack = [start]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node])

        # mark all nodes in the same connected component with the same integer.
        for interval in intervals:
            if interval not in visited:
                mark_component_dfs(interval)
                comp_number += 1

        return nodes_in_comp, comp_number

    def merge(self, intervals):
        graph = self.build_graph(intervals)
        nodes_in_comp, number_of_comps = self.get_components(graph, intervals)

        # all intervals in each connected component must be merged.
        return [self.merge_nodes(nodes_in_comp[comp]) for comp in range(number_of_comps)]
if __name__ == "__main__":
    print (Solution2().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15,18)]))
    print (Solution2().merge([Interval(1, 4), Interval(0, 4)]))
"""