import random

class Agent:
    def __init__(self, epsilon_decay=0.995, learning_rate=0.1, discount=0.9, action_number=5):
        self.epsilon = 1.0
        self.epsilon_decay = epsilon_decay
        self.q_table = {}
        self.learning_rate = learning_rate
        self.discount = discount
        self.action_number = action_number

    def action(self, state):
        if random.random() < self.epsilon:
            action =  random.randint(0, 4)
        else:
            action = self.best_action(state)

        if self.epsilon > 0.02:
            self.epsilon *= self.epsilon_decay

        return action

    def best_action(self, state):
        if state not in self.q_table:
            return random.randint(0, 3)
        return self.q_table[state].index(max(self.q_table[state]))

    def update(self, state, action, next_state, reward, done):
        if state not in self.q_table:
            self.q_table[state] = [0 for _ in range(self.action_number)]
            
        if next_state not in self.q_table:
            self.q_table[next_state] = [0 for _ in range(self.action_number)]
            
        if not done:
            self.q_table[state][action] += self.learning_rate *\
                (reward + self.discount * max(self.q_table[next_state]) -  self.q_table[state][action])
        if done:
            self.q_table[state][action] += self.learning_rate *\
                                           (reward - self.q_table[state][action])