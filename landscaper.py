
game = {"tool": 0, "money": 0}

tools = [
  {"name": "teeth", "profit": 1, "cost": 0 },
  {"name": "rusty scissors", "profit": 5, "cost": 5 },
  {"name": "old-lawnmower", "profit": 50, "cost": 25 },
  {"name": "fancy power lawnmower", "profit": 100, "cost": 250 },
  {"name": "team of starving students", "profit": 250, "cost": 500 }
]




#Player functions

def mow_lawn():
  tool = tools[game["tool"]]
  print(f"You have mowed the lawn with your {tool['name']} and made ${tool['profit']}")
  game["money"] += tool["profit"]


def check_stats():
  tool = tools[game["tool"]]
  print(f"You currently have ${game['money']} and are using your {tool['name']} to mow lawns")
  
  
def upgrade():
  if (game["tool"] >= len(tools) - 1):#if current tool is the last tool in list
    print("no more upgrades")#when i have done all upgrades
    return 0   
  upgraded_tool = tools[game["tool"] + 1]#the upgraded tool is the current tool +1
  
  if (game["money"] < upgraded_tool ["cost"]):
    print("You do not have enough. Keep cutting!")
    return 0
  print("You are upgrading your tool")
  game["money"] -= upgraded_tool ["cost"]# reduce your money by tool cost
  game ["tool"] += 1 #tool now = next num
  
  
def check_winner():
  if (game["tool"] == 4 and game["money"] >= 1000):
    print("Congratulations!, You win.") 
    return True #or return false
  return False

while(True):
  
    user_choice = input("[1] Mow Lawn [2] Check Stats [3] Upgrade [4] Quit")
    user_choice = int(user_choice)
    
    if(user_choice == 1):
      mow_lawn()
    
    
    if(user_choice == 2):
      check_stats()
    
    if(user_choice == 3):
      upgrade()
    
    if(user_choice == 4):
      print("You have quit the game")
      break
    
    if(check_winner()):
      break