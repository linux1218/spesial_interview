import pygame

pygame.init()

#화면 크기 설정
screen_width = 480 
screen_height = 640 
screen=pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Game")

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# 게임 종료
pygame.quit()