import heapq


class PuzzleState:
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent
        self.cost = 0 if parent is None else parent.cost + 1
        self.heuristic = 0

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))


def get_next_states(state):
    next_states = []
    i = state.board.index(0)
    if i >= 3:
        next_board = list(state.board)
        next_board[i], next_board[i - 3] = next_board[i - 3], next_board[i]
        next_states.append(PuzzleState(next_board, state))
    if i < 6:
        next_board = list(state.board)
        next_board[i], next_board[i + 3] = next_board[i + 3], next_board[i]
        next_states.append(PuzzleState(next_board, state))
    if i % 3 > 0:
        next_board = list(state.board)
        next_board[i], next_board[i - 1] = next_board[i - 1], next_board[i]
        next_states.append(PuzzleState(next_board, state))
    if i % 3 < 2:
        next_board = list(state.board)
        next_board[i], next_board[i + 1] = next_board[i + 1], next_board[i]
        next_states.append(PuzzleState(next_board, state))
    return next_states


def a_star(start_state, goal_state):
    open_list = [start_state]
    closed_list = set()

    while open_list:
        current_state = heapq.heappop(open_list)
        if current_state == goal_state:
            path = []
            while current_state is not None:
                path.append(current_state.board)
                current_state = current_state.parent
            return path[::-1]

        closed_list.add(current_state)
        next_states = get_next_states(current_state)
        for next_state in next_states:
            if next_state in closed_list:
                continue
            if next_state not in open_list:
                next_state.heuristic = heuristic(next_state.board, goal_state.board)
                heapq.heappush(open_list, next_state)
            else:
                index = open_list.index(next_state)
                if (next_state.cost + next_state.heuristic) < (open_list[index].cost + open_list[index].heuristic):
                    open_list[index] = next_state

    return None


def heuristic(board1, board2):
    distance = 0
    for i in range(9):
        row1, col1 = i // 3, i % 3
        row2, col2 = board2.index(board1[i]) // 3, board2.index(board1[i]) % 3
        distance += abs(row1 - row2) + abs(col1 - col2)
    return distance


start_state = PuzzleState([1, 5, 2, 0, 4, 3, 7, 6, 8])
goal_state = PuzzleState([1, 2, 3, 4, 5, 6, 7, 8, 0])
path = a_star(start_state, goal_state)

if path is not None:
    for board in path:
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print("\n")