from graph import Graph, Tree


def depthfirstsearch(tree):
    pass


if __name__ == '__main__':
    tree = Tree(
        {'a', 'b', 'c', 'd', 'e'},
        {'ab', 'bc', 'ad', 'ae'}
    )
    graph = Graph(
        {'a', 'b', 'c', 'd'},
        {'ab', 'bc', 'cb', 'ba', 'ac', 'bd'}
    )
    print(tree)
    print(f"deg(a) = {tree.deg('a')}")
    
    if graph.is_complete():
        print("Complete")
    else:
        print("Not complete")