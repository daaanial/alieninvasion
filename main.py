import pygame
import threading
import uvicorn
from fastapi import FastAPI
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from main_api import app as fastapi_app

def run_game(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, play_button, stats, sb)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

def run_fastapi():
    uvicorn.run(fastapi_app, host="127.0.0.1", port=8000, log_level="info")

if __name__ == "__main__":
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    fastapi_thread = threading.Thread(target=run_fastapi)
    fastapi_thread.start()

    run_game(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
