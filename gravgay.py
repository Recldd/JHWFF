import pygame
from pygame.locals import *

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Gravity Example')

# 색깔 정의
WHITE = (255, 255, 255)

# 중력 가속도 설정
gravity = 0.5

# 물체의 초기 위치, 속도 설정
object_rect = pygame.Rect(100, 100, 50, 50)
velocity_y = 0

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # 중력에 의해 속도 변경
    velocity_y += gravity

    # 물체의 위치 업데이트
    object_rect.y += velocity_y

    # 화면 지우기
    screen.fill(WHITE)

    # 물체 그리기
    pygame.draw.rect(screen, (0, 0, 255), object_rect)

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 수 설정
    pygame.time.Clock().tick(60)

pygame.quit()