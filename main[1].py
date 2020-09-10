import random
on = input ("(would you like to start or end)")
while on == "start":
  player = input(
     " (type 1, 2, or random)? ")
  if player == "1":
      print("you chose option 1")
      place = input("(name a place) ") 
      person = input("(name a person)") 
      thing = input("(name a object)")
      place2 = input("(name another place)")
      person2 = input("(name another person)")
      item = input("(name a item you sit on)")

      print("after walking for miles and finally reaching " + place + " you find " + person + " waiting for you.After talking for a while he reaches into the pocket of his jacket and then hands you a " + thing + ",in which he tells you to deliver it to " + place2 + ".After speaking with him you set of to an unknown place and find " + person2 + " waiting in the darkness.They ask you for the item you hand it over and head home.upon reaching you house you enter and sit on your " + item + " and read a fantasy book")
      on = input("(would you like start again or end)")

  elif player == "2":
    print("you chose option 2")
    wake = input("(what do you like more a tv or a monitor)")
    name = input("(name a person)")
    number = input("(pick a number from 1-4)")
    print ("you wake to see a " + wake + " infront of you.You don't remember your name but then on the " + wake + " a video starts to play and they say the name " + name + ", you suddenly realise your stuck in a room with 4 doors.The strange man behind a mask asks you to chose 1 of the 4 doors, you choose door " + number)
    if number == "1":
      print("you open door number one and walk inside only to set off a trap that releases a sledge hammer that crushes your skull.")
    elif number == "2":
      print("You start to open door number 2 but before you can open it you hear a click from behind it, and you suddenly fall over as your vision fades to black.")    
    elif number == "3":
      print("you open door number 3 and are suprised to see the outside wourld and when you look back the door is no longer there.")
    elif number == "4":
        print("You open door number 4 and walk inside only for the door to shut behind you and the walls start to close in on you.")
        on = input("(would you like start again or end)")
  elif player == "random":
      print("you chose random")
      a = [" pikachu"," sonic"," zeus"," ash"," tracer"," hulk"]
      a2 = [" hernia"," daiodon"," greev"," taoi"," cri"," evelent"]
      a3 = [" sandman"," browser"," joker"," silverfang"," goro"," dracula"]
      a4= [" 195"," 1,000"," 420"," 365"," 2,575"," 74"]

      print("look up in the sky thats the lost city of" +  random.choice(a2) + ".Not a lot of people know the true villian of    this tale but I was there, and I know there truename.")
      print("It was once ruled by an evil demon lord called." + random.choice(a3) + ".That demon lord was always so ruthless leaving nothing but dust in his path.")
      print("But one day a legendary hero called " + random.choice(a) + " saved them by using there god like powers to slay the demon lord.")
      print("that happended around" + random.choice(a4) + " years ago.It is a very old story that we tell our childern and hopefully they tell there's.")
      on = input("(would you like start again or end)")
  else:
      print("you tried")
  