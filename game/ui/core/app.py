# game/ui/core/app.py

import pygame
from game.ui.core.screen_manager import ScreenManager
from game.ui.core.event_bus import event_bus
from game.ui.services.network import NetworkClient
from game.ui.services.state_loader import load_state_from_file


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Battlegrounds Client")

    clock = pygame.time.Clock()
    manager = ScreenManager(screen)

    # Fallback: local state (in case server is not running)
    try:
        state = load_state_from_file("data/mock_state.json")
        manager.set_state(state)
    except Exception:
        pass

    # Connect to server
    client = NetworkClient()
    try:
        client.connect()
        print("Connected to server")
    except Exception as e:
        print("Could not connect to server:", e)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            manager.handle_event(event)

        # Check if server sent a new state
        try:
            while not event_bus.uiQueue.empty():
                new_state = event_bus.uiQueue.get_nowait()
                manager.set_state(new_state)
        except Exception:
            pass

        screen.fill((15, 15, 15))
        manager.render()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
