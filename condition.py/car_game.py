cargame=""
while cargame == "":
    game_command= input('>:')
    if game_command.lower() == 'game':
        print('start: to start the car')
        print('stop:stop the car')
        print('exit:exit the car')
    elif game_command.lower() == 'start':
        print('>>>>>>>>..........car started>>>>>>>>>>>>')
    elif game_command.lower() == 'stop':
        print('<><><>car stopped<><><><>')
    elif game_command.lower()== 'exit':
        print('end')
        break
else:
    print('i did not understand what you said')




