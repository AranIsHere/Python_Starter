import sys

import pygame

from alienGame.Settings import Settings
from alienGame.game_stats import GameStats
from alienGame.ship import Ship
import alienGame.game_functions as gf
# from alienGame.alien import Alien
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个外星人编组
    aliens = Group()
    # 设置背景色

    bg_color = (230, 230, 230)

    # alien = Alien(ai_settings, screen)

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏的主循环

    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(aliens, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
