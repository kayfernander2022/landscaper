
game = {"tool": 0, "money": 0}

tools = [
  {"name": "teeth", "profit": 1, "cost": 0 }
]



#Player functions

def mow_lawn():
  tool = tools[game["tool"]]
  print(f"You have mowed the lawn with your {tool['name']} and made ${tool['profit']}")
  game["money"] += tool["profit"]


def check_stats():
  tool = tools[game["tool"]]
  print(f"You currently have ${game['money']} and are using your {tool['name']} to mow lawns")

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