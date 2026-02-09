import pygame
from game.ui.components.shop_slot import ShopSlot
from game.ui.components.button import Button
from game.ui.components.log_panel import LogPanel
from game.ui.core.event_bus import event_bus

class RecruitScreen:
    def __init__(self, screen):
        self.shop_slots = []
        self.screen = screen
        self.state = None
        self.font = pygame.font.SysFont(None, 48)

        self.end_turn_btn = Button(
            rect=(1000, 600, 200, 50),
            text="End Turn",
            on_click=self.end_turn,
        )

        self.log_panel = LogPanel((20, 450, 600, 200))

    def set_state(self, state):
        self.state = state
        self.shop_slots = []

        # Build shop UI from player 1's shop
        p1 = state.players[0]
        if hasattr(p1, "shop"):
            x = 50
            for item in p1.shop:
                slot = ShopSlot(x, 300, 120, 80, item)
                self.shop_slots.append(slot)
                x += 140


    def end_turn(self):
        event_bus.serverQueue.put({"type": "END_TURN"})

    def handle_event(self, event):
        self.end_turn_btn.handle_event(event)
        for slot in self.shop_slots:
            slot.handle_event(event)



    def render(self):
        title = self.font.render("RECRUIT PHASE", True, (200, 200, 200))
        self.screen.blit(title, (50, 50))
        
        for slot in self.shop_slots:
            slot.render(self.screen)


        y = 150
        for player in self.state.players:
            text = self.font.render(
                f"Player {player.id} - HP: {player.health}",
                True,
                (180, 180, 180),
            )
            self.screen.blit(text, (50, y))
            y += 50

        self.end_turn_btn.render(self.screen)
        self.log_panel.render(self.screen)
