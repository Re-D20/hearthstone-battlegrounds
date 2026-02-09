import pygame
from game.ui.core.event_bus import event_bus

class ShopSlot:
    def __init__(self, x, y, width, height, minion):
        self.rect = pygame.Rect(x, y, width, height)
        self.minion = minion
        self.font = pygame.font.SysFont(None, 24)

    def render(self, screen):
        pygame.draw.rect(screen, (60, 60, 60), self.rect)
        pygame.draw.rect(screen, (200, 200, 200), self.rect, 2)

        text = self.font.render(self.minion["card_id"], True, (255, 255, 255))
        screen.blit(text, (self.rect.x + 5, self.rect.y + 5))

        buy_text = self.font.render("BUY", True, (255, 255, 0))
        screen.blit(buy_text, (self.rect.x + 5, self.rect.y + 30))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                event_bus.serverQueue.put({
                    "type": "BUY",
                    "minion_id": self.minion["card_id"]
                })
