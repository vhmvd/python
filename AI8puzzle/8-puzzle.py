"""
Ahmed Nadeem
2018047
"""

import math
import random
from typing import List

def pretty_print(list_to_print) -> None:
    """Prints in pretty format

    Args:
        list_to_print (list)
    """
    for index, item in enumerate(list_to_print, start=1):
        print(item, end=' ')
        if not index % 3:
            print()
    print()

class hill_climbing_8_puzzle:
    def __init__(self):
        """Constructor
        """
        self.front = []
        self.goal_node = ['1', '2', '3', '8', ' ', '4', '7', '6', '5']
        self.start_node = ['5', '4', ' ', '6', '7', '8', '1', '3', '2']
        self.previous_node = []
        self.pre_node = []
        self.pre_count = 1

    def solver(self) -> None:
        self.move_generator()
        pretty_print(self.start_node)
        self.child(self.start_node)
        next_node = self.get_next_node()
        pretty_print(next_node)
        count = 1
        while next_node != self.goal_node:
            print("Iteration:", count)
            count += 1
            self.child(next_node)
            if count > 1000:
                print("Please re-run")
                exit()
            next_node = self.get_next_node()
            pretty_print(next_node)
        print('\nResult\n')
        pretty_print(next_node)

    def move_generator(self) -> None:
        """Generates moves
        """
        while True:
            node = self.start_node
            neighbor_node = []
            direct = random.randint(1, 4)
            empty_location = node.index(' ')+1
            neighbor_node.extend(node)
            boundary = self.boundaries(empty_location)

            # Down
            if empty_location+3 <= 9 and direct == 1:
                temp = neighbor_node[node.index(' ')]
                neighbor_node[node.index(' ')] = neighbor_node[node.index(' ')+3]
                neighbor_node[node.index(' ')+3] = temp
                self.start_node = neighbor_node
                return

            # Up
            elif empty_location-3 >= 1 and direct == 2:
                temp = neighbor_node[node.index(' ')]
                neighbor_node[node.index(' ')] = neighbor_node[node.index(' ')-3]
                neighbor_node[node.index(' ')-3] = temp
                self.start_node = neighbor_node
                return

            # Left
            elif empty_location-1 >= boundary[0] and direct == 3:
                temp = neighbor_node[node.index(' ')]
                neighbor_node[node.index(' ')] = neighbor_node[node.index(' ')-1]
                neighbor_node[node.index(' ')-1] = temp
                self.start_node = neighbor_node
                return

            # Right
            elif empty_location+1 <= boundary[1] and direct == 4:
                temp = neighbor_node[node.index(' ')]
                neighbor_node[node.index(' ')] = neighbor_node[node.index(' ')+1]
                neighbor_node[node.index(' ')+1] = temp
                self.start_node = neighbor_node
                return

    def boundaries(self, location) -> list:
        lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        low = 0
        up = 0
        for i in lst:
            if location in i:
                low = i[0]
                up = i[2]
        return [low, up]

    def get_next_node(self) -> list:
        next_node = []
        temp_node = []
        while True:
            cost = 100000
            for i in self.front:
                if(i[-1] < cost):
                    cost = i[-1]
                    next_node = i[0:-1]
                    temp_node = i

            if temp_node in self.previous_node and temp_node in self.front:
                self.front.remove(temp_node)
                self.previous_node.append(temp_node)

            else:
                self.previous_node.append(temp_node)
                return next_node


    def heuristic(self, node) -> list:
        misplaced_values = 0
        distance = 0

        for i in range(9):
            if node[i] != self.goal_node[i]:
                misplaced_values += 1
        for i in node:
            distance += math.fabs(node.index(i)-self.goal_node.index(i))

        total_heuristic = distance+misplaced_values
        node.append(total_heuristic)
        return node

    def child(self, node=[]) -> list:
        subNode = []
        getZeroLocation = node.index(' ')+1
        subNode.extend(node)
        boundary = self.boundaries(getZeroLocation)
        self.front = []

        if getZeroLocation+3 <= 9:
            temp = subNode[node.index(' ')]
            subNode[node.index(' ')] = subNode[node.index(' ')+3]
            subNode[node.index(' ')+3] = temp
            self.front.append(self.heuristic(subNode))
            subNode = []
            subNode.extend(node)

        if getZeroLocation-3 >= 1:
            temp = subNode[node.index(' ')]
            subNode[node.index(' ')] = subNode[node.index(' ')-3]
            subNode[node.index(' ')-3] = temp
            self.front.append(self.heuristic(subNode))
            subNode = []
            subNode.extend(node)

        if getZeroLocation-1 >= boundary[0]:
            temp = subNode[node.index(' ')]
            subNode[node.index(' ')] = subNode[node.index(' ')-1]
            subNode[node.index(' ')-1] = temp
            self.front.append(self.heuristic(subNode))
            subNode = []
            subNode.extend(node)

        if getZeroLocation+1 <= boundary[1]:
            temp = subNode[node.index(' ')]
            subNode[node.index(' ')] = subNode[node.index(' ')+1]
            subNode[node.index(' ')+1] = temp
            self.front.append(self.heuristic(subNode))
            subNode = []
            subNode.extend(node)


a = hill_climbing_8_puzzle()
a.solver()
