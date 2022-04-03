# %% Graph class (NOT COMPLETED)
# this is adjacency list
class Graph:
    def __init__(self, V) -> None:
        # matrix
        # self.matrix = [None] * len(V)
        # for i in range(len(V)):
        #     self.matrix[i] = [None] * len(V)

        # array
        self.vertices = [None] * len(V)
        for i in range(len(V)):
            self.vertices[i] = Vertex(V[i])

    def bfs(self, source):
        """
        Function for BFS, starting from source
        INCOMPLETE -> UNRRUNABLE
        """
        return_bfs = []
        discovered = []  # this is a queue
        discovered.append(source)
        while len(discovered) > 0:
            # serve from queue
            # u = discovered.serve()
            u = discovered.pop(0)  # pop(0) same as serve
            u.visited = True  # means I have visited u
            return_bfs.append(u)
            for edge in u.edges:
                v = edge.v
                if v.discovered == False:
                    discovered.append(v)
                    v.discovered = True  # means I have discovered v, adding it to queue
        return return_bfs

    def bfs_distance(self, source):
        """
        Function for BFS, starting from source
        INCOMPLETE -> UNRRUNABLE
        """
        discovered = []  # this is a queue
        discovered.append(source)
        while len(discovered) > 0:
            # serve from queue
            # u = discovered.serve()
            u = discovered.pop(0)  # pop(0) same as serve
            u.visited = True  # means I have visited u
            for edge in u.edges:
                v = edge.v
                if v.discovered == False:
                    discovered.append(v)
                    v.discovered = True  # means I have discovered v, adding it to queue
                    # backtracking -> INCOMPLETE
                    v.distance = u.distance + 1
                    v.previous = u

    def dijkstra(self, source, destination):
        """
        Function for BFS, starting from source
        INCOMPLETE -> UNRRUNABLE
        """
        source.distance = 0
        discovered = MinHeap()  # this is a MinHeap
        discovered.append(source.distance, source)  # append(key, data)
        while len(discovered) > 0:
            # serve from queue
            # u = discovered.serve()
            u = discovered.serve()  # pop(0) same as serve
            u.visited = True  # means I have visited u -> distance finalized
            if u == destination:
                return
            # perform edge relaxation for all adjacent vertices
            for edge in u.edges:
                v = edge.v
                if v.discovered == False:  # means distance is still inf
                    discovered.append(v)
                    v.discovered = True  # means I have discovered v, adding it to queue
                    # backtracking -> INCOMPLETE
                    v.distance = u.distance + edge.w
                    v.previous = u
                    discovered.append(v.distance, v)
                # it is in heap, but not yet finalized
                else v.visited == False:
                    # if i find a shorter route, change it
                    if v.distance > u.distance + edge.w:
                        # update distance
                        v.distance = u.distance + edge.w
                        v.previous = u
                        # update heap
                        # TODO code it yourself
                        discovered.update(v, v.distance) # update vertex v in heap, w/ distance v.distance (smaller); perform upheap

    def dfs(self, source):
        """
        Function for DFS, starting from source
        INCOMPLETE -> UNRRUNABLE
        also possible with recursion (this inst recursion -> refer to slides)
        """
        return_dfs = []
        discovered = []  # this is a stack (LNFO)
        discovered.append(source)  # append = push
        while len(discovered) > 0:
            # serve from queue
            # u = discovered.serve()
            u = discovered.pop(0)  # pop(0) same as serve
            u.visited = True  # means I have visited u
            return_dfs.append(u)
            for edge in u.edges:
                v = edge.v
                if v.discovered == False:
                    discovered.append(v)
                    v.discovered = True  # means I have discovered v, adding it to queue
        return return_dfs

    def __str__(self) -> str:
        return_string = ""
        for vertex in self.vertices:
            return_string = return_string + "Vertex " + str(vertex) + "\n"
        return return_string


class Vertex:
    def __init__(self, id) -> None:
        self.id = id
        # list
        self.edges = []
        # for traversal
        self.discovered = False
        self.visited = False
        # distance
        self.distance = 0
        # backtracking / where i was from
        self.previous = None

    def added_to_queue(self):
        self.discovered = True

    def visit_node(self):
        self.visited = True

    def __str__(self) -> str:
        return_string = str(self.id)
        return return_string


class Edge:
    def __init__(self, u, v, w) -> None:
        self.u = u
        self.v = v
        self.w = w


# %%
if __name__ == "__main__":
    vertices = [0, 1, 2, 3, 4]
    my_graph = Graph(V=vertices)
    print(my_graph)
