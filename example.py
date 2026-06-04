"""Zomboid RCON: https://github.com/jmwhitworth/zomboid_rcon"""

import os

from zomboid_rcon import ZomboidRcon

# Sets to env variables for testing, with defaults set otherwise
IP = os.getenv("IP", "127.0.0.1")
PORT = int(os.getenv("PORT", 27015))
PASSWORD = os.getenv("PASSWORD", "myPassword")
RETRIES = int(os.getenv("RETRIES", 5))
LOGGING = os.getenv("LOGGING", "False").lower() == "true"


if __name__ == "__main__":
    pz = ZomboidRcon(
        ip=IP, port=PORT, password=PASSWORD, retries=RETRIES, logging=LOGGING
    )

    # Shows list of all currently connected players
    print(pz.players())

    # Broadcasts message to all players
    print(pz.servermsg("This is how you all died!"))

    # Shows list of current server options and values
    print(pz.showoptions())

    # For more, check the README.md
