import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.users[vertex_id]

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # enqueue a path to the starting node instead of the starting node
        visited = set()
        q = Queue()
        q.enqueue([starting_vertex])

        while q.size() > 0:
            current_node = q.dequeue()
            v = current_node[-1] #last one
            if v not in visited:
                visited.add(v)
                for neighbor in self.friendships[v]:
                    next_v = current_node + [neighbor]
                    if neighbor == destination_vertex:
                        return next_v #includes neighbor
                    #if not
                    q.enqueue(next_v)

    def dft(self, starting_vertex, visited=set()):
       if starting_vertex not in visited:
            print (starting_vertex)

            visited.add(starting_vertex)

            neighbors = self.get_neighbors(starting_vertex)
            print(neighbors.users)
            if len(neighbors) == 0:
                return 
            
            else:
                for neighbor in neighbors:
                    self.dft_recursive(neighbor, visited)


    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
        total_friendships = avg_friendships * num_users

        friendship_combos = []

        for user_id in range(1, num_users + 1):
            for friend_id in range(user_id + 1, num_users + 1):
                friendship_combos.append((user_id, friend_id))
        
        self.fisher_yates_shuffle(friendship_combos)

        friendships_to_make = friendship_combos[:(total_friendships // 2)]

        for friendship in friendships_to_make:
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
    
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME        
       

        #DFT first creating dictionary item for each
        for item in self.dft(user_id):
            visited[item] = []

        #then BFS to find shortest path to each

        for item in self.friendships[user_id]:
            #get each user in item's network
            for extended in self.friendships[item]:
                #find shortest path between extended and user_id
                visited[extended].append(self.bfs(user_id, extended))

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
