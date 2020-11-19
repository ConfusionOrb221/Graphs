import random
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
        if(num_users < avg_friendships):
            return None
        # Add users
        for i in range(num_users):
            self.add_user(i)
        # Create friendships
        userlist = list(self.users.keys())
        for i in range(1, num_users):
            userlist.remove(i)
            random.shuffle(userlist)
            count = random.randint(0,avg_friendships * 2 - 1)
            if count == 0:
                userlist.append(i)
            else:
                for j in range(0, count):
                    if random.getrandbits(1):
                        self.add_friendship(i, userlist[j]) 
                userlist.append(i)
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        for i in range(1, self.last_id + 1):
            if i == user_id:
                visited[user_id] = i
            else:
                l = bfs(self.friendships, user_id, i)
                if l:
                    visited[i] = l
        return visited

def bfs(graph, starting_vertex, destination_vertex):
        explored = []

        queue = [[starting_vertex]]

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node not in explored:
                neighbors = graph[node]

                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

                    if neighbor == destination_vertex:
                        return new_path
                explored.append(node)


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
