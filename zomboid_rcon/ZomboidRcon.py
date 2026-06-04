"""Zomboid RCON: https://github.com/jmwhitworth/zomboid_rcon"""

from .BaseRconClient import BaseRconClient
from .CommandResult import CommandResult


class ZomboidRcon(BaseRconClient):
    """Used to interact with Zomboid servers via RCON"""

    def __init__(
        self,
        ip: str = "localhost",
        port: int = 27015,
        password: str = "pzserver",
        retries: int = 5,
        logging: bool = False,
    ):
        super().__init__(ip, port, password, retries, logging)

    #
    # GENERAL COMMANDS
    #

    def additem(self, user: str, item: str, count: int | None = None) -> CommandResult:
        """
        Gives the specified player a specified item.
        /additem "user" "module.item" count
        Items can be found on the PZ wiki: https://pzwiki.net/wiki/Items
        Count is optional.
        """
        if count is not None:
            return self.command("additem", user, item, str(count))
        return self.command("additem", user, item)

    def addvehicle(self, vehicle: str, user: str) -> CommandResult:
        """Spawns a vehicle near a player.
        /addvehicle vehiclescript 'user'
        """
        return self.command("addvehicle", vehicle, user)

    def addxp(self, user: str, perk: str, XP: int) -> CommandResult:
        """Gives XP to a player.
        /addxp "user" "perk=XP"
        """
        return self.command("addxp", user, f"{perk}={XP}")

    def alarm(self) -> CommandResult:
        """Sounds a building alarm at the admin's position. Must be in a room.
        /alarm
        """
        return self.command("alarm")

    def changeoption(self, option: str, newOption: str) -> CommandResult:
        """Changes a server option.
        /changeoption option="newOption"
        """
        return self.command("changeoption", f'{option}="{newOption}"')

    def chopper(self) -> CommandResult:
        """Places a helicopter event on a random player.
        /chopper
        """
        return self.command("chopper")

    def changepwd(self, pwd: str, newPwd: str) -> CommandResult:
        """Changes your password.
        /changepwd "pwd" "newPwd"
        """
        return self.command("changepwd", pwd, newPwd)

    def clear(self) -> CommandResult:
        """Clears the server console.
        /clear
        """
        return self.command("clear")

    def createhorde(self, number: int, user: str | None = None) -> CommandResult:
        """Spawns a horde near a player.
        /createhorde count "username"
        Username is optional.
        """
        if user is not None:
            return self.command("createhorde", str(number), user)
        return self.command("createhorde", str(number))

    def godmode(self, user: str, value: bool = True) -> CommandResult:
        """Makes a player invincible.
        /godmode "user" -value
        """
        return self.command("godmode", user, f"-{str(value).lower()}")

    def gunshot(self) -> CommandResult:
        """Makes a gunshot noise near the player.
        /gunshot
        """
        return self.command("gunshot")

    def help(self) -> CommandResult:
        """Brings up the help menu.
        /help
        Not to be confused with the commands available within zomboid_rcon. For a list of these commands see zomboid_rcon's Github repo: https://github.com/jmwhitworth/zomboid_rcon
        """
        return self.command("help")

    def invisible(self, user: str, value: bool = True) -> CommandResult:
        """Makes a player invisible to zombies.
        /invisible "user" -value
        """
        return self.command("invisible", user, f"-{str(value).lower()}")

    def lightning(self, user: str | None = None) -> CommandResult:
        """Triggers a lightning strike on a player.
        /lightning "username"
        Username is optional.
        """
        if user is not None:
            return self.command("lightning", user)
        return self.command("lightning")

    def log(self, log_type: str, level: str) -> CommandResult:
        """Sets the log level for a given log type.
        /log "type" level
        """
        return self.command("log", log_type, level)

    def noclip(self, user: str, value: bool = True) -> CommandResult:
        """Allows a player to pass through solid objects.
        /noclip "user" -value
        """
        return self.command("noclip", user, f"-{str(value).lower()}")

    def quit(self) -> CommandResult:
        """Saves and quits the server.
        /quit
        """
        return self.command("quit")

    def releasesafehouse(self) -> CommandResult:
        """Releases a safehouse you own.
        /releasesafehouse
        """
        return self.command("releasesafehouse")

    def reloadlua(self, filename: str) -> CommandResult:
        """Reload a lua script on the server.
        /reloadlua "filename"
        """
        return self.command("reloadlua", filename)

    def reloadoptions(self) -> CommandResult:
        """Reloads server options.
        /reloadoptions
        """
        return self.command("reloadoptions")

    def replay(self, user: str, command: str, filename: str) -> CommandResult:
        """Records and plays a replay for a moving player.
        /replay "user" [-record | -play | -stop] "filename"
        """
        return self.command("replay", user, command, filename)

    def save(self) -> CommandResult:
        """Saves the current world.
        /save
        """
        return self.command("save")

    def sendpulse(self) -> CommandResult:
        """Toggles sending server performance info to the client.
        /sendpulse
        """
        return self.command("sendpulse")

    def showoptions(self) -> CommandResult:
        """Shows a list of current server options and values.
        /showoptions
        """
        return self.command("showoptions")

    def startrain(self, intensity: int | None = None) -> CommandResult:
        """Starts rain on the server.
        /startrain "intensity"
        Intensity is optional, from 1 to 100.
        """
        if intensity is not None:
            return self.command("startrain", str(intensity))
        return self.command("startrain")

    def startstorm(self, duration: int | None = None) -> CommandResult:
        """Starts a storm on the server.
        /startstorm "duration"
        Duration is optional, in game hours.
        """
        if duration is not None:
            return self.command("startstorm", str(duration))
        return self.command("startstorm")

    def stats(self, mode: str, period: int | None = None) -> CommandResult:
        """Sets and clears server statistics.
        /stats none/file/console/all period
        Period is optional.
        """
        if period is not None:
            return self.command("stats", mode, str(period))
        return self.command("stats", mode)

    def stoprain(self) -> CommandResult:
        """Stops rain on the server.
        /stoprain
        """
        return self.command("stoprain")

    def stopweather(self) -> CommandResult:
        """Stops weather on the server.
        /stopweather
        """
        return self.command("stopweather")

    def teleport(self, user: str, toUser: str | None = None) -> CommandResult:
        """Teleports to a player.
        /teleport "toUser" or /teleport "user" "toUser"
        """
        if toUser is not None:
            return self.command("teleport", user, toUser)
        return self.command("teleport", user)

    def teleportto(self, x: int, y: int, z: int) -> CommandResult:
        """Teleports to certain coordinates.
        /teleportto x,y,z
        """
        return self.command("teleportto", f"{x},{y},{z}")

    def thunder(self, user: str | None = None) -> CommandResult:
        """Triggers a thunder event on a player.
        /thunder "username"
        Username is optional.
        """
        if user is not None:
            return self.command("thunder", user)
        return self.command("thunder")

    #
    # MODERATION COMMANDS
    #

    def addalltowhitelist(self) -> CommandResult:
        """Adds all current users connected with a password to the whitelist.
        /addalltowhitelist
        """
        return self.command("addalltowhitelist")

    def adduser(self, user: str, pwd: str) -> CommandResult:
        """Adds a new user to the whitelist.
        /adduser "user" "pwd"
        """
        return self.command("adduser", user, pwd)

    def addusertowhitelist(self, user: str) -> CommandResult:
        """Adds a single user connected with a password to the whitelist.
        /addusertowhitelist "user"
        """
        return self.command("addusertowhitelist", user)

    def removeuserfromwhitelist(self, user: str) -> CommandResult:
        """Removes a single user connected with a password to the whitelist.
        /removeuserfromwhitelist "user"
        """
        return self.command("removeuserfromwhitelist", user)

    def banid(self, SteamID: str) -> CommandResult:
        """Bans a Steam ID.
        /banid "SteamID"
        """
        return self.command("banid", SteamID)

    def unbanid(self, SteamID: str) -> CommandResult:
        """Unbans a Steam ID.
        /unbanid "SteamID"
        """
        return self.command("unbanid", SteamID)

    def banuser(self, user: str, ip: bool = False, reason: str | None = None) -> CommandResult:
        """Bans a user.
        /banuser "user" -ip -r "reason"
        -ip also bans the user's IP address. -r specifies a ban reason.
        """
        args = [user]
        if ip:
            args.append("-ip")
        if reason is not None:
            args.extend(["-r", reason])
        return self.command("banuser", *args)

    def unbanuser(self, user: str) -> CommandResult:
        """Unbans a user.
        /unbanuser "user"
        """
        return self.command("unbanuser", user)

    def checkModsNeedUpdate(self) -> CommandResult:
        """Indicates whether a mod has been updated. Writes answer to log file.
        /checkModsNeedUpdate
        """
        return self.command("checkModsNeedUpdate")

    def grantadmin(self, user: str) -> CommandResult:
        """Gives admin rights to a user.
        /grantadmin "user"
        """
        return self.command("grantadmin", user)

    def removeadmin(self, user: str) -> CommandResult:
        """Removes admin rights to a user.
        /removeadmin "user"
        """
        return self.command("removeadmin", user)

    def kickuser(self, user: str) -> CommandResult:
        """Kicks a user from the server.
        /kickuser "user"
        """
        return self.command("kickuser", user)

    def players(self) -> CommandResult:
        """Lists all connected players.
        /players
        """
        return self.command("players")

    def servermsg(self, message: str) -> CommandResult:
        """Broadcast a message to all players.
        /servermsg "message"
        Spaces are replaced with underscores for compatibility.
        """
        stripped = message.strip()
        if not stripped:
            raise ValueError("servermsg message cannot be empty or whitespace-only")
        return self.command("servermsg", stripped.replace(" ", "_"))

    def setaccesslevel(self, user: str, accesslevel: str) -> CommandResult:
        """Set the access/permission level of a player.
        /setaccesslevel "user" "[admin | moderator | overseer | gm | observer]"
        """
        return self.command("setaccesslevel", user, accesslevel)

    def voiceban(self, user: str, ban: str) -> CommandResult:
        """Ban a user from using the voice feature.
        /voiceban "user" [-true | -false]
        """
        return self.command("voiceban", user, ban)
