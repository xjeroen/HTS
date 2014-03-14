__author__ = 'Jeroen'

import socket

BOT_IRC_SERVER = "irc.geekshed.net"
BOT_IRC_CHANNEL = "#bottesting"
BOT_IRC_PORT = 6667
BOT_NICKNAME = "xjBot"
BOT_OWNER = "xjeroen"

irc = socket.socket() #socket.AF_INET, socket.SOCK_STREAM
irc.connect((BOT_IRC_SERVER, BOT_IRC_PORT))

irc.recv(4096)
irc.send(bytes('NICK '+BOT_NICKNAME+'\r\n', 'utf-8'))
irc.send(bytes('USER xjBot xjBot xjBot : xj IRC\r\n', 'utf-8'))



while 1:
    line = irc.recv(4096)
    print(line)
    if line.find(bytes('Welcome to the GeekShed IRC Network', 'utf-8')) != -1:
        irc.send(bytes('JOIN ' + BOT_IRC_CHANNEL+'\r\n', 'utf-8'))
    if line.find(bytes('PING', 'utf-8')) != -1:
        #parsemsg(line)
        line = line.rstrip()
        line = line.split()
        print("Line 0:"+str(line[0]))
        if line[0] == "b'PING'":
            print('Succes')
            irc.send(bytes('PONG ' + line[1]+'\r\n'))

