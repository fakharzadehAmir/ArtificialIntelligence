from Algorithm import Algorithm


class BFS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def run_algorithm(self, snake):
        def bfs(queueNode, finalState, _snake):
            while len(queueNode) > 0:
                # FIFO
                leftmost_node = queueNode.pop(0)  # reduce length of deque (First out)
                self.explored_set.append(leftmost_node)
                for neighbor in self.get_neighbors(leftmost_node):
                    if self.inside_body(_snake, neighbor) or self.outside_boundary(neighbor):
                        self.explored_set.append(neighbor)
                        continue
                    # BFS part of the game
                    # check child after breadth
                    if neighbor not in queueNode and neighbor not in self.explored_set:
                        neighbor.parent = leftmost_node
                        queueNode.append(neighbor)  # neighbors will add at the end of the dequeNode
                        self.explored_set.append(neighbor)
                        # check if neighbor is our final state or not
                        if neighbor.x == finalState.x and neighbor.y == finalState.y:
                            return self.get_path(neighbor)

        first_state, final_state = self.get_initstate_and_goalstate(snake)
        self.path, self.explored_set = [], []
        return bfs([first_state], final_state, snake)



