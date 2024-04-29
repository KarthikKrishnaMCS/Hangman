from core.dbcon import *
from core.gui import *
import random

def cls(): print ("\n"*100)
#=======
def pc_human():
    a_chars=[]
    lives_lost=0
    db,cur=db_con_()
    cur.execute('select * from words')
    data=cur.fetchall()
    word=data[random.randint(0,len(data))] [0]
    db.close()
    word_=list('_'*len(word))
    while lives_lost<8:
        cls()
        print(lifelost(lives_lost))
        ltr=human_pc_gameplay1(word_,lives_lost,a_chars) [0]
        if ltr not in a_chars:
            a_chars.append(ltr)
        if ltr in word:
            for i in range(0, len (word)):
                if word[i]==ltr:
                    word_[i]=ltr
        else:
            lives_lost+=1
        if word_==list(word):
            human_pc_game_win(True, word, lives_lost)
            break
        if lives_lost==8:
            cls()
            lifelost(lives_lost)
            human_pc_game_win(False, word, lives_lost)
def human_pc():
    lives_lost=0
    used_chars=[]
    unused_chars=[]
    char_var=0
    #====
    word_length=int(get_no_letters()[0])
    word = list('_'*word_length)
    def get_rnd_char(char_var):
        if char_var<4:
            char=random.choice(common_chars1)
        else:
            char=educatedguess (word, unused_chars, used_chars)
        return char
    while lives_lost<8:
        cls()
        print(lifelost(lives_lost))
        rnd_char=get_rnd_char(char_var)
        if rnd_char in used_chars: continue
        char_var+=1
        used_chars.append(rnd_char)
        wrd_txt=f'Is {rnd_char} present in the word? (Y/N)'
        a,b=game_play(word,wrd_txt) #gets postion too :))
        if b==True:
            for i in a:
                word[i-1]=rnd_char
            word_list=filter_out(word, unused_chars)
            if len(word_list)==1:
                human_pc_game_win(True,word_list[0], lives_lost, 'I')
                break
        else:
            unused_chars.append(rnd_char)
            lives_lost+=1
        if lives_lost==7:
            cls()
            print(lifelost(lives_lost))
            word_list=filter_out(word, unused_chars)
            if len(word_list)>0:
                c=game_play_word_check(word_list[0])[0]
                if c.lower()=='y':
                    human_pc_game_win(True,word_list[0], lives_lost, 'I')
                    break
                else:
                    lives_lost+=1
                    break
    if lives_lost==8:
        cls()
        print(lifelost(lives_lost))
        c_word=human_pc_game_win(False, word, lives_lost, 'I')
        if c_word!=[]:
            learn_word(c_word[0])



