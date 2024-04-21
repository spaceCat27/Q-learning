import pygame
from sys import exit
from agent import Agent
from enviroment import Enviroment

pygame.init()

board_size = 5
object_size = 50

env = Enviroment(board_size=board_size)
agent = Agent()

epochs = 10_000

for e in range(epochs):
    state = env.reset()
    done = False
    score = 0
    while not done:
        action = agent.action(state)
        next_state, reward, done = env.step(action)
        agent.update(state, action, next_state, reward, done)
        state = next_state
        score += reward
        
        if reward == 1:
            env.new_apple_position()
        if score == 15:
            #print(f'{e}: Wygrana')
            break


screen = pygame.display.set_mode((board_size * object_size, board_size * object_size))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

state = env.reset()
done = False
score = 0

snake = pygame.Rect(0, 0, 50, 50)
apple = pygame.Rect(env.apple_position[0] * object_size, env.apple_position[1] * object_size, 50, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('Black')
    pygame.draw.rect(screen, 'Red', snake)
    if reward != 1:
        pygame.draw.rect(screen, 'Green', apple)

    action = agent.action(state)
    next_state, reward, done = env.step(action)
    agent.update(state, action, next_state, reward, done)
    state = next_state
    score += reward


    snake.x = env.agent_position[0] * object_size
    snake.y = env.agent_position[1] * object_size
        

    if done:
        state = env.reset()
        snake.x = 0
        snake.y = 0
        apple.x = env.apple_position[0] * object_size
        apple.y = env.apple_position[1] * object_size
        
    if reward == 1:
        env.new_apple_position()
        apple.x = env.apple_position[0] * object_size
        apple.y = env.apple_position[1] * object_size
        

    pygame.display.update()
    clock.tick(2)
