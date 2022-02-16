from random import choice

with open("liste_francais.txt", "r") as tf:
    lines = tf.read().split(',')


def look_for_letter(s:str, letter:str)-> list | None:
    occurrences = []
    for i, car in enumerate(s.upper()):
        if car == letter.upper():
            occurrences.append(i)
    if occurrences:
        return occurrences
    else:
        return None



#!---- THE GAME ----!

start = str(input('Do you want to start the game ? (YES or NO) '))
if start.upper() != 'YES':
    print('Bye ! ')

else :
    print('Good luck ! :D ')

    mystery_word : str =  choice(lines)
    find = False
    list_bad_letter : list = []
    list_good_letter : list = []
    trials = 10
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    mwtf = ''
    for l in mystery_word:
        mwtf += '_'
    
    while True:
        print('#'*50)
        if trials == 10:
            pass
        elif trials == 9:
            print(' ____' + '\n' + '/    \ ')
        elif trials == 8:
            print('   |' + '\n' + '   |' + '\n' + '   |' + '\n' + '   |' + '\n' + '   |' + '\n' +' __|__' + '\n' + '/     \ ')
        elif trials == 7:
            print('   +-------+' + '\n' +'   |' + '\n' + '   |' + '\n' + '   |' + '\n' + '   |' + '\n' + '   |' + '\n' +' __|__' + '\n' + '/     \ ')
        elif trials == 6:
            print('   +-------+' + '\n' +'   |       |' + '\n' + '   |' + '\n' + '   |' + '\n' + '   |' + '\n' + '   |' + '\n' +' __|__' + '\n' + '/     \ ')
        elif trials == 5:
            print('   +-------+' + '\n' +'   |       |' + '\n' + '   |       O' + '\n' + '   |' + '\n' + '   |' + '\n' + '   |' + '\n' +' __|__' + '\n' + '/     \ ')
        elif trials == 4:
            print('   +-------+' + '\n' +'   |       |' + '\n' + '   |       O' + '\n' + '   |       |' + '\n' + '   |' + '\n' + '   |' + '\n' +' __|__' + '\n' + '/     \ ')
        elif trials == 3:
            print('   +-------+' + '\n' +'   |       |' + '\n' + '   |       O' + '\n' + '   |      /|' + '\n' + '   |' + '\n' + '   |' + '\n' +' __|__' + '\n' + '/     \ ')
        elif trials == 2:
            print('   +-------+' + '\n' +'   |       |' + '\n' + '   |       O' + '\n' + '   |      /|\ ' + '\n' + '   |' + '\n' + '   |' + '\n' +' __|__' + '\n' + '/     \ ')
        elif trials == 1:
            print('   +-------+' + '\n' +'   |       |' + '\n' + '   |       O' + '\n' + '   |      /|\ ' + '\n' + '   |      / ' + '\n' + '   |' + '\n' +' __|__' + '\n' + '/     \ ')
        elif trials == 0:
            print('   +-------+' + '\n' +'   |       |' + '\n' + '   |       O' + '\n' + '   |      /|\ ' + '\n' + '   |      / \ ' + '\n' + '   |' + '\n' +' __|__' + '\n' + '/     \ ')
            break
        print('Letter proposed : ', list_good_letter + list_bad_letter)
        if mystery_word == mwtf:
            break
        print('Mysterious word to find :' + mwtf)
        ask_letter = str(input('Submit a letter : '))
        
        

        if ask_letter.upper() in mystery_word and ask_letter.upper() not in list_good_letter:
            list_good_letter.append(ask_letter.upper())
            l= look_for_letter(mystery_word,ask_letter)
            l1 = list(mwtf)
            for elt in l:
                l1[elt] =ask_letter.upper()
                mwtf = "".join(l1)

        elif ask_letter.upper() not in mystery_word and ask_letter.upper() not in list_bad_letter:
            list_bad_letter.append(ask_letter.upper())
            trials -= 1
        elif ask_letter.upper() in list_bad_letter and ask_letter.upper() in list_good_letter:
            print('Letter already proposed ! ')

        

    if trials == 0:
        print('mysterious word was : ', mystery_word)
        print('GAME OVER ! ')
    else:
        print('mysterious word was : ', mystery_word)
        print('Well play, you won ! :D' )


