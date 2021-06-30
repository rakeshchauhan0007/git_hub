cargame= ""
print('Type:::>Game (to know the detail about the game)')
while cargame=="":

 startgame: str= input('<--->:')
 if startgame.lower()=='game':
     print('to start the car<--->type(start)')
     print('to stop the car<--->type(hitbrake)')
     print('to quit the game<--->type(stop)')

 elif startgame.lower()=='start':
     print("car has started...")
     while cargame.lower()=="":
      astart=input('<-->')
      if astart.lower()=='start':
         print('car has already started...')
      elif astart.lower()=='quit':
         print('car has not stopped so you cannot exit...')
      elif astart.lower()=='stop':
         print('car has stopped___')
         break
      else:
         print('type appropriate keyword:>')

 if startgame.lower()=='stop':
     print('you havent started the car yet..')
 elif startgame== 'quit':
    print('you have exited---')
    break

else:
  print('i didnot understand what you typed, please type again<>..')
