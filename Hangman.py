# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 21:02:56 2024

@author: ilknu
"""
print("\n")
print("           _")
print("          | |                                        ")
print("          | |__  _ _ _ _  _   _ _  _ _ _ _ _ _ _ _ _ _  _  ")
print("          | '_ \|   _  | '_ \/  _   | '_ ' _  \/ _' | '_  \ " )
print("          | | | |  (_| | || |  (_|  | | | | | | (_| | | | |")
print("          |_| |_|\_ _,_|_||_|\_ _,  |_| |_| |_|\__,_|_| |_|")
print("                              _ _/  |       ")
print("                             |_ _ _/           ")
print("                                     ")

def adam():
    print("\n")
    print("                             +_____+     ")
    print("                             |     |  ")
    print("                                   |")
    print("                                   |")
    print("                                   |")
    print("                                   |")
    print("                              _____|")


def adam1():
    print("\n")
    print("                             +_____+     ")
    print("                             |     |  ")
    print("                             O     |")
    print("                                   |")
    print("                                   |")
    print("                                   |")
    print("                              _____|")


def adam2():
    print("\n")
    print("                             +_____+     ")
    print("                             |     |  ")
    print("                             0     |")
    print("                             |     |")
    print("                                   |")
    print("                                   |")
    print("                              _____|")

def adam3():
    print("\n")
    print("                             +_____+     ")
    print("                             |     |  ")
    print("                             0     |")
    print("                             |\    |")
    print("                                   |")
    print("                                   |")
    print("                              _____|")

def adam4():
    print("\n")
    print("                             +_____+     ")
    print("                             |     |  ")
    print("                             0     |")
    print("                            /|\    |")
    print("                                   |")
    print("                                   |")
    print("                              _____|")

def adam5():
    print("\n")
    print("                             +_____+     ")
    print("                             |     |  ")
    print("                             0     |")
    print("                            /|\    |")
    print("                                   |")
    print("                                   |")
    print("                              _____|")

def adam6():
    print("\n")
    print("                             +_____+     ")
    print("                             |     |  ")
    print("                             0     |")
    print("                            /|\    |")
    print("                            /      |")
    print("                                   |")
    print("                              _____|")

def adam7():
    print("\n")
    print("                             +_____+     ")
    print("                             |     |  ")
    print("                             0     |")
    print("                            /|\    |")
    print("                            / \    |")
    print("                                   |")
    print("                              _____|")

x="ilknur"
x.islower()
count=0
l=[]
for _ in range(len(x)):
    l.append("_")
func=[adam1,adam2,adam3,adam4,adam5,adam6,adam7]
adam()
s=""
while True:
    for _ in l:
        print(_,end=" ")
    if s.join(l)==x:
        print("\nYou win")
        break

    print("\nGues a letter: ")
    enter_letter=input()
    enter_letter.islower()
    if len(enter_letter) == 1:
        if enter_letter in x:
            for i in range(len(x)):
                if x[i]==enter_letter:
                    l[i]=enter_letter
        else:
            count +=1
            print(f"your letter is {enter_letter}, and you lost live.")
            y=func[count-1]
            y()
    if count == 7:
        print(" You lost")
        break
    if count<7 and l == x.split():
        print("You win")
        break
    

    
                
                    
