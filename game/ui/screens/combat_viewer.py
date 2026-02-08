import pygame
from game.ui.components.log_panel import LogPanel
from game.ui.components.button import Button
from game.ui.core.event_bus import event_bus

class CombatViewer:
    def __init__(self, screen):
        self.screen = screen
        self.state = None
        self.font = pygame.font.SysFont(None, 48)
        self.log_panel = LogPanel((20, 450, 600, 200))

        # NEW: End combat button
        self.end_btn = Button(
            rect=(1000, 600, 200, 50),
            text="End Combat",
            on_click=self.end_combat
        )

    def set_state(self, state):
        self.state = state
        if hasattr(state, "log"):
            self.log_panel.set_logs(state.log)

    def end_combat(self):
        event_bus.serverQueue.put({"type": "END_TURN"})

    def handle_event(self, event):
        self.end_btn.handle_event(event)

    def render(self):
        title = self.font.render("COMBAT PHASE", True, (220, 100, 100))
        self.screen.blit(title, (50, 50))

        y = 150
        for player in self.state.players:
            text = self.font.render(
                f"Player {player.id} - Board size: {len(player.board)}",
                True,
                (200, 200, 200),
            )
            self.screen.blit(text, (50, y))
            y += 50

        self.end_btn.render(self.screen)
        self.log_panel.render(self.screen)
