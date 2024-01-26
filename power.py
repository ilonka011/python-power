def get_colors():
  pretty_color = 'pink'
  ugly_color = 'purple'

  return ugly_color + ' ' + pretty_color

colors = get_colors()
print(colors)

def get_choices():
  player_choice = input('Enter a choice (rock, paper, scissors): ')
  computer_choice = input('Enter a choice (rock, paper, scissors): ')
  choices = {'playr': player_choice, 'computer': computer_choice}

  return choices

get_choices()
