from random import randint
from time import time

alpha = 'abcdefghijklmnopqrstuvwxyz'
def random_string(nchars):
    answer = ''
    for i in range(nchars):
        answer += alpha[randint(0,25)]
    return answer

# create 100,000 4-char random strings and compute the number of unique ones that you see
def answery():
    start = time()
    big_dic = {}
    answers = []
    for i in range(100000): 
        astring=random_string(4)
        # your code here
        try:
            big_dic[astring] += 1 
        except:
            big_dic[astring] = 0
            answers.append(astring)
            
    return len(answers), time() - start


    
