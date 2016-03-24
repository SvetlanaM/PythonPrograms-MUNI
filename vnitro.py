# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 16:11:09 2014

@author: gomi
"""

'''UKOL 1'''
def test(a,b):
    if b!=0 and a%b==0:
        print str(a) + " is divisible by " + str(b)
    elif a!=0 and b%a==0:
        print str(b) + " is divisible by " + str(a)
    else:
        print str(a) + " and " + str(b) + " are comprime"
        
'''UKOL 2'''
def table(n):
    for i in range(n):
        for j in range(1,n+1):
            print j**i,
        print
        
'''UKOL 3'''
def vowels(s, t):
    sum_s = 0
    sum_t = 0    
    for x in s:
        if x in ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]: sum_s +=1
    print s, sum_s
    for y in t:
        if y in ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]: sum_t +=1
    print t, sum_t
    
    if sum_s==sum_t: return 0
    elif sum_s>sum_t: return 1
    else: return -1 
    
'''UKOL 4'''
def isPrime(num):
    result = False    
    for i in range(2,num+1):
        result = True        
        if num%i==0:
            if i!=1 and i!=num:
                result = False
                break
    return result
    
#the answer
def primes(s):
    out = []
    for x in s:
        if isPrime(x) and x not in out:
            out.append(x)
    return out
    
'''UKOL 5'''
def letter(n):
    sharpLine = n/2
    for x in range(n):
        if x == sharpLine:
            print "#"*n
        else:
            out = ""            
            for y in range(n):
                if y==0 or y==n-1:
                    out += "#"
                else:
                    out+= "."
            print out