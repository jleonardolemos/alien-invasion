import unittest
from game_state import GameState 

class TestGameState(unittest.TestCase):
    def setUp(self):
        self.game_state = GameState()

    def test_it_begins_as_start_state(self):
        self.assertTrue(self.game_state.has_game_just_started())
        self.assertFalse(self.game_state.is_game_running())
        self.assertFalse(self.game_state.is_game_paused())

    def test_it_can_change_to_running_state(self):
        self.game_state.run_game()
        self.assertFalse(self.game_state.has_game_just_started())
        self.assertTrue(self.game_state.is_game_running())
        self.assertFalse(self.game_state.is_game_paused())

    def test_it_can_change_to_paused_state(self):
        self.game_state.pause_game()
        self.assertFalse(self.game_state.has_game_just_started())
        self.assertFalse(self.game_state.is_game_running())
        self.assertTrue(self.game_state.is_game_paused())

    def test_it_return_to_start_state(self):
        self.game_state.pause_game()
        self.game_state.restart_game()
        self.assertTrue(self.game_state.has_game_just_started())
        self.assertFalse(self.game_state.is_game_running())
        self.assertFalse(self.game_state.is_game_paused())