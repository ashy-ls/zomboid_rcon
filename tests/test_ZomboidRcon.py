import unittest
from unittest.mock import MagicMock

from zomboid_rcon import CommandResult, ZomboidRcon


def make_success_result(command="test"):
    return CommandResult(command, "OK", successful=True)


class ZomboidRcon_test(unittest.TestCase):
    def setUp(self):
        self.pz = ZomboidRcon()
        self.pz.command = MagicMock(return_value=make_success_result())

    def test_constructor_defaults(self):
        pz = ZomboidRcon()
        self.assertEqual(pz._ip, "localhost")
        self.assertEqual(pz._port, 27015)
        self.assertEqual(pz._password, "pzserver")
        self.assertEqual(pz._retries, 5)
        self.assertFalse(pz.logging)

    def test_constructor_accepts_custom_values(self):
        pz = ZomboidRcon(ip="10.0.0.1", port=1234, password="pass", retries=3, logging=True)
        self.assertEqual(pz._ip, "10.0.0.1")
        self.assertEqual(pz._port, 1234)
        self.assertEqual(pz._password, "pass")
        self.assertEqual(pz._retries, 3)
        self.assertTrue(pz.logging)

    # --- General commands ---

    def test_players(self):
        self.pz.players()
        self.pz.command.assert_called_once_with("players")

    def test_save(self):
        self.pz.save()
        self.pz.command.assert_called_once_with("save")

    def test_quit(self):
        self.pz.quit()
        self.pz.command.assert_called_once_with("quit")

    def test_additem(self):
        self.pz.additem("user1", "Base.Axe")
        self.pz.command.assert_called_once_with("additem", "user1", "Base.Axe")

    def test_addvehicle(self):
        self.pz.addvehicle("Base.VanSeats", "user1")
        self.pz.command.assert_called_once_with("addvehicle", "Base.VanSeats", "user1")

    def test_addxp_formats_perk_correctly(self):
        self.pz.addxp("user1", "Strength", 100)
        self.pz.command.assert_called_once_with("addxp", "user1", "Strength=100")

    def test_teleport_single_arg(self):
        self.pz.teleport("user1")
        self.pz.command.assert_called_once_with("teleport", "user1")

    def test_teleport_two_args(self):
        self.pz.teleport("user1", "user2")
        self.pz.command.assert_called_once_with("teleport", "user1", "user2")

    def test_teleportto_formats_coordinates(self):
        self.pz.teleportto(100, 200, 0)
        self.pz.command.assert_called_once_with("teleportto", "100,200,0")

    def test_servermsg_replaces_spaces_with_underscores(self):
        self.pz.servermsg("Hello world")
        self.pz.command.assert_called_once_with("servermsg", "Hello_world")

    def test_servermsg_strips_leading_trailing_whitespace(self):
        self.pz.servermsg("  Hello  ")
        self.pz.command.assert_called_once_with("servermsg", "Hello")

    def test_createhorde(self):
        self.pz.createhorde(50)
        self.pz.command.assert_called_once_with("createhorde", "50")

    # --- Moderation commands ---

    def test_banuser(self):
        self.pz.banuser("badguy")
        self.pz.command.assert_called_once_with("banuser", "badguy")

    def test_unbanuser(self):
        self.pz.unbanuser("badguy")
        self.pz.command.assert_called_once_with("unbanuser", "badguy")

    def test_kickuser(self):
        self.pz.kickuser("someuser")
        self.pz.command.assert_called_once_with("kickuser", "someuser")

    def test_grantadmin(self):
        self.pz.grantadmin("someuser")
        self.pz.command.assert_called_once_with("grantadmin", "someuser")

    def test_removeadmin(self):
        self.pz.removeadmin("someuser")
        self.pz.command.assert_called_once_with("removeadmin", "someuser")

    def test_setaccesslevel(self):
        self.pz.setaccesslevel("someuser", "moderator")
        self.pz.command.assert_called_once_with("setaccesslevel", "someuser", "moderator")

    def test_adduser(self):
        self.pz.adduser("newuser", "password123")
        self.pz.command.assert_called_once_with("adduser", "newuser", "password123")
