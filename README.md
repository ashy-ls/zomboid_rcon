# zomboid_rcon: Python RCON for Project Zomboid Servers

### Version: 2.0.0

zomboid_rcon enables you to easily communicate with your Project Zomboid servers via RCON. With zomboid_rcon, you can send commands to your server, manage players, and more, all from within your Python script.

- [GitHub Repo](https://github.com/jmwhitworth/zomboid_rcon)
- [Pypi Package](https://pypi.org/project/zomboid-rcon/)


# Installation

To get started, simply install zomboid-rcon using pip:

```bash
pip install zomboid-rcon
```


# Usage

Using zomboid_rcon is easy. Here's a basic example:

```python
from zomboid_rcon import ZomboidRcon

if __name__ == "__main__":
    pz = ZomboidRcon(ip='localhost', port=12345, password='myPassword')
    command = pz.servermsg("You dead yet?")
    print(command)
```

This example connects to a server running on your local machine and sends the message "You dead yet?".

zomboid_rcon provides several built-in methods for common server management tasks, such as getting a list of connected players:

```python
from zomboid_rcon import ZomboidRcon

if __name__ == "__main__":
    pz = ZomboidRcon(ip='localhost', port=12345, password='myPassword')
    print(pz.players())
```

This example prints a list of all players currently connected to the server.


# Available Commands

zomboid_rcon provides built-in methods for the available RCON commands within Project Zomboid.

These methods were curated from the list of commands listed here: [https://pzwiki.net/w/index.php?oldid=1361361](https://pzwiki.net/w/index.php?oldid=1361361)

## General Commands

- `additem("user", "item")` : Gives a player an item. Items can be found on the PZ wiki: https://pzwiki.net/wiki/Items
- `additem("user", "item", count)` : As above, with an optional item count.
- `addvehicle("vehiclescript", "user")` : Spawns a vehicle near a player.
- `addxp("user", "perk", xp)` : Gives XP to a player.
- `alarm()` : Sounds a building alarm at the admin's position. Must be in a room.
- `changeoption("option", "newOption")` : Changes a server option.
- `chopper()` : Places a helicopter event on a random player.
- `changepwd("pwd", "newPwd")` : Changes your password.
- `clear()` : Clears the server console.
- `createhorde(count)` : Spawns a horde near you.
- `createhorde(count, "username")` : Spawns a horde near a specific player.
- `godmode("user")` : Makes a player invincible (default: true).
- `godmode("user", False)` : Removes invincibility from a player.
- `gunshot()` : Places a gunshot sound on a random player.
- `help()` : Brings up the help menu. (Lists native RCON commands. For all zomboid_rcon commands, refer to this list)
- `invisible("user")` : Makes a player invisible to zombies (default: true).
- `invisible("user", False)` : Makes a player visible to zombies again.
- `lightning()` : Triggers a lightning strike on a random player.
- `lightning("user")` : Triggers a lightning strike on a specific player.
- `log("type", "level")` : Sets the log level for a log type.
- `noclip("user")` : Allows a player to pass through solid objects (default: true).
- `noclip("user", False)` : Disables noclip for a player.
- `quit()` : Saves and quits the server.
- `releasesafehouse()` : Releases a safehouse you own.
- `reloadlua("filename")` : Reload a lua script on the server.
- `reloadoptions()` : Reloads server options.
- `replay("user", [-record | -play | -stop], "filename")` : Records and plays a replay for a moving player.
- `save()` : Saves the current world.
- `sendpulse()` : Toggles sending server performance info to the client.
- `showoptions()` : Shows a list of current server options and values.
- `startrain()` : Starts rain on the server.
- `startrain(intensity)` : Starts rain at a specific intensity (1–100).
- `startstorm()` : Starts a storm on the server.
- `startstorm(duration)` : Starts a storm with a specific duration in game hours.
- `stats("mode")` : Sets server statistics mode (none/file/console/all).
- `stats("mode", period)` : As above, with a reporting period.
- `stoprain()` : Stops rain on the server.
- `stopweather()` : Stops all weather on the server.
- `teleport("user")` : Teleports yourself to a player.
- `teleport("user", "toUser")` : Teleports one player to another.
- `teleportto(x, y, z)` : Teleports to certain coordinates.
- `thunder()` : Triggers a thunder event on a random player.
- `thunder("user")` : Triggers a thunder event on a specific player.

## Moderation Commands

- `addalltowhitelist()` : Adds all current users connected with a password to the whitelist.
- `adduser("user", "pwd")` : Adds a new user to the whitelist.
- `addusertowhitelist("user")` : Adds a single user connected with a password to the whitelist.
- `removeuserfromwhitelist("user")` : Removes a single user from the whitelist.
- `banid("SteamID")` : Bans a Steam ID.
- `unbanid("SteamID")` : Unbans a Steam ID.
- `banuser("user")` : Bans a user.
- `banuser("user", ip=True)` : Bans a user and their IP address.
- `banuser("user", reason="reason")` : Bans a user with a reason.
- `banuser("user", ip=True, reason="reason")` : Bans a user, their IP, with a reason.
- `unbanuser("user")` : Unbans a user.
- `checkModsNeedUpdate()` : Indicates whether a mod has been updated. Writes answer to log file.
- `grantadmin("user")` : Gives admin rights to a user.
- `removeadmin("user")` : Removes admin rights from a user.
- `kickuser("user")` : Kicks a user from the server.
- `players()` : Lists all connected players.
- `servermsg("message")` : Broadcast a message to all players. (Spaces are replaced with underscores for compatibility)
- `setaccesslevel("user", [admin | moderator | overseer | gm | observer])` : Set the access/permission level of a player.
- `voiceban("user", [-true | -false])` : Ban a user from using the voice feature.

## Command not listed?

You can execute any custom command using the command method:
```python
pz.command("command", "arg1", "arg2", "etc")
```


# Demonstration

![Zomboid RCON demonstration GIF](https://raw.githubusercontent.com/jmwhitworth/zomboid_rcon/refs/heads/main/docs/zomboid_rcon_demo.gif)


# Known Issues

Please raise any issues in the GitHub repo.


# Contributing

We welcome contributions from anyone! If you would like to contribute to the project, please open an issue or submit a pull request on [Github](https://github.com/jmwhitworth/zomboid_rcon).


# Testing

Tests can be ran using unittest:

```bash
python -m unittest
```


# License

zomboid_rcon is licensed under the GPL-3.0 license.
