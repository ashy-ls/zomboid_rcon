"""Zomboid RCON: https://github.com/jmwhitworth/zomboid_rcon"""

from rcon.exceptions import SessionTimeout, WrongPassword
from rcon.source import Client

from .CommandResult import CommandResult


class BaseRconClient:
    """RCON client for sending commands to a server."""

    def __init__(
        self, ip: str, port: int, password: str, retries: int = 5, logging: bool = False
    ):
        """Args:
        ip (str): The IP Address of the server.
        port (int): The RCON port of the server.
        password (str): The RCON password of the server.
        retries (int): Number of retries on request timeout (must be >= 0).
        logging (bool): Print processes in terminal while running, used in debugging.
        """
        if retries < 0:
            raise ValueError(f"retries must be >= 0, got {retries}")
        self._ip = ip
        self._port = port
        self._password = password
        self._retries = retries
        self.logging = logging

    def createClient(self) -> Client:
        """Returns an rcon.source.Client object for requests"""
        return Client(self._ip, self._port, passwd=self._password, timeout=10)

    def command(self, command: str, *args) -> CommandResult:
        """
        Attempts to execute a given command.
        Upon TimeoutError it will retry according to self._retries
        """
        tries = 0
        while tries <= self._retries:
            try:
                with self.createClient() as client:
                    result = client.run(command, *args)
                return CommandResult(command=command, successful=True, response=result)
            except ConnectionRefusedError:
                return CommandResult(
                    command=command,
                    successful=False,
                    response="Connection refused",
                    failureMessage="Connection refused",
                )
            except WrongPassword:
                msg = "Wrong RCON password"
                return CommandResult(
                    command=command, successful=False, response=msg, failureMessage=msg
                )
            except SessionTimeout as e:
                detail = str(e) or "packet ID mismatch"
                msg = f"Session timeout: {detail}"
                return CommandResult(
                    command=command, successful=False, response=msg, failureMessage=msg
                )
            except TimeoutError:
                if self.logging:
                    print(
                        f"({tries+1}/{self._retries+1}) Request timed out, retrying..."
                    )
                tries += 1
        timeout_msg = f"Session timed out (after {self._retries + 1} attempt(s))"
        return CommandResult(
            command=command,
            successful=False,
            response=timeout_msg,
            failureMessage=timeout_msg,
        )

    def getInfo(self) -> dict:
        """Returns dict of current object's information"""
        return {
            "ip": self._ip,
            "port": self._port,
            "password": "***",
            "retries": self._retries,
        }
