import random

class Enviroment:
    def __init__(self, board_size=2):
        self.board_size = board_size
        self.agent_position = [0, 0]
        self.apple_position = [random.randint(0, board_size - 1), random.randint(0, board_size - 1)]

    def step(self, action):
        #lewo
        if action == 0:
            self.agent_position[0] -= 1

        #dol
        if action == 1:
            self.agent_position[1] += 1

        #prawo
        if action == 2:
            self.agent_position[0] += 1

        #gora
        if action == 3:
            self.agent_position[1] -= 1

        if self.agent_position == self.apple_position:
            reward = 1
            done = 0
        elif self.agent_position[0] >= self.board_size or self.agent_position[0] < 0:
            reward = -1
            done = 1
        elif self.agent_position[1] >= self.board_size or self.agent_position[1] < 0:
            reward = -1
            done = 1
        else:
            reward = 0
            done = 0

        vector = self.create_vector()

        return [vector, reward, done]

    def reset(self):
        self.agent_position = [0, 0]
        self.new_apple_position()
        vector = self.create_vector()
        return vector

    def create_vector(self):
        x_vector = self.agent_position[0] - self.apple_position[0]
        y_vector = self.agent_position[1] - self.apple_position[1]

        return tuple([x_vector, y_vector])
    
    def new_apple_position(self):
        while True:
            y_position = random.randint(0, self.board_size - 1)
            x_position = random.randint(0, self.board_size - 1)
            if y_position != self.agent_position[1] or x_position != self.agent_position[0]:
                break
        self.apple_position = [x_position, y_position]
    
