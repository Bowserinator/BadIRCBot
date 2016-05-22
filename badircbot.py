# A bad irc bot
# For extra lulz, run this bot with sudo under the root account
# Note: NEVER run something that doesn't need root access under the root account.
import socket
from time import sleep

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Hardcoding stuff is bad, use varaibles
# Also python's string.format method makes it neater
ircsock.connect(("irc.freenode.net",6667))
ircsock.send("USER "+"BadIRCBot"+" 0 * :"+"BadIRCBot"+"\n")
ircsock.send("NICK "+"BadIRCBot"+"\n")

sleep(7) # Doesn't really need to be here  

# You can JOIN multiple channels by JOIN #chan1,#chan2, etc...
ircsock.send("JOIN #badircbot\n".encode("utf8")) 

# Using nicks for your admin list isn't a good idea, use hostmasks
# Also, admins/non-admins isn't good, use a permission level dictionary instead (i.e. {"unaffiliated/iovoid": 5, etc)
admins = ["iovoid", "Bowserinator", "jeffl36"]

# Don't join yet - We don't want anyone deleting or bot
#ircsock.send("JOIN #powder-bots\n".encode("utf8"))
#ircsock.send("JOIN #botters-test\n".encode("utf8")) # For extra abuse


while True:
    try: # Try to prevent the bot from crashing every 5 seconds
        msg = ircsock.recv(2048) # You should probably strip \n\r from the message
        print(msg)
        
        # Commands
        # ------------------------------------------------------
        # elif/if statements for commands are bad in general
        # msg.find to get response type is bad
        # Having a nick variable, channel varaible, etc... is better and more understandable
        # Than msg.split(" ")[2] and stuff.
        # Check if message starts with !command, not if it's in the message
        # Check if type is PRIVMSG then do commands
        # Use a sendmsg function rather than doing PRIVMSG each time
        
        # Calc command uses raw eval and is very unsafe, people can delete your code/run unsafe scripts on your computer
        if msg.find("PRIVMSG") != -1 and msg.find("!calc") != -1:  # CAlc Cmd lel
            ircsock.send("PRIVMSG "+msg.split(" ")[2]+" "+ str(eval(msg.split("!calc")[1])) + "\n")
        
        # Bad string formatting, not understandable.
        if msg.find("PRIVMSG") != -1 and msg.find("!ping") != -1:  # pIng Cmd lel
            ircsock.send("PRIVMSG "+msg.split(" ")[2]+" :PONG"+str(msg.split("!ping")[1])+"\n")
        
        # Command using poor perm system
        if msg.find("PRIVMSG") != -1 and msg.find("!quit") != -1 and msg.split(" ")[0].split("!")[0].replace(":","") in admins:  # quit Cmd lel
            ircsock.send("QUIT :"+str(msg.split("!quit")[1])+"\n")
            
        # Echo commands should have a 0-width char to prevent abuse, also allows echo \nQUIT: and such commands
        if msg.find("PRIVMSG") != -1 and msg.find("!echo") != -1:  # echo Cmd lel
            ircsock.send("PRIVMSG "+msg.split(" ")[2]+" :"+str(msg.split("!echo")[1])+"\n")
            
        # List shouldn't be hardcoded
        if msg.find("PRIVMSG") != -1 and msg.find("!list") != -1:  # echo Cmd lel
            ircsock.send("PRIVMSG "+msg.split(" ")[2]+" :list, echo, ping, calc\n")
            
        if msg.find("PING") != -1: # Only supports freenode (and some other IRCds), ircd-ratbox requires a ping response with the correct key during registration
            ircsock.send("PONG :pingis\n".encode('utf-8'))
    except:
        # No error message makes errors completly useless and debugging a pain
        print("OH NOHS I HAVE ERRORED U WILL NEVER FIND THE ERROR THOUGH :D")
