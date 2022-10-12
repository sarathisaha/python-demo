def validport(port):
    if(port >= 0):
        return "Valid Port"
    else:
        return "Not a valid port"

print (validport(-1))