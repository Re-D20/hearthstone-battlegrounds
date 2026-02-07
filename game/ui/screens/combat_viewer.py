import pygame 

class CombatViewer:
    def init(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 48)

    def render(self, game_state):
        title = self.font.render("COMBAT PHASE", True, (220, 100, 100))
        self.screen.blit(title, (50, 50))

        y = 150
        for player in game_state.players:
            text = self.font.render(
                f"Player {player.id} - Board size: {len(player.board)}",
                True,
                (200, 200, 200),
            )
            self.screen.blit(text, (50, y))
            y += 50