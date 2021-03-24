import os
import time
import math


#Selects version for the clear terminal message

print("Linux(1)\n")
print("Microsoft(2)\n")
Version = ""
while not(Version in ["1", "2"]):  
  Version = input("?:")
clearmsg = ['clear', 'cls'][int(Version) - 1]


#sets up profile

class profile:
  money = 10001
  science = 0
  kerbs = 10
  Location = "SC"
turns = 0


#Checks if all kerbals are dead

def checkkerbs():

  quitthing = False
  global profile
  global clearmsg

  if profile.kerbs < 1:

    os.system(clearmsg)
    print("Whoops, All your kerbs died. \n")
    print("Get 10 More Kerbs $10000 (1)\n")
    print("Give Up (2)\n")
    while not(quitthing) and profile.kerbs < 1:

      answer = input("?:")
      if answer == "1":

        if profile.money < 10000:

          os.system(clearmsg)
          print("Not enogh money. \n")
          print("Quiting \n")
          quitthing = True

        else:

          os.system(clearmsg)
          profile.money -= 10000
          profile.kerbs += 10
          print("Turn " + str(turns) + "\n")
          print("Money: $" + str(profile.money) + "\n")
          print("Kerbs: " + str(profile.kerbs) + "\n")
          print("10 Kerbs hired for $10,000")

      elif answer == "2":

        os.system(clearmsg)
        print("Quiting \n")
        quitthing = True

    return quitthing


#Loading animation

def loading(breaktime):
  global clearmsg
  os.system(clearmsg)
  string = ""
  for j in range(10):
    os.system(clearmsg)
    for l in range(j):
      string += "-"
    for k in range(10-j):
      string += " "
    print("Loading[" + string + "]")
    string = ""
    time.sleep(breaktime)
  time.sleep(breaktime)
#finds colon
def findc(line):
  beforec = True
  beforeline = ""
  afterline = ""
  for a in line:
    if beforec and not(a==":"):
      beforeline += a
    elif beforec == False:
      afterline += a
    if a==":":
      beforec = False
  return [beforeline, afterline]
