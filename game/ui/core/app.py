import pygame
from ui.services.network import NetworkClient
from ui.core.event_bus import event_bus


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    screen_manager = ScreenManager(screen)

    network = NetworkClient()
    network.connect()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Apply latest server state if available
        if not event_bus.uiQueue.empty():
            state = event_bus.uiQueue.get()
            screen_manager.set_state(state)

        screen.fill((20, 20, 20))
        screen_manager.render()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()