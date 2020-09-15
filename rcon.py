from mcrcon import MCRcon
import sys

try:
    def collectArgv():
        argvs = ""
        for x in range(1, len(sys.argv)):
            argvs = argvs + sys.argv[x] + " "
        return argvs

    if(len(sys.argv) > 1):
        with MCRcon("87.104.32.36", "minecraft") as mcr:
            resp = mcr.command(collectArgv())
            print(resp)
except OSError:
    print("errorX")
