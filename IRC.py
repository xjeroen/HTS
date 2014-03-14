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
irc.send(bytes('JOIN ' + BOT_IRC_CHANNEL+'\r\n', 'utf-8'))


while 1:
    line = irc.recv(4096)
    print(line)
    if line.find(bytes('PING', 'utf-8')) != -1:
        line = line.rstrip().split()
        if line[0] == bytes("PING", 'utf-8'):
            print('PONG')
            irc.send(bytes('PONG ' + str(line[1])+'\r\n', 'utf-8'))

