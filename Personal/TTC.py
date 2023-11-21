while True:
    print()
    print()
    print()
    print("1: report an incident")
    print("2: view current incidents")
    while True: 
        try:  
            mode = int(input("Would you like to report an incident or view current incidents? "))
            if mode==1 or mode==2:
                break
            else:
                print("Please only input 1 (to report) or 2(to view)")
                print()
        except ValueError:
            print("Please enter a number")
    print()
    violence_stations = []
    violence_discriptions = []
    verbal_stations = []
    verbal_discriptions = []
    other_stations = []
    other_discriptions = []

    while True:
        if mode==1:
            print("1: violence")
            print("2: verbal abuse")
            print("3: other")
            try:
                report = int(input("what do you want to input? "))
                if report==1:
                    violence_stations.append(input("What station would you like to report violence at? "))
                    violence_discriptions.append(input("discribe the violence please: "))
                    break
                elif report==2:
                    verbal_stations.append(input("What station would you like to report verbal abuse at? "))
                    verbal_discriptions.append(input("discribe the verbal abuse please: "))
                    break
                elif report==3:
                    other_stations.append(input("What station would you like to report other at? "))
                    other_discriptions.append(input("discribe the other please: "))
                    break
                else:
                    print("Please enter either 1, 2, or 3")
            except ValueError:
                print("Please enter a number")
    
    if mode==2:
        for i in range (len(violence_stations)):
            print(f"The first violence was reported at {violence_stations[i]}. It was described as: {violence_discriptions[i]}")
        for i in range (len(verbal_stations)):
            print(f"The first verbal abuse was reported at {verbal_stations[i]}. It was described as: {verbal_discriptions[i]}")
        for i in range (len(other_stations)):
            print(f"The first other abuse was reported at {other_stations[i]}. It was described as: {other_discriptions[i]}")