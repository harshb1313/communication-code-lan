# coding: UTF-8

from lan import Lan

#Timeout(1sec)
Timeout_default = 1

def main():
    #Instantiation of the LAN communication class
    lan = Lan(Timeout_default)

    #Connect
    print("IP?")
    IP = input()
    print("Port?")
    port = int(input())
    if not lan.open(IP, port):
        return
    
    #Send and receive commands
    while True:
        print("Please enter the command (Exit with no input)")
        command = input()
        #Exit if no input
        if command == "":
            break
        #If the command contains "?"
        if "?" in command :
            msgBuf = lan.SendQueryMsg(command, Timeout_default)
            print(msgBuf) 
        #Send only
        else:
            lan.sendMsg(command)
        
    lan.close()

if __name__ == '__main__':
  main()