#Turn Loop
while True:
  turns += 1
  os.system(clearmsg)
  print("Turn: " + str(turns) + "\n")
  print("Money: $" + str(profile.money) + "\n")
  print("Kerbs: " + str(profile.kerbs) + "\n")
  print("Location: " + str(profile.Location) + "\n")
  checked = checkkerbs()
  if checked:
    break
  if profile.money < 1:
    os.system(clearmsg)
    print("You ran out of money. \n")
    print("quitting.")
    break

  #Space Center Options
  if profile.Location == "SC":
    print("Where do you want to go?\n")
    print("VAB(1)\n")
    print("R&D(2)\n")
    while True:
      where = input("?:")
      if where == "1":
        profile.Location = "VAB"
        break
      elif where == "2":
        profile.Location = "R&D"
        break

  #VAB Options
  elif profile.Location == "VAB":
    print("Build A New Spacecraft?\n")
    print("yes(1)")
    print("no(2)")
    while True:
      build = input("?:")
      if build == "1":
        os.system(clearmsg)
        print('select a capsule')
      elif build == "2":
        profile.Location = "SC"
        break
  turns += 1
  os.system(clearmsg)
  print("Turn: " + str(turns) + "\n")
  print("Money: $" + str(profile.money) + "\n")
  print("Kerbs: " + str(profile.kerbs) + "\n")
  print("Location: " + str(profile.Location) + "\n")
  checked = checkkerbs()
  if checked:
    break
  if profile.money < 1:
    os.system(clearmsg)
    print("You ran out of money. \n")
    print("quitting.")
    break

  #Space Center Options
  if profile.Location == "SC":
    print("Where do you want to go?\n")
    print("VAB(1)\n")
    print("R&D(2)\n")
    while True:
      where = input("?:")
      if where == "1":
        profile.Location = "VAB"
        break
      elif where == "2":
        profile.Location = "R&D"
        break

  #VAB Options
  elif profile.Location == "VAB":
    print("Build A New Spacecraft?\n")
    print("yes(1)")
    print("no(2)")
    while True:
      build = input("?:")
      if build == "1":
        totalw = 0
        totalc = 0
        os.system(clearmsg)

        #Selecting Parts


        #command modules

        cmmdmods = open('Data/Parts/Commod.txt', 'r')
        cmmdmods = cmmdmods.readlines()
        newcmdmods = []
        temp = []
        for j in cmmdmods:
          j = j.rstrip('\n')
          if j == ":":
            newcmdmods.append(temp)
            temp = []
            continue
          temp.append(j)
        counter = -1
        print("Select Command Module:\n")
        for k in newcmdmods:
          counter += 1
          print(str(k[0]) + "(" + str(counter+1) + ")\n")
        possibleopts = []
        for j in range(counter + 2):
          possibleopts.append(str(j))
        while True:
          cmmdmoda = input("?:")
          if not(cmmdmoda in possibleopts):
            continue
          if cmmdmoda == "0":
            continue
          cmmdmoda = int(cmmdmoda) - 1
          break
        os.system(clearmsg)
        totalw += float(newcmdmods[cmmdmoda][1])
        totalc += float(newcmdmods[cmmdmoda][2])
        print("Command module: " + newcmdmods[cmmdmoda][0] + "\n")
        print("mass: " + str(totalw) + " t\n")
        print("cost: $" + str(totalc) + "\n")


        #Fuel Tanks

        totalfueltanks = []
        fueltanka = ""
        counter2 = 1
        totalm = 0
        totalf = 0
        totaldm = 0
        totalco = 0
        while not(fueltanka == False):
          Fueltanks = open('Data/Parts/FuelT.txt', 'r')
          Fueltanks = Fueltanks.readlines()
          NewFuelTanks = []
          temp = []
          for j in Fueltanks:
            j = j.rstrip('\n')
            if j == ":":
              NewFuelTanks.append(temp)
              temp = []
              continue
            temp.append(j)
          counter = -1
          print("Select a fuel tank\n")
          for k in NewFuelTanks:
            counter += 1
            print(str(k[0]) + "(" + str(counter+1) + ")\n")
          print("input done to quit\n")
          possibleopts = []
          for j in range(counter + 2):
            possibleopts.append(str(j))
          fueltanka = ""
          while True:
            fueltanka = input("?:")
            if fueltanka == "done":
              break
            if not(fueltanka in possibleopts):
              continue
            if fueltanka == "0":
              continue
            fueltanka = int(fueltanka) - 1
            break
          if fueltanka == "done":
            if counter2 == 1:
              os.system(clearmsg)
              print("NO YOU NEEEEED A FUEL TANK")
              fueltanka == ""
              continue
            else:
              fueltanka = False
              continue
          os.system(clearmsg)
          totalfueltanks.append(NewFuelTanks[fueltanka])

          totalm = 0
          totalf = 0
          totaldm = 0
          totalco = 0
          totalw -= totalm
          totalc -= totalco
          for l in totalfueltanks:
            totalm += float(l[1])
          for l in totalfueltanks:
            totalco += float(l[2])
          for l in totalfueltanks:
            totaldm += float(l[3]) 
          for l in totalfueltanks:
            totalf += float(l[4])
          totalw += totalm
          totalc += totalco

          print("Command module: " + newcmdmods[cmmdmoda][0] + "\n")
          for l in totalfueltanks:
            print("Fuel Tank: " + l[0] + "\n")
          print("mass: " + str(totalw) + " t\n")
          print("cost: $" + str(totalc) + " \n")
          counter2 += 1

        #engines


        Engines = open('Data/Parts/Engine.txt', 'r')
        Engines = Engines.readlines()
        NewEngines = []
        temp = []
        for j in Engines:
          j = j.rstrip('\n')
          if j == ":":
            NewEngines.append(temp)
            temp = []
            continue
          temp.append(j)
        counter = -1
        print("Select an engine\n")
        for k in NewEngines:
          counter += 1
          print(str(k[0]) + "(" + str(counter+1) + ")\n")
        possibleopts = []
        for j in range(counter + 2):
          possibleopts.append(str(j))
        while True:
          enginea = input("?:")
          if not(enginea in possibleopts):
            continue
          if enginea == "0":
            continue
          enginea = int(enginea) - 1
          break

        #Launch equations

        totalc += float(NewEngines[enginea][2])
        totalw += float(NewEngines[enginea][1])
        twratioatm = float(NewEngines[enginea][3])/(totalw*9.8)
        DeltaV = float(NewEngines[enginea][4])*9.82*math.log(totalw/(totalw+float(totaldm)))
        while True:
          os.system(clearmsg)
          print("Command module: " + newcmdmods[cmmdmoda][0] + "\n")
          for l in totalfueltanks:
            print("Fuel Tank: " + l[0] + "\n")
          print(totaldm)
          print("Engine: " + NewEngines[enginea][0] + "\n")
          print("mass: " + str(totalw) + "\n")
          print("DeltaV: " + str(int(DeltaV)) + "\n")
          print("cost: $" + str(totalc) + "\n")
          print("TWR in the atmosphere at 100% throttle: " + str(twratioatm) + "\n")
          print("select throttle\n")
          throttle = input("%:")
          possiblethrottles = []
          for j in range(101):
            possiblethrottles.append(str(j))
          if throttle in possiblethrottles:
            break
        os.system(clearmsg)
        twratioatm = float(NewEngines[enginea][3])/(totalw*9.8)*(int(throttle)/100)
        print("Command module: " + newcmdmods[cmmdmoda][0] + "\n")
        for l in totalfueltanks:
            print("Fuel Tank: " + l[0] + "\n")
        print("Engine: " + NewEngines[enginea][0] + "\n")
        print("mass: " + str(totalw) + "\n")
        print("DeltaV: " + str(int(DeltaV)) + "\n")
        print("cost: $" + str(totalc) + "\n")
        print("TWR in the atmosphere: " + str(twratioatm) + "\n")
        print("Launch?\n")
        print("Yes(1)\n")
        print("No(2)\n")
        while True:
          Launch = input("?:")
          if Launch == "2":
            profile.Location = "SC"
            break
          elif Launch == "1":
            break
        if Launch == "2":
          break
        if twratioatm < 1.01:
          print("TWR TOO LOW\n")
          input("PRESS ENTER TO RETURN TO SC")
          profile.Location = "SC"
          break
        else:

          #Rocket Launch
          loading(0.2)
          os.system(clearmsg)
          img1 = open("Images/Image1.txt", 'r')
          raw = img1.readlines()
          for j in raw:
            print(j.rstrip('\n'))
          img1.close()
          input("Continue?(press enter)")
          os.system(clearmsg)


          #testing for landing sites

          print("You can travel to:\n")
          LandingSites = open('Data/Landing Sites/LandingLocations.txt', 'r')
          possible = []
          for a1 in LandingSites.readlines():
            a1.rstrip('\n')
            split = findc(a1)
            if int(split[1].rstrip('\n'))<DeltaV:
              possible.append(split[0])
          print(possible)
          LandingSites.close()
          input()

      elif build == "2":
        profile.Location = "SC"
        break

  #R&D Options
  elif profile.Location == "R&D":

    print("Not programmed yet")
    input("Press enter to return")
    profile.Location = "SC"