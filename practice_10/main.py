import sys
import pygame
from persistence import load_settings, save_settings, load_leaderboard, add_leaderboard_entry
from ui import (
    screen_username,
    screen_main_menu,
    screen_settings,
    screen_leaderboard,
    screen_game_over,
)
from racer import run_game
from settings import screen_width, screen_height


def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Racer – TSIS3")
    clock = pygame.time.Clock()

    # ── load persistent data
    settings    = load_settings()
    leaderboard = load_leaderboard()

    # ── ask for username once per launch
    username = screen_username(screen, clock)

    while True:
        action = screen_main_menu(screen, clock)

        if action == "quit":
            break

        elif action == "leaderboard":
            leaderboard = load_leaderboard()
            screen_leaderboard(screen, clock, leaderboard)

        elif action == "settings":
            settings = screen_settings(screen, clock, settings)
            save_settings(settings)

        elif action == "play":
            while True:
                result = run_game(settings)

                # save to leaderboard
                leaderboard = add_leaderboard_entry(
                    username,
                    result["score"],
                    result["distance"]
                )

                choice = screen_game_over(screen, clock, result)
                if choice == "retry":
                    continue
                else:
                    break  # back to main menu

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()