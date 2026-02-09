from game.ui.screens.recruit_screen import RecruitScreen
from game.ui.screens.combat_viewer import CombatViewer
from game.common.enums import Phase

class ScreenManager:
    def __init__(self, screen):
        self.screen = screen
        self.recruit = RecruitScreen(screen)
        self.combat = CombatViewer(screen)
        self.active = self.recruit

    def set_state(self, state):
        if state.phase == Phase.RECRUIT:
            self.active = self.recruit
        elif state.phase == Phase.COMBAT:
            self.active = self.combat

        self.active.set_state(state)

    def handle_event(self, event):
        self.active.handle_event(event)

    def render(self):
        self.active.render()
