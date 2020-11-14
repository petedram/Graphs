from graph import Graph


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
    #Build Graph
    my_graph = Graph()
    for node in ancestors:
        my_graph.add_vertex(node[0]) #Add parent nodes
        my_graph.add_vertex(node[1]) #Add child nodes
        #need to check if already exists? No dups.

    for node in ancestors:
        my_graph.add_edge(node[1],node[0]) #create connections, ensure correct direction

    
    print(my_graph.vertices)

    #Traverse DFT
    depth = my_graph.dft(starting_node)
    print(f'depth {depth}')
    # Last item is the furthest away
    furthest = list(depth)[-1]
    
    print('furthest',furthest)

    #why returning visited sorted? instead of when visited?
        #order of visit: 6,5,4,3,2,1,10
        #returns: 1,2,3,4,5,6,10
        #because it's a set which orders!
    #Changed from set to list.


    #how to know when multiple furthest at equal depth?
        #use BFS to return the depth between, where equal, return lowest item.
            #warning bfs to self gives a higher depth!?! - added condition to check.
    
    #determine if more than one possible longest route:
        #loop over array backwards, adding value and depth until depth decreses, then retun based on logic
    max_depth = len(my_graph.bfs(starting_node, furthest))
    possible_max = set()
    for item in reversed(depth):
        if starting_node == item:
            print("can't BFS on self in DAG!")
        else:
            item_depth = len(my_graph.bfs(starting_node, item))
            print(f'item:{item} has a depth of:{item_depth}')
            if item_depth < max_depth:
                print('item depth is < max depth, no need to continue')
                break
            else:
                possible_max.add(item)

    print(f'there are {len(possible_max)} possible max!')
    if len(possible_max) == 0:
        return -1 #no parents
    else:
        lowest_id = min(possible_max)
        print('result to return is:', lowest_id)
        return lowest_id


# earliest_ancestor(ancestors, 2)