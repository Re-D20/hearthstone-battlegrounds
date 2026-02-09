# game/server/server.py

import json
import socket
from game.server.state import ServerState
from game.server.validators import validate_intent
from game.server.transitions import apply_intent


HOST = "127.0.0.1"
PORT = 9999


def handle_client(conn, addr):
    print(f"Client connected from {addr}")
    state = ServerState.initial()

    # Send initial state
    conn.sendall(json.dumps(state.to_payload()).encode("utf-8"))

    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break

            intent = json.loads(data.decode("utf-8"))
            intent_type = validate_intent(intent, state)
            state = apply_intent(state, intent_type, intent)

            payload = state.to_payload()
            conn.sendall(json.dumps(payload).encode("utf-8"))
    finally:
        conn.close()
        print("Client disconnected")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            handle_client(conn, addr)


if __name__ == "__main__":
    main()
