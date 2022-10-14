from Algorithm import Algorithm


class DFS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def run_algorithm(self, snake):
        # har bar ke run_DFS ejra mishe parent node neighbor ke head baadi hast barabare heade alane

        # *elate shekastegi ha dar bazi az masir ha tabee inside_body mibashad
        #   ke ture mishe choon badane mar dar code taghir nemikone
        # **elate inke ta ghable inke be goal state berese az masir haye sabegh ham ubur nemikonad explored set mibashad
        # ***ba khordan mive ham badan e mar update mishavad ham explored data ha va baghie sefr mishavad
        #   va ham len(path) dobare sefr mishe ta dafeye baad
        def dfs(head, finalState, _snake):
            if head.x == finalState.x and head.y == finalState.y:
                return self.get_path(head)
            if head in self.explored_set:
                return
            self.explored_set.append(head)
            ###########
            # DFS part of game
            for neighbor in self.get_neighbors(head):
                if neighbor not in self.explored_set and not(self.inside_body(_snake, neighbor)) \
                        and not(self.outside_boundary(neighbor)):
                    neighbor.parent = head
                    new_path_dfs = dfs(neighbor, finalState, _snake)
            #############
                    if new_path_dfs is not None:
                        return new_path_dfs
            return

        ####################
        # This part shows head's path(green position after pressing Space)
        if len(self.path) != 0:
            new_path = self.path.pop()  # poping from path step by step untill head == final_state
            if self.inside_body(snake, new_path):
                self.path = []
            else:
                return new_path
        ######################
        first_state, final_state = self.get_initstate_and_goalstate(snake)
        self.path, self.explored_set = [], []
        return dfs(first_state, final_state, snake)
