import logging

# Reset
Color_Off = "\033[0m"       # Text Reset

# Regular Colors
Black = "\033[0;30m"        # Black
Red = "\033[0;31m"          # Red
Green = "\033[0;32m"        # Green
Yellow = "\033[0;33m"       # Yellow
Blue = "\033[0;34m"         # Blue
Purple = "\033[0;35m"       # Purple
Cyan = "\033[0;36m"         # Cyan
White = "\033[0;37m"        # White

# Bold
BBlack = "\033[1;30m"       # Black
BRed = "\033[1;31m"         # Red
BGreen = "\033[1;32m"       # Green
BYellow = "\033[1;33m"      # Yellow
BBlue = "\033[1;34m"        # Blue
BPurple = "\033[1;35m"      # Purple
BCyan = "\033[1;36m"        # Cyan
BWhite = "\033[1;37m"       # White

# Underline
UBlack = "\033[4;30m"       # Black
URed = "\033[4;31m"         # Red
UGreen = "\033[4;32m"       # Green
UYellow = "\033[4;33m"      # Yellow
UBlue = "\033[4;34m"        # Blue
UPurple = "\033[4;35m"      # Purple
UCyan = "\033[4;36m"        # Cyan
UWhite = "\033[4;37m"       # White

# Background
On_Black = "\033[40m"       # Black
On_Red = "\033[41m"         # Red
On_Green = "\033[42m"       # Green
On_Yellow = "\033[43m"      # Yellow
On_Blue = "\033[44m"        # Blue
On_Purple = "\033[45m"      # Purple
On_Cyan = "\033[46m"        # Cyan
On_White = "\033[47m"       # White

logging.getLogger("twitchio.client").setLevel(logging.ERROR)
logging.getLogger("twitchio.http").setLevel(logging.ERROR)
logging.getLogger("twitchio.websocket").setLevel(logging.ERROR)
logging.getLogger("websockets.protocol").setLevel(logging.ERROR)

def setup_logger(logger):
	formatter = logging.Formatter('[%(asctime)s] [%(levelname)s]: %(message)s', '%Y-%m-%d %H:%M:%S')
	fh = logging.FileHandler('logs.log')
	sh = logging.StreamHandler()
	fh.setFormatter(formatter)
	sh.setFormatter(formatter)
	logger.setLevel(5)

	def decorate_emit(fn):
		def new(*args):
			levelno = args[0].levelno
			if levelno >= logging.CRITICAL:
				colour = BPurple
			elif levelno >= logging.ERROR:
				colour = BRed
			elif levelno >= logging.WARNING:
				colour = BYellow
			elif levelno >= logging.INFO:
				colour = BWhite
			elif levelno >= logging.DEBUG:
				colour = BGreen
			elif levelno >= 5:
				colour = BBlue
				args[0].levelname = "CHAT"
			else:
				colour = Color_Off
			args[0].levelname = "{0}{1}\033[0;0m".format(colour, args[0].levelname)

			return fn(*args)
		return new

	sh.emit = decorate_emit(sh.emit)
	logger.addHandler(fh)
	logger.addHandler(sh)
