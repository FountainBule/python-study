import sys
my_path = "C:/Users/he0871"
sys.path.append(my_path)
import word_manip as wm
import numpy.random as rnd

#read file
source_file = open('C:/Users/he0871/homework3_data.txt','r')
MyWord = source_file.read()

WordList = wm.sep_words(MyWord)

#initialization and chose a random integer
encrypto = ""
seed = round(2000000000 * rnd.rand())
EncodeList = []
DecodeList = []
#encode
for sentence in WordList :
    EncodeList.append(wm.crypto(sentence,seed,True))

 
encrypto = wm.comb_word(EncodeList)

code_list = wm.sep_words(encrypto)

for sentence in code_list :
    DecodeList.append(wm.crypto(sentence,seed,False))


interpret = wm.comb_word(DecodeList)

"""
write result into file
"""
def file_write(str_in, file):
    n = 60
    while n < len(str_in) :
        str_in = str_in[:n-1] + '\n' + str_in[n-1:]
        n += 60
    file.write(str_in)
    
fo = open(my_path + "\H3.5_output.txt", "w")
file_write(MyWord, fo)
fo.write('\n\n')
fo.write(str(seed))
fo.write('\n\n')
file_write(encrypto,fo)
fo.write('\n\n')
file_write(interpret,fo)
fo.close()




