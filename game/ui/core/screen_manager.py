from common.enums import Phase
from ui.screens.recruit_screen import RecruitScreen
from ui.screens.combat_viewer import CombatViewer


class ScreenManager:
    def __init__(self, screen):
        self.screen = screen
        self.state = None
        self.recruit_screen = RecruitScreen(screen)
        self.combat_screen = CombatViewer(screen)

    def set_state(self, game_state):
        self.state = game_state

    def render(self):
        if self.state.phase == Phase.RECRUIT:
            self.recruit_screen.render(self.state)
        elif self.state.phase == Phase.COMBAT:
            self.combat_screen.render(self.state)
