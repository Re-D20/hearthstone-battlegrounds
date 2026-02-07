import pygame


class RecruitScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 48)

    def render(self, game_state):
        title = self.font.render("RECRUIT PHASE", True, (200, 200, 200))
        self.screen.blit(title, (50, 50))

        y = 150
        for player in game_state.players:
            text = self.font.render(
                f"Player {player.id} - HP: {player.health}",
                True,
                (180, 180, 180),
            )
            self.screen.blit(text, (50, y))
            y += 50
