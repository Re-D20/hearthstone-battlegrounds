# game/ui/services/network.py

import json
import socket
import threading
from game.ui.core.event_bus import event_bus
from game.ui.services.state_loader import load_state_from_dict


class NetworkClient:
    def __init__(self, host="127.0.0.1", port=9999):
        self.host = host
        self.port = port
        self.socket = None
        self.running = False

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.running = True

        threading.Thread(target=self._listen, daemon=True).start()
        threading.Thread(target=self._send, daemon=True).start()

    def _listen(self):
        while self.running:
            data = self.socket.recv(4096)
            if not data:
                break

            payload = json.loads(data.decode("utf-8"))
            game_state = load_state_from_dict(payload)

            # Server → UI
            event_bus.uiQueue.put(game_state)

    def _send(self):
        while self.running:
            intent = event_bus.serverQueue.get()
            message = json.dumps(intent).encode("utf-8")
            self.socket.sendall(message)
