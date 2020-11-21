
def earliest_ancestor(ancestors, starting_node):
    stack = []
    for i in range(len(ancestors)):
        if ancestors[i][1] == starting_node:
            if stack:
                if stack[0][0] > ancestors[i][0]:
                    stack.pop()
                    stack.append(ancestors[i])
            else:
                stack.append(ancestors[i])
    if len(stack) == 0:
        return -1
    while True:
        prev = stack[0]
        for i in range(len(ancestors)):
            if ancestors[i][1] == stack[0][0]:
                stack.pop()
                stack.append(ancestors[i])
        if stack[0] == prev:
            if stack[0][0] == starting_node:
                return -1
            return stack[0][0]



if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 1))
    print(earliest_ancestor(test_ancestors, 2))
    print(earliest_ancestor(test_ancestors, 3))
    print(earliest_ancestor(test_ancestors, 6))