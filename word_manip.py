"""
    word_manip module
    Author: Jingyuan_He
    2/25/2018
"""
import numpy.random as rnd

def if_terminator(str_word):
    """terminator detective
    input string
    output Bool
    """
    if '.' in str_word :
        return True
    if '!' in str_word :
        return True
    if '?' in str_word :
        return True
    return False

def sep_words(str_in):
    """spilt the sentence
    input string
    output list
    """
    list_in = str_in.split()
    list_out = []
    list_sub = []
    for word in list_in :
        #append the sub list and reset the sub list when any terminator is found
        if if_terminator(word) :
            list_sub.append(word[:-1])
            list_sub.append(word[-1:])
            list_out.append(list_sub)
            list_sub = []
            continue
        #append the word without terminator to sub list
        else :
            list_sub.append(word)
        #in case of ending without terminator
        if word == list_in[-1]:
            list_out.append(list_sub)
            
    return list_out
        
def comb_word(list_in):
    """
        reveres the effect of sep_words
        input list
        output string
    """
    stream = ''
    curr_list = []
    sbu = []
    for curr_list in list_in:
        for sub in curr_list:
            #there is no space in front of terminator
            if if_terminator(sub):
                stream = stream[:-1]            
            stream = stream + (str(sub))
            stream += ' '
    return stream


def crypto_table(n):
    """create a disorder alphabet table based on n
        input:
            n: seed of random
        output:
            swap_table: disorder alphabet
    """
    if n < 0 or n > 2000000000 :
        return None
    rnd.seed(n)
    rnd_table = rnd.random(26)
    swap_table = []
    n = 0
    low_c = ord('a')
    up_c = ord('A')
    while n < 26:
        swap_table.append((rnd_table[n],chr(low_c+n),chr(up_c+n)))
        n += 1
    swap_table = sorted(swap_table, key=lambda x : x[0])
    return swap_table


def encode(x,table):
    """return a list containing encode word
        x is a list of words
    """
    #encode words with disorder alphabet
    cryp_code = ""
    asc = 0
    low_c = ord('a')
    up_c = ord('A')
    for walk in x:        
        asc = ord(walk)
        diff1 = asc - low_c
        diff2 = asc - up_c
        #search the encode characters by index
        if (diff1 >= 0) and (diff1 < 26):
            cryp_code += (table[diff1][1])
        elif (diff2 >= 0) and (diff2 < 26):
            cryp_code += (table[diff2][2])
        else:
            cryp_code += (walk)
    return cryp_code

def search(ch,table):
    """
        search the index in the table
    """
    n = 0
    while n < len(table):
        if ch in table[n]:
            return n
        n += 1
    return None
       
    
def decode(x,table):
    """return a list containing decode word
        x is a list of words
    """
    #decode words with disorder alphabet
    origin_code = ""
    asc = 0
    index = 0
    low_c = ord('a')
    up_c = ord('A')
    for walk in x:        
        asc = ord(walk)
        diff1 = asc - low_c
        diff2 = asc - up_c
        #search the decode characters by index
        if (diff1 >= 0) and (diff1 < 26):
            index = search(walk,table)
            origin_code += (chr(low_c+index))
        elif (diff2 >= 0) and (diff2 < 26):
            index = search(walk,table)
            origin_code += (chr(up_c+index))
        else:
            origin_code += (walk)
    return origin_code
    
def crypto(x,n,enc):
    """input:
    x: a list of words
    n: integer in the range 0 to 2,000,000,000
    enc : Boolean value. True:code / False:decode
    """
    table = crypto_table(n)
    list_out = []
    if enc == True:
        for word in x:
            list_out.append(encode(word,table))
        return list_out
    else:
        for word in x:
            list_out.append(decode(word,table))
        return list_out
        
    
