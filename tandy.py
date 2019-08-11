from math import *
print("                                        _______________________________________")
print("                                        |!!!!!!!!!!TANDY THE CHATBOT!!!!!!!!!!|")
print("                                        |_____________________________________|")
print("MENU: ")
print("1.solve maths")
print("2.convert temperature")
print("3.calculate percentage")
print("4.end to end the program")
print("                          ")
print("enter your details to launch tandy")
name=input("enter your name: ")
age=float(input("enter your age: "))
sex=input("enter your sex: ")
country=input("enter your country: ")
state=input("enter your state: ")
print("                          ")
print("WELCOME " + name + "")
a="end"
user=""
while user!=a:
    user=input("user: ")
    if user=="hi" or user=="hello":
        print("hello " + name + "")
    elif user=="what is your work":
        print("i am a chatbot and my work is to talk with you")
    elif user=="will you be my friend":
        print("ofcourse " + name + "")
    elif user == "what do you do":
       print("i talk to people like you")
    elif user=="how are you":
        print("i am fine")
    elif user=="who are you" or user=="what is your name" or user=="whats your name":
        print("i am tandy the chatbot")
    elif user=="who is your creator" or user=="who made you" or user=="who is your inventor":
        print("my creator is aditya")
    elif user=="who is aditya" or user=="who's aditya":
        print("aditya is my creator and he is a programmer")
    elif user=="what can you do" or user=="what is your ability" or user=="what are your abilities":
        print("i can do many things whatever you want")
    elif user=="can you solve maths" or user=="are you able to perform mathematical operation":
        print("yes i can solve")
    elif user=="solve maths":
        print("provide inputs and operator")
        x=float(input("enter x: "))
        y=float(input("enter y: "))
        op = input("enter operator: ")
        if op=="+":
            print(x+y)
        elif op=="-":
            print(x-y)
        elif op=="*":
            print(x*y)
        elif op=="/":
            print(x/y)
        elif op=="**":
            print(x**y)
        else:
            print("invalid command")
    elif user=="from which country you belong to":
        print("i was made by aditya who belongs from india")
    elif user=="what you know about india":
        print("india is beautiful country full of diversity")
        print("full of beautiful people")
    elif user=="do you know about freedom fighters of india":
        print("yes i know about many freedom fighters of india who sacrificed there life for their nation")
    elif user=="can you tell me about some freedom fighters":
        print("input there name i will tell you about them")
        name=input("enter freedom fighters name: ")
        if name=="mahatma gandhi":
            print("1869-1948")
            print("mahatma gandhi is called the father of nation")
            print("he played key role in the independence of india")
            print("he is also called as bapu")
            print("he believed in non-violence")
    elif user=="what is a chatbot":
        print("a chatbot is basically a talking bot created by human to have a conversation when they feel alone or sad")
    elif user=="convert temperature":
        t1 = input("enter temp in celcius: ")
        t2=32+9*int(t1)/5
        print("your temperature in farenhite is: " + str(t2))
    elif user=="calculate percentage":
        print("PERCENTAGE OF 12th GRADE")
        no1 = input("math: ")
        no2 = input("physics: ")
        no3 = input("english: ")
        no4 = input("chemistry: ")
        no5 = input("music: ")
        total = float(no1) + float(no2) + float(no3) + float(no4) + float(no5)
        percentage = float(total) * 100 / 500
        print("total percent: " + str(percentage))
        if float(percentage) > 40:
            print("PASS")






    else:
        print("i am a baby bot and i am not so user friendly sorry for inconvinience as i am not able to understand you")
