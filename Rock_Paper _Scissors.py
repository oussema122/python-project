import random
def play():
    user = input("'r' for rock ,'p' for paper,'s' for scissors : \n")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return'It\'s atie'
    # r>s , s>p, p>r
    if is_win(user, computer):
        return 'You won' 
    return 'You lost'
    def is_win(player, opponemt):
        #return true if player wins
        # r>s , s>p, p>r
        if (player == 'r' and opponemt == 's') or (player == 's' and opponemt == 'p') or (splayer == 'p' and opponemt == 'r'):
            return True


print(play())
