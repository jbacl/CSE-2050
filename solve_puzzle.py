def move_options(len, iterator, step):
    if iterator + step in range(len):
        clockwise = iterator + step
    else:
        clockwise = step - (len - iterator)
    if iterator - step > -1:
        counterclockwise = iterator - step
    else:
        counterclockwise = len - (step - iterator)
    return(clockwise, counterclockwise)

def solve_puzzle(L, current_index=0, visited=None): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""
    if visited == None:
        visited = set()
        visited.add(0)
    # 1) Base case: have you found a valid solution?
    if len(L) - 1 == current_index:
        return True

    # 2) Find all valid next-steps
    clockwise = move_options(len(L), current_index, L[current_index])[0]
    counterclockwise = move_options(len(L), current_index, L[current_index])[1]
    if clockwise not in visited:
        visited.add(clockwise)
        if solve_puzzle(L, clockwise, visited) == True:
            return True
        else:
            solve_puzzle(L, clockwise, visited)
    if counterclockwise not in visited:
        visited.add(counterclockwise)
        if solve_puzzle(L, counterclockwise, visited) == True:
            return True
        else:
            solve_puzzle(L, counterclockwise, visited)
    # 3) Return True if any valid solution is found
    return False

