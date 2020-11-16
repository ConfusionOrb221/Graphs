"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy  
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.count = 0

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.count += 1
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        to_visit = Queue()
        visited = set()
        to_visit.enqueue(starting_vertex)
        visited.add(starting_vertex)
        while to_visit.size() > 0:
            current_vert = to_visit.dequeue()
            print(current_vert)
            for next_vert in self.get_neighbors(current_vert):
                if next_vert not in visited:
                    visited.add(next_vert)
                    to_visit.enqueue(next_vert)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = [False for i in range(self.count + 1)]  
  
        stack = [] 
  
        stack.append(starting_vertex)  
  
        while (len(stack)):  

            s = stack[-1]  
            stack.pop() 
  
            if (not visited[s]):  
                print(s) 
                visited[s] = True 

            for node in self.vertices[s]:  
                if (not visited[node]):  
                    stack.append(node)  
        

    def dft_recursive(self, starting_vertex, visited = []):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print(starting_vertex)
        visited.append(starting_vertex)
        for next_vert in self.get_neighbors(starting_vertex):
            if next_vert not in visited:
                self.dft_recursive(next_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        explored = []

        queue = [[starting_vertex]]

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node not in explored:
                neighbors = self.vertices[node]

                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

                    if neighbor == destination_vertex:
                        print(*new_path)
                        return new_path
                explored.append(node)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = [(starting_vertex, [starting_vertex])]
        visited = set()
        while stack:
            (vertex, path) = stack.pop()
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for neighbor in self.vertices[vertex]:
                    stack.append((neighbor, path + [neighbor]))

    def dfs_recursive(self, starting_vertex, destination_vertex, explored = set(), path_so_far = ""):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        #This is a cool little cheap trick i use a str because its not stored in memory the same way a list
        #would be so im able to not have to instatiate a new spot in memory for each list recursion and have the
        #path so far be stored in one str variable.
        explored.add(starting_vertex)
        if starting_vertex == destination_vertex: 
            result = path_so_far + str(starting_vertex)
            return [int(x) for x in result] 
        for w in self.vertices[starting_vertex]:
            if w not in explored:
                p = self.dfs_recursive(w, destination_vertex, explored, path_so_far + str(starting_vertex))
                if p: 
                    return p
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
