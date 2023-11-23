from random import randint

def load_bad_foodlines():
  #Take input from touch lines from ChatGPT
  inputFile = open("../TermiText/lines.txt")
  badLineList = []
  for line in inputFile:
    voice = line.split("\n")
    badLineList.append(voice[0])
  return badLineList

def load_touch_lines():
  #Take input from bad food lines from ChatGPT
  inputFile = open("../TermiText/lines.txt")
  lineList = []
  for line in inputFile:
    voice = line.split("\n")
    lineList.append(voice[0])
  return lineList

def load_good_foodlines():
  # Take input from good food lines from ChatGPT
  inputFile = open("TermiText/goodFood.txt")
  goodLineList = []
  for line in inputFile:
    voice = line.split("\n")
    goodLineList.append(voice[0])
  return goodLineList

def load_toy_reactions():
  # Take input from toy reactions from ChatGPT
  inputFile = open("../TermiText/toy_react.txt")
  toyList = []
  for line in inputFile:
    voice = line.split("\n")
    toyList.append(voice[0])
  return toyList
def output_lines(voicelines):
  randIndex = randint(0, len(voicelines) - 1);
  print(voicelines[randIndex])

#Food Menu
def foodMenu():
  print("Today's Menu (Best Prices): ")
  randomPrices = []
  for i in range(10):
    randomPrices.append(randint(40,1000))
  print("1. Chowder $" + str(randomPrices[0]))
  print("2. Salad   $" + str(randomPrices[1]))
  print("3. Pudding $" + str(randomPrices[2]))
  print("4. Shrimp  $" + str(randomPrices[3]))
  print("5. Fish    $" + str(randomPrices[4]))
  print("6. Chicken $" + str(randomPrices[5]))
  print("7. Apple   $" + str(randomPrices[6]))
  print("8. Grass   $" + str(randomPrices[7]))
  print("9. Insect  $" + str(randomPrices[8]))
  print("10.Bamboo  $" + str(randomPrices[9]))
  chooseItem = "M"
  while(chooseItem != "q"):
    chooseItem = input("Please enter your choice literally from the menu").lower()
    if chooseItem == "chowder":
      break
    elif chooseItem == "salad":
      break
    elif chooseItem == "pudding":
      break
    elif chooseItem == "shrimp":
      break
    elif chooseItem == "fish":
      break
    elif chooseItem == "chicken":
      break
    elif chooseItem == "apple":
      break
    elif chooseItem == "grass":
      break
    elif chooseItem == "insect":
      break
    elif chooseItem == "bamboo":
      break
    else:
      print("Hey, where's my food, hooman? Meow!")
  print()
  print("Cat's Rating:")
  if randint(0,10) % 2 == 1:
    output_lines(load_good_foodlines())
    print("It was well worth it!! :)")
  else:
    output_lines(load_bad_foodlines())
    print("The food sucks :(")
  print()

def itemMenu():
  print("Gifts for the Cat Who Rules")
  randomPrices = []
  for i in range(10):
    randomPrices.append(randint(500,9000))
  print("1. Feather wand toy $" + str(randomPrices[0]))
  print("2. Wind up mouse   $" + str(randomPrices[1]))
  print("3. Scratching post $" + str(randomPrices[2]))
  print("4. Kibble  $" + str(randomPrices[3]))
  print("5. Cat Tower    $" + str(randomPrices[4]))
  print("6. Soft Spread $" + str(randomPrices[5]))
  print("7. Disco Laser   $" + str(randomPrices[6]))
  print("8. LG 50in Class 4K UHD SmartTV   $" + str(randomPrices[7]))
  print("9. iPhone 12  $" + str(randomPrices[8]))
  print("10.Stuffed Bear  $" + str(randomPrices[9]))
  chooseItem = "M"
  while(chooseItem != "q"):
    chooseItem = input("Please enter your choice literally: ").lower()
    if chooseItem == "feather wand toy":
      break;
    elif chooseItem == "wind up mouse":
      break
    elif chooseItem == "scratching post":
      break
    elif chooseItem == "kibble":
      break
    elif chooseItem == "cat tower":
      break
    elif chooseItem == "soft spread":
      break
    elif chooseItem == "disco laser":
      break
    elif chooseItem == "lg 50in class 4k uhd smarttv":
      break
    elif chooseItem == "iphone 12":
      break
    elif chooseItem == "stuffed bear":
      break
    else:
      print("Oak's words echoed... There's a time and place for everything...")
      str_out = ""
      print()

  print()
  print("Feline Gear Grading:")
  print(output_lines(load_toy_reactions()))
  print()

#fix bool flag for when cat is touched: used to give normal reactions
boole = 0
cmd = "sudo"
while cmd != "quit":
  if boole == 1:
    print()
    print("Cat Reacts:")
    output_lines(load_touch_lines())
    print()
  print("[[Hint type --help to find out what commands to use & type exit to end program...]]")
  cmd = input("tm@Termies-Friend-01 ~ % |").lower()
  if cmd == "--help":
    print()
    print("Possible Commands:")
    print("1. <--help>: to show list of possible commands")
    print("2. <quit>: Exit program")
    print("3. <cd food menu>: Enter Food Menu")
    print("4. <cd item menu>: Enter Item Menu")
    print()
  elif cmd == "quit":
    print()
    break;
  elif cmd == "cd food menu":
    foodMenu()
    print()
  elif cmd == "cd item menu":
    itemMenu()
    print()
  else:
    print("zsh: command not found: " + cmd)
exit()




