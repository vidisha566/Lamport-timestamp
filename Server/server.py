#NAME: VIDISHA NARENDRA SHETTY                              UTA ID: 1001672826
"""Server for Synchronization and Logical clocks."""
from socket import AF_INET, socket, SOCK_STREAM 
from threading import Thread #Import for multithreading
import tkinter #Import for GUI
import random
from datetime import datetime #Import for date and time
import time

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True: #Loop waiting for incoming connection
        client, client_address = SERVER.accept() #Server logs the accepted connection 
        print("%s:%s has connected." % client_address) #Prints which client is connected
        client.send(bytes("Greetings from the server! Now type your name and press enter!", "utf8")) #Sends a welcome message to the client that is connected and asks for the user's name
        addresses[client] = client_address #Stores the connected client’s address in the addresses dictionary 
        Thread(target=handle_client, args=(client,)).start() #Handling thread for the connected client is initiated

def local_time(counter):
    return ' (LAMPORT_TIME={}, LOCAL_TIME={})'.format(counter, datetime.now())

def calc_recv_timestamp(recv_time_stamp, counter):
    return max(recv_time_stamp , counter) + 1

def handle_client(client):  #Takes client socket as argument.
    """Handles a single client connection."""
    name = client.recv(BUFSIZ).decode("utf8") #Saves the name given by the user
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name #Further instruction to quit the connection
    username[name] = client #Stores the connected client's name in the username dictionary
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined" % name #Whenever a new client joins the connection
    broadcast(bytes(msg, "utf8")) #Broadcasts the message to other clients
    clients[client] = name #Stores the client's name in client dictonary
    counter = str(random.randrange(0,50)) #Randomly generates counter between 0 to 50
    client.send(bytes('LAMPORT_TIME={}, LOCAL_TIME={}'.format(counter, datetime.now()), "utf8")) #Sends logical time and local time 
    t = datetime.now()
    while True:
     delta= datetime.now()-t
     if delta.seconds >= 1:
      counter = str(int(counter) + 1) #Increments the counter by 1 for every second
      client.send(bytes('LAMPORT_TIME={}, LOCAL_TIME={}'.format(counter, datetime.now()), "utf8"))
      t = datetime.now()
    while True:
        msg = client.recv(BUFSIZ) 
        if msg != bytes("{quit}", "utf8"): #If the msg doesn't contain {quit} it will broadcast the message to all the connected clients
            
            unicast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8")) 
            client.close() #The client that sends {quit} will be closed
            del clients[client] #Deletes the entry of the client
            broadcast(bytes("%s has left" % name, "utf8")) #Broadcasts that the client has left the chat
            break


def unicast(msg, receiverUsername , prefix=""):  #prefix is for name identification.
    """Unicasts a message to the desired client"""
    for name,socket in username.items(): 
        if receiverUsername == name:
            socket.send(bytes(prefix, "utf-8")+bytes(msg, "utf-8")) #Sends message to the desired client

def broadcast(msg, prefix=""): 
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg) 

def on_closing():
    top.destroy()

"""Dictonaries"""
clients = {}
addresses = {}
username = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)
if __name__ == "__main__":
    SERVER.listen(5) #Listens to maximum 5 connections 
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections) #Accepts incoming connections
    ACCEPT_THREAD.start() #Starts the infinite loop
    ACCEPT_THREAD.join()
    client.send (('HTTP/1.1 200 OK').encode('utf-8'))
    message = msg.encode("utf-8")
    client.send(b)
    print("Content-type: text")
    SERVER.close()
