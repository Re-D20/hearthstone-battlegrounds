from ui.services.state_loader import load_state_from_file

def test_load_valid_state():
    state = load_state_from_file("data/mock_state.json")
    assert state.phase.name in ["RECRUIT", "COMBAT"]
    assert len(state.players) == 2
