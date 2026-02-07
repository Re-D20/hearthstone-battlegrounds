import pygame


class LogPanel:
    def __init__(self, rect):
        self.rect = pygame.Rect(rect)
        self.font = pygame.font.SysFont(None, 20)
        self.lines = []

    def set_logs(self, logs):
        self.lines = logs[-6:]  # display last entries only

    def render(self, surface):
        pygame.draw.rect(surface, (30, 30, 30), self.rect)
        pygame.draw.rect(surface, (150, 150, 150), self.rect, 1)

        y = self.rect.top + 5
        for line in self.lines:
            text = self.font.render(line, True, (220, 220, 220))
            surface.blit(text, (self.rect.left + 5, y))
            y += 20
