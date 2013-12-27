#!/usr/bin/python
  
import bitcoinrpc
import sys, time
  
serverIP = '127.0.0.1'
serverPort = '1069'
user = 'username'
password = 'password'
address = 'AddressToSendCoinTo'
fee = 0.001

conn = bitcoinrpc.connect_to_remote(user, password, host=serverIP, port=serverPort);
  
while True:

    balance = conn.getbalance()
    print 'Your current balance is', balance
  
    if balance > fee:
        adjbalance = float(balance) - float(fee)    
        print 'Sending', adjbalance, 'to your designated address'
      
        try:
            conn.sendtoaddress(address,adjbalance)
        except Exception:
            pass
            print 'Coin send fail'
  
    time.sleep(3)
