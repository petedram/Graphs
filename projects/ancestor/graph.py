"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}


    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v2 not in self.vertices:
            print(f"No such node!!, can't add {v2}")
        else:
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
        #make queue
        q = Queue()
        
        #make a set to track which nodes we have visited
        visited = set()

        #enqueue the starting node
        q.enqueue(starting_vertex)
        
        #loop while the queue isn't empty
        while q.size() > 0:
        #dq, this is out current node
            current_node = q.dequeue()

        
        #check if we've been here
            if current_node not in visited:
                print(current_node)
        ##if not we go to the node
        ###mark it as visited (add to visited set)
                visited.add(current_node)

        ###get the neighbors 
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()

        visited = []
        s.push(starting_vertex)

        while s.size() > 0:
            current_node = s.pop()

            if current_node not in visited:
                print(current_node)
                visited.append(current_node)

                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    s.push(neighbor)
        
        print(f'visited {visited}')
        
        return visited


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #nest function within a function
        def vertex_check(starting_vertex, node_set):
            #base case
            if starting_vertex in node_set:
                return
            print(starting_vertex)
            
            #sub-set of original problem
            for neighbor in self.vertices[starting_vertex]:
                node_set.add(starting_vertex)
                vertex_check(neighbor, node_set)
        
        vertex_check(starting_vertex, set())


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # enqueue a path to the starting node instead of the starting node
        visited = []
        q = Queue()
        q.enqueue([starting_vertex])

        while q.size() > 0:
            current_node = q.dequeue()
            v = current_node[-1] #last one
            # print(current_node, v)
            if v not in visited:
                visited.append(v)
                for neighbor in self.vertices[v]:
                    next_v = current_node + [neighbor]
                    if neighbor == destination_vertex:
                        return next_v #includes neighbor
                    #if not
                    q.enqueue(next_v)
        
        return visited


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        s = Stack()
        s.push([starting_vertex])

        while s.size() > 0:
            current_node = s.pop()
            v = current_node[-1] #last one
            print(current_node, v)
            if v not in visited:
                visited.add(v)
                for neighbor in self.vertices[v]:
                    next_v = current_node + [neighbor]
                    if neighbor == destination_vertex:
                        return next_v #includes neighbor
                    #if not
                    s.push(next_v)


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        def vertex_check(starting_vertex, node_set, destination_vertex):
            #base case
            node_set.add(starting_vertex)
            print(starting_vertex, destination_vertex)
            if starting_vertex == destination_vertex:
                return node_set
            
            #sub-set of original problem
            v = node_set[-1] #last one
            for neighbor in self.vertices[v]:
                next_v = starting_vertex + [neighbor]
                vertex_check(next_v, node_set, destination_vertex)
        
        vertex_check(starting_vertex, set(), destination_vertex)



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
