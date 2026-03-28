def StartJamming():
    print("Welcome to the Jamming Session!")
    print("Let's create some music together.")
    print("Choose your instrument:")
    print("1. Guitar")
    print("2. Drums or Cajon")
    print("3. Keyboard")
    print("4. Bass")
    print("5. Vocals")

    
    choice = input("Enter the number of your instrument: ")
    needed_instruments= ["Enter the number of the instrument which is needed: "]
    
    if needed_instruments == "1":
        print("We need a Guitarist to join the jam!")
        print("Show all the guitarists in the community and ask them to join the jam. According to the Location")

    elif needed_instruments == "2":
        print("We need a Drummer or Cajon player to join the jam!")
        print("Show all the drummers or cajon players in the community and ask them to join the jam. According to the Location")
    
    elif needed_instruments == "3":
        print("We need a Keyboardist to join the jam!")
        print("Show all the keyboardists in the community and ask them to join the jam. According to the Location")

    elif needed_instruments == "4":
        print("We need a Bassist to join the jam!")
        print("Show all the bassists in the community and ask them to join the jam. According to the Location")

    elif needed_instruments == "5":
        print("We need a Vocalist to join the jam!")
        print("Show all the vocalists in the community and ask them to join the jam. According to the Location")

def MessageMusicians():
    print("Send a message to the musicians to request a jam.")
    print("Encourage them to bring their instruments and be ready to create some amazing music together!")
    print("We are excited to have you join the jamming session and can't wait to see the magic you create with your fellow musicians!")