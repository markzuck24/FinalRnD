# coding=utf-8

from nltk.tokenize import word_tokenize
from nltk.translate.bleu_score import sentence_bleu

import os
import time
import nltk

# a = [1,2,3,4,5]
# for i in a:
#     f = open("s.txt", "a")
#     f1 = open("s1.txt", "a")
#     f2 = open("s2.txt", "a")
#     f3 = open("s3.txt", "a")
    
#     ss = str(i)+"\n"
#     f.write(ss)
#     f1.write(ss)
#     f2.write(ss)
#     f3.write(ss)
    
#     time.sleep(2)
#     fname = str(i)+'.txt'
#     os.system("perl blu.pl r.txt < %s" % (fname))
#     os.system("perl blu1.pl r.txt p1.txt < %s" % (fname))
#     os.system("perl blu2.pl r.txt p1.txt p2.txt < %s" % (fname))
#     os.system("perl blu3.pl r.txt p1.txt p2.txt p3.txt < %s" % (fname))
#     time.sleep(1)



r = open('/home/adi/Videos/FinalRnD/paraphrased files for WMT14/cs-en/r.txt', 'r') 
Lines = r.readlines() 
r1=[]
for line in Lines:
    l1 = []
    l1 =  word_tokenize(line)
    r1.append(l1)

f = open("/home/adi/Videos/FinalRnD/paraphrased files for WMT14/cs-en/tokens/r.txt","w")
f.write(str(r1))



p1 = open('/home/adi/Videos/FinalRnD/paraphrased files for WMT14/cs-en/p1.txt', 'r') 
Lines = p1.readlines() 
r2=[]
for line in Lines:
    l1 = []
    l1 =  word_tokenize(line)
    r2.append(l1)

f = open("/home/adi/Videos/FinalRnD/paraphrased files for WMT14/cs-en/tokens/p1.txt","w")
f.write(str(r2))




p2 = open('/home/adi/Videos/FinalRnD/paraphrased files for WMT14/cs-en/p2.txt', 'r') 
Lines = p2.readlines() 
r3=[]
for line in Lines:
    l1 = []
    l1 =  word_tokenize(line)
    r3.append(l1)

f = open("/home/adi/Videos/FinalRnD/paraphrased files for WMT14/cs-en/tokens/p2.txt","w")
f.write(str(r3))


p3 = open('/home/adi/Videos/FinalRnD/paraphrased files for WMT14/cs-en/p3.txt', 'r') 
Lines = p3.readlines() 
r4=[]
for line in Lines:
    l1 = []
    l1 =  word_tokenize(line)
    r4.append(l1)

f = open("/home/adi/Videos/FinalRnD/paraphrased files for WMT14/cs-en/tokens/p3.txt","w")
f.write(str(r4))


a = [1,2,3,4,5]
for i in a:
    f = open("s.txt", "a")
    f1 = open("s1.txt", "a")
    f2 = open("s2.txt", "a")
    f3 = open("s3.txt", "a")
    o = open('/home/adi/Videos/FinalRnD/paraphrased files for WMT14/cs-en/'+str(i)+'.txt', 'r') 
    Lines = o.readlines() 
    c=[]
    for line in Lines:
        l1 = []
        l1 =  word_tokenize(line)
        c.append(l1)

    o = open("/home/adi/Videos/FinalRnD/paraphrased files for WMT14/cs-en/tokens/"+str(i)+".txt","w")
    f.write(str(o))

    weights = (0.4,0.3,0.2,0.1)

    ref=[r1]
    ref1=[r1,r2]
    ref2=[r1,r2,r3]
    ref3=[r1,r2,r3,r4]

    bleu = nltk.translate.bleu_score.corpus_bleu(ref,c,weights)
    bleu1 = nltk.translate.bleu_score.corpus_bleu(ref1,c,weights)
    bleu2 = nltk.translate.bleu_score.corpus_bleu(ref2,c,weights)
    bleu3 = nltk.translate.bleu_score.corpus_bleu(ref3,c,weights)

    ss = str(i)+"\n"
    f.write(ss)
    f1.write(ss)
    f2.write(ss)
    f3.write(ss)
    time.sleep(2)
    f.write(bleu*100)
    f1.write(bleu1*100)
    f2.write(bleu2*100)
    f3.write(bleu3*100)
    print ("\nBLEU score with single Reference sentence = ", bleu*100)
    print ("BLEU score with one extra Reference sentence = ", bleu1*100)
    print ("BLEU score with two extra Reference sentences = ", bleu2*100)
    print ("BLEU score with three extra Reference sentences = ", bleu3*100)











# p1 = open('/home/adi/Videos/FinalRnD/paraphrased files for WMT14/cs-en/p1.txt', 'r') 
# p1 = open('/home/adi/Videos/FinalRnD/paraphrased files for WMT14/cs-en/p1.txt', 'r') 
# r = open('/home/adi/Videos/FinalRnD/paraphrased files for WMT14/cs-en/r.txt', 'r') 


# a = [1,2,3,4,5]
# for i in a:
#     file1 = open('/home/adi/Videos/FinalRnD/paraphrased files for WMT14/cs-en/'+str(i)+'.txt', 'r') 
#     file2 = open('/home/adi/Videos/FinalRnD/bleu site/WMT 14 references', 'r') 
#     Lines = file1.readlines() 
    
  
#     l2=[]
    
#     for line in Lines:
#         l1 = []
#         l1 =  word_tokenize(line)
#         l2.append(l1)


# c= word_tokenize(rpl2)
# r1= word_tokenize(rl2)
# r2= word_tokenize(p1l2)
# r3= word_tokenize(reference3)
# r4= word_tokenize(reference4)

# weights = (0.4,0.3,0.2,0.1)

# ref=[r1]
# ref1=[r1,r2]
# ref2=[r1,r2,r3]
# ref3=[r1,r2,r3,r4]

# bleu = sentence_bleu(ref,c,weights)
# bleu1 = sentence_bleu(ref1,c,weights)
# bleu2 = sentence_bleu(ref2,c,weights)
# bleu3 = sentence_bleu(ref3,c,weights)

# print ("\nBLEU score with single Reference sentence = ", bleu*100)
# print ("BLEU score with one extra Reference sentence = ", bleu1*100)
# print ("BLEU score with two extra Reference sentences = ", bleu2*100)
# print ("BLEU score with three extra Reference sentences = ", bleu3*100)

# print ("\n")

# Using readlines() 


# print(l2)

