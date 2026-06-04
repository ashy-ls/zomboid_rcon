import unittest
from unittest.mock import MagicMock

from zomboid_rcon import BaseRconClient, CommandResult


def make_mock_cm(return_value="OK"):
    """Returns a mock context manager that simulates rcon.source.Client."""
    mock_cm = MagicMock()
    mock_cm.__enter__ = MagicMock(return_value=mock_cm)
    mock_cm.__exit__ = MagicMock(return_value=False)
    mock_cm.run.return_value = return_value
    return mock_cm


class BaseRconClient_test(unittest.TestCase):
    def setUp(self):
        self.client = BaseRconClient("127.0.0.1", 27015, "secret")

    def test_constructor_stores_values(self):
        self.assertEqual(self.client._ip, "127.0.0.1")
        self.assertEqual(self.client._port, 27015)
        self.assertEqual(self.client._password, "secret")
        self.assertEqual(self.client._retries, 5)
        self.assertFalse(self.client.logging)

    def test_command_success_returns_successful_result(self):
        mock_cm = make_mock_cm("players: user1, user2")
        self.client.createClient = MagicMock(return_value=mock_cm)

        result = self.client.command("players")

        self.assertIsInstance(result, CommandResult)
        self.assertTrue(result.successful)
        self.assertEqual(result.response, "players: user1, user2")

    def test_command_passes_args_to_client(self):
        mock_cm = make_mock_cm()
        self.client.createClient = MagicMock(return_value=mock_cm)

        self.client.command("additem", "user1", "Base.Axe")

        mock_cm.run.assert_called_once_with("additem", "user1", "Base.Axe")

    def test_command_connection_refused_returns_failure(self):
        self.client.createClient = MagicMock(side_effect=ConnectionRefusedError)

        result = self.client.command("players")

        self.assertFalse(result.successful)
        self.assertIn("refused", result.response.lower())

    def test_command_connection_refused_does_not_retry(self):
        self.client.createClient = MagicMock(side_effect=ConnectionRefusedError)

        self.client.command("players")

        self.assertEqual(self.client.createClient.call_count, 1)

    def test_command_timeout_exhausts_retries_and_returns_failure(self):
        client = BaseRconClient("127.0.0.1", 27015, "secret", retries=2)
        client.createClient = MagicMock(side_effect=TimeoutError)

        result = client.command("players")

        self.assertFalse(result.successful)
        self.assertIn("timed out", result.raw_response.lower())

    def test_command_timeout_retries_correct_number_of_times(self):
        # retries=2 → 3 total attempts (initial + 2 retries)
        client = BaseRconClient("127.0.0.1", 27015, "secret", retries=2)
        client.createClient = MagicMock(side_effect=TimeoutError)

        client.command("players")

        self.assertEqual(client.createClient.call_count, 3)

    def test_command_succeeds_after_timeout_retry(self):
        mock_cm = make_mock_cm("OK")
        self.client.createClient = MagicMock(
            side_effect=[TimeoutError, mock_cm]
        )

        result = self.client.command("save")

        self.assertTrue(result.successful)
        self.assertEqual(self.client.createClient.call_count, 2)

    def test_getinfo_masks_password(self):
        info = self.client.getInfo()
        self.assertEqual(info["password"], "***")
        self.assertNotIn("secret", info.values())

    def test_getinfo_returns_correct_fields(self):
        info = self.client.getInfo()
        self.assertEqual(info["ip"], "127.0.0.1")
        self.assertEqual(info["port"], 27015)
        self.assertEqual(info["retries"], 5)
