import mysql.connector as cn
import os

#====DB

db_user='root'
db_pass='123456789'

#====
def db_con_():
    db_=cn.connect(host='localhost', database="hangman", user=db_user, passwd=db_pass, charset="utf8")
    cur_=db_.cursor()
    return db_,cur_

def initial_setup():
    if os.path.exists('./core/.done')==False:
        print("Lemme setup the DB :)))")
        db=cn.connect(host='localhost',user=db_user,passwd=db_pass,charset='utf8')
        cur=db.cursor()
        cur.execute('create database hangman')
        cur.execute('use hangman')
        cur.execute('create table words (word varchar(50))')
        f=open('./core/words.txt').readlines()
        for i in f:
            cur.execute(f'insert into words values("{i.strip()}");')
        db.commit()
        db.close()
        f=open('./core/.done','w').close()
        print("Done :)"+'\n'+('='*16))
        
def filter_out(word, trash_chars):
    new_word=''
    filtered1=[]
    for i in word:
        new_word+=i
    db,cur=db_con_()
    cur.execute(f'select * from words where word like "{new_word}";')
    data=cur.fetchall()
    for i in data:
        filtered1.append(i[0])
    db.close()
    trash=[]
    for i in filtered1:
        for j in trash_chars:
            if j in i:
                trash.append(i)
    return list(set(filtered1)-set(trash))

common_chars1=['a','e', 'o','i']

def learn_word (word):
    db,cur=db_con_()
    cur.execute(f'insert into words values("{word}");')
    print("word learnt")
    db.commit()
    db.close()

def educatedguess (word, trash_chars, used_chars):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    I = 0
    J = 0
    k = 0
    l = 0
    m = 0
    n = 0
    o = 0
    p = 0
    q = 0
    r = 0
    s = 0
    t = 0
    u = 0
    v = 0
    w = 0
    x = 0
    y = 0
    z = 0
    new_word=''
    filtered1=[]
    for i in word:
        new_word+=i
    db,cur=db_con_()
    cur.execute(f'select * from words where word like "{new_word}";')
    data=cur.fetchall()
    for i in data:
        filtered1.append(i[0])
    db.close()
    var=None
    for P in filtered1:
        for K in P:
            if K in word:
                for i in word:
                    if i == K:
                        if P[word.index(K)]==K:
                            continue
                        else:
                            filtered1.pop(filtered1.index(P))
    for i in filtered1:
        for j in i:
            if j not in used_chars and j not in trash_chars:
                if j == 'a':
                    a+=1
                    var='a'
                elif j == 'b':
                    b+=1
                    var='b'
                elif j == 'c':
                    c+=1
                    var='c'
                elif j== 'd':
                    d+=1
                    var='d'
                elif j == 'e':
                    e+=1
                    var='e'
                elif j == 'f':
                    f+=1
                    var='f'
                elif j == 'g':
                    g+=1
                    var='g'
                elif j == 'h':
                    h+=1
                    var='h'
                elif j == 'i':
                    I += 1
                    var = 'i'
                elif j == 'j':
                    J += 1
                    var = 'j'
                elif j == 'k':
                    k += 1
                    var = 'k'
                elif j == 'l':
                    l += 1
                    var = 'l'
                elif j == 'm':
                    m += 1
                    var = 'm'
                elif j == 'n':
                    n += 1
                    var = 'n'
                elif j == 'o':
                    o += 1
                    var = 'o'
                elif j == 'p':
                    p += 1
                    var = 'p'
                elif j == 'q':
                    q += 1
                    var = 'q'
                elif j == 'r':
                    r += 1
                    var = 'r'
                elif j == 's':
                    s += 1
                    var = 's'
                elif j == 't':
                    t += 1
                    var = 't'
                elif j == 'u':
                    u += 1
                    var = 'u'
                elif j == 'v':
                    v += 1
                    var = 'v'
                elif j == 'w':
                    w += 1
                    var = 'w'
                elif j == 'x':
                    x += 1
                    var = 'x'
                elif j == 'y':
                    y += 1
                    var = 'y'
                elif j == 'z':
                    z += 1
                    var = 'z'
    return var



