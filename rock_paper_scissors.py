from random import*
# !--- FUNCTION WHO CHECK IF PLAYER WIN OR NOT ---!
def validity(a: str,b: str) -> bool: # a = player
    if a.upper() == 'ROCK' and b.upper() == 'SCISSORS' :
        return True
    elif a.upper() == 'PAPER' and b.upper() == 'ROCK':
        return True
    elif a.upper() == 'SCISSORS' and b.upper() == 'PAPER':
        return True
    else:
        return False


# !--- THE GAME ---!
start = str(input("Do you want start the game ? (YES or NO) "))

if start.upper() != 'YES': #if you don't want to play anymore
    print('Bye !')

else:
    print('Good luck ! :D')
    bo = int(input('BO : ')) 
    
    counter = [0,0]
    list_r_p_s = ["Rock","Paper","Scissors"]
    print('#'*50)
    answer = str(input('Choose between: Rock, Paper, Scissors = '))
    answer_ennemie = choice(list_r_p_s)
    if bo %2 == 0:
        a = bo/2 +1
    else:
        a = bo//2 +1

    while counter[0] <= a-1 and counter[1] <= a-1:
        print('#'*50)
        if validity(answer,answer_ennemie):
            print('Nice answer !')
            counter[0]+=1
            print(counter)
        elif not validity(answer,answer_ennemie):
            print('Bad answer !')
            counter[1]+=1
            print(counter)

        if counter[0] == a:
            print('#'*50)
            print('Well play, you won !')
            print(counter)
            break
        elif counter[1] == a:
            print('#'*50)
            print('GAME OVER ! ')
            print(counter)
            break

        print('#'*50)
        answer = str(input('Choose between: Rock, Paper, Scissors = '))
        answer_ennemie = choice(list_r_p_s)
        
