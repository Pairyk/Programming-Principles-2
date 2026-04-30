"""ui.py – all Pygame screen flows (no external UI libs)."""

import pygame, sys
from pygame.locals import *
from settings import *


# ═══════════════════════════════════════════════════════════════
#  Low-level drawing helpers
# ═══════════════════════════════════════════════════════════════

def draw_text(surface, text, font, color, center):
    surf = font.render(text, True, color)
    surface.blit(surf, surf.get_rect(center=center))
    return surf.get_rect(center=center)


class Button:
    PADDING = (40, 14)

    def __init__(self, text, center, font, color=CYAN, text_color=DARK):
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = WHITE
        self.text_color = text_color
        txt_surf = font.render(text, True, text_color)
        w = txt_surf.get_width() + self.PADDING[0]
        h = txt_surf.get_height() + self.PADDING[1]
        self.rect = pygame.Rect(0, 0, w, h)
        self.rect.center = center

    def draw(self, surface):
        mouse = pygame.mouse.get_pos()
        hovered = self.rect.collidepoint(mouse)
        color = self.hover_color if hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        pygame.draw.rect(surface, WHITE, self.rect, 2, border_radius=8)
        txt = self.font.render(self.text, True, self.text_color)
        surface.blit(txt, txt.get_rect(center=self.rect.center))

    def is_clicked(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(event.pos)
        return False


def gradient_background(surface, top=(10,10,30), bottom=(30,30,60)):
    h = surface.get_height()
    w = surface.get_width()
    for y in range(h):
        r = top[0] + (bottom[0]-top[0]) * y // h
        g = top[1] + (bottom[1]-top[1]) * y // h
        b = top[2] + (bottom[2]-top[2]) * y // h
        pygame.draw.line(surface, (r,g,b), (0,y), (w,y))


# ═══════════════════════════════════════════════════════════════
#  Username entry
# ═══════════════════════════════════════════════════════════════

def screen_username(surface, clock):
    font_title = pygame.font.SysFont("Verdana", 42, bold=True)
    font_med   = pygame.font.SysFont("Verdana", 28)
    font_sm    = pygame.font.SysFont("Verdana", 22)

    name = ""
    cursor_visible = True
    cursor_timer = 0

    while True:
        dt = clock.tick(60)
        cursor_timer += dt
        if cursor_timer >= 500:
            cursor_visible = not cursor_visible
            cursor_timer = 0

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN and name.strip():
                    return name.strip()
                elif event.key == K_BACKSPACE:
                    name = name[:-1]
                elif len(name) < 18 and event.unicode.isprintable():
                    name += event.unicode

        gradient_background(surface)
        draw_text(surface, "RACER", font_title, YELLOW,
                  (screen_width//2, 120))
        draw_text(surface, "Enter your name:", font_med, WHITE,
                  (screen_width//2, 230))

        # input box
        box = pygame.Rect(screen_width//2 - 160, 270, 320, 48)
        pygame.draw.rect(surface, DARK, box, border_radius=8)
        pygame.draw.rect(surface, CYAN, box, 2, border_radius=8)
        display = name + ("|" if cursor_visible else " ")
        txt = font_med.render(display, True, WHITE)
        surface.blit(txt, txt.get_rect(center=box.center))

        draw_text(surface, "Press ENTER to start", font_sm, GRAY,
                  (screen_width//2, 350))

        pygame.display.flip()


# ═══════════════════════════════════════════════════════════════
#  Main Menu
# ═══════════════════════════════════════════════════════════════

def screen_main_menu(surface, clock):
    """Returns 'play' | 'leaderboard' | 'settings' | 'quit'."""
    font_title = pygame.font.SysFont("Verdana", 52, bold=True)
    font_btn   = pygame.font.SysFont("Verdana", 26, bold=True)

    cx = screen_width // 2
    buttons = {
        "play":        Button("▶  Play",       (cx, 280), font_btn, GREEN),
        "leaderboard": Button("🏆  Leaderboard",(cx, 350), font_btn, YELLOW),
        "settings":    Button("⚙  Settings",   (cx, 420), font_btn, CYAN),
        "quit":        Button("✕  Quit",        (cx, 490), font_btn, RED),
    }

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            for key, btn in buttons.items():
                if btn.is_clicked(event):
                    return key

        gradient_background(surface, (5,5,20), (20,20,50))

        # Title
        draw_text(surface, "RACER", font_title, YELLOW, (cx, 120))
        draw_text(surface, "Arcade Road Game", pygame.font.SysFont("Verdana",22), GRAY, (cx, 175))

        # Road decoration
        for i in range(0, screen_width, 60):
            pygame.draw.rect(surface, (40,40,40), (i, 220, 40, 8))

        for btn in buttons.values():
            btn.draw(surface)

        pygame.display.flip()


# ═══════════════════════════════════════════════════════════════
#  Settings Screen
# ═══════════════════════════════════════════════════════════════

def screen_settings(surface, clock, settings: dict) -> dict:
    """Returns updated settings dict."""
    import copy
    s = copy.deepcopy(settings)

    font_title = pygame.font.SysFont("Verdana", 36, bold=True)
    font_med   = pygame.font.SysFont("Verdana", 24, bold=True)
    font_sm    = pygame.font.SysFont("Verdana", 20)

    cx = screen_width // 2

    def toggle_btn(label, value, center, on_label="ON", off_label="OFF"):
        text = f"{label}: {on_label if value else off_label}"
        color = GREEN if value else RED
        return Button(text, center, font_sm, color)

    def option_btn(label, opts, current, center):
        idx = opts.index(current) if current in opts else 0
        text = f"{label}: {current.upper()}"
        return Button(text, center, font_sm, CYAN)

    back_btn = Button("← Back & Save", (cx, 600), font_med, YELLOW)

    # option state
    diff_opts  = ["easy", "normal", "hard"]
    color_opts = list(CAR_COLORS.keys())

    while True:
        clock.tick(60)

        sound_btn = toggle_btn("Sound", s["sound"],   (cx, 240))
        diff_btn  = option_btn("Difficulty", diff_opts, s["difficulty"], (cx, 310))
        color_btn = option_btn("Car color",  color_opts, s["car_color"],  (cx, 380))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            if sound_btn.is_clicked(event):
                s["sound"] = not s["sound"]
            if diff_btn.is_clicked(event):
                idx = diff_opts.index(s["difficulty"])
                s["difficulty"] = diff_opts[(idx+1) % len(diff_opts)]
            if color_btn.is_clicked(event):
                idx = color_opts.index(s["car_color"])
                s["car_color"] = color_opts[(idx+1) % len(color_opts)]
            if back_btn.is_clicked(event):
                return s

        gradient_background(surface)
        draw_text(surface, "SETTINGS", font_title, WHITE, (cx, 120))

        # car color preview
        preview_color = CAR_COLORS.get(s["car_color"], RED)
        pygame.draw.rect(surface, preview_color, (cx-20, 440, 40, 70), border_radius=6)
        draw_text(surface, "Preview", font_sm, GRAY, (cx, 525))

        sound_btn.draw(surface)
        diff_btn.draw(surface)
        color_btn.draw(surface)
        back_btn.draw(surface)

        pygame.display.flip()


# ═══════════════════════════════════════════════════════════════
#  Leaderboard Screen
# ═══════════════════════════════════════════════════════════════

def screen_leaderboard(surface, clock, entries: list):
    font_title = pygame.font.SysFont("Verdana", 36, bold=True)
    font_hdr   = pygame.font.SysFont("Verdana", 20, bold=True)
    font_row   = pygame.font.SysFont("Verdana", 20)
    back_btn   = Button("← Back", (screen_width//2, 640), font_hdr, YELLOW)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            if back_btn.is_clicked(event):
                return

        gradient_background(surface, (5,20,5), (10,40,10))
        draw_text(surface, "🏆  LEADERBOARD", font_title, YELLOW,
                  (screen_width//2, 60))

        # header
        cols = [40, 80, 220, 350]
        headers = ["#", "Name", "Score", "Dist(m)"]
        for x, h in zip(cols, headers):
            txt = font_hdr.render(h, True, CYAN)
            surface.blit(txt, (x, 110))
        pygame.draw.line(surface, GRAY, (30, 135), (screen_width-30, 135), 1)

        for i, e in enumerate(entries[:10]):
            y = 148 + i * 44
            rank_color = [YELLOW, (200,200,200), (180,120,60)]+[WHITE]*7
            color = rank_color[i]
            for x, val in zip(cols, [str(i+1), e.get("name","?"),
                                      str(e.get("score",0)),
                                      str(e.get("distance",0))]):
                txt = font_row.render(val, True, color)
                surface.blit(txt, (x, y))
            if i < len(entries)-1:
                pygame.draw.line(surface, (50,50,50), (30, y+36), (screen_width-30, y+36), 1)

        if not entries:
            draw_text(surface, "No scores yet!", font_hdr, GRAY,
                      (screen_width//2, 300))

        back_btn.draw(surface)
        pygame.display.flip()


# ═══════════════════════════════════════════════════════════════
#  Game Over Screen
# ═══════════════════════════════════════════════════════════════

def screen_game_over(surface, clock, result: dict) -> str:
    """Returns 'retry' | 'menu'."""
    font_title = pygame.font.SysFont("Verdana", 46, bold=True)
    font_med   = pygame.font.SysFont("Verdana", 26, bold=True)
    font_sm    = pygame.font.SysFont("Verdana", 22)

    cx = screen_width // 2
    title_text = "FINISHED! 🏁" if result.get("finished") else "GAME OVER"
    title_color = GREEN if result.get("finished") else RED

    retry_btn = Button("↺  Retry",     (cx, 480), font_med, GREEN)
    menu_btn  = Button("⌂  Main Menu", (cx, 550), font_med, CYAN)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            if retry_btn.is_clicked(event):
                return "retry"
            if menu_btn.is_clicked(event):
                return "menu"

        gradient_background(surface, (20,5,5), (40,10,10))
        draw_text(surface, title_text, font_title, title_color, (cx, 120))

        stats = [
            ("Score",    str(result.get("score", 0))),
            ("Distance", f"{result.get('distance', 0)} m"),
            ("Coins",    str(result.get("coins", 0))),
        ]
        for i, (label, val) in enumerate(stats):
            y = 220 + i * 60
            draw_text(surface, label, font_sm, GRAY, (cx-80, y))
            draw_text(surface, val,   font_med, WHITE, (cx+80, y))
            pygame.draw.line(surface, (60,60,60),
                             (cx-160, y+30), (cx+160, y+30), 1)

        retry_btn.draw(surface)
        menu_btn.draw(surface)
        pygame.display.flip()