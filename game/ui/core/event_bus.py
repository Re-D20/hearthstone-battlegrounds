import queue


class EventBus:
    def __init__(self):
        self.uiQueue = queue.Queue()
        self.serverQueue = queue.Queue()


event_bus = EventBus()
