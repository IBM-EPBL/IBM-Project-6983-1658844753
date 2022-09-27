import random
threshold = int(input("Enter Threshold Temperature(Range 0,50):"))
a=1
while(a==1):
    val=random.randint(0,50)
    print("Random Temperature: ",val)
    valh = random.randint ( 0, 200)
    print ( "Random humidity: ", valh )
    if val>threshold:
        print("Random Temp:",val,"higher than",threshold,"(Threshold Temperature)")
        print("Alarm activated")
    elif threshold>val:
        print("Random Temp:",val,"less than",threshold,"(Threshold Temperature)")
    else:
        print("Random Temp:",val,"equals to",threshold,"(Threshold Temperature)")
    a=1