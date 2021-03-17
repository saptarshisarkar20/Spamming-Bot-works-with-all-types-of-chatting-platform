from pynput import keyboard
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


def paste_txt():
    """function to paste somthing        
    useful for printing emojis"""
    keyboard.press(Key.ctrl)
    keyboard.press("v")
    keyboard.release("v")
    keyboard.release(Key.ctrl)

def paste_txt_send():
    """function to paste somthing        
    useful for printing emojis"""
    keyboard.press(Key.ctrl)
    keyboard.press("v")
    keyboard.release("v")
    keyboard.release(Key.ctrl)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def paste_txt_n_send(n=0,t=0.1):
    """it useage the paste function 
    to paste and also send the msg"""
    for _ in range(n):
        paste_txt()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print(f"Sent {_+1} times", end="\r")
        time.sleep(t)


def send_n_inc(s1=" ", s2=" ", n=0, t=0.1):
    """takes s1 which is static for every line
    then every line increse s2 by the line no
    max n times it runs"""
    for j in range(n):
        for ltr in s1:
            keyboard.press(ltr)
            keyboard.release(ltr)
        for i in range(j):
            for ltr in s2:
                keyboard.press(ltr)
                keyboard.release(ltr)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print(f"Sent {j} times", end="\r")
        time.sleep(t)


def type_txt(ss):
    '''function for typing a 
    long paragraph
    passes argument should be in string format or a variable'''
    keyboard.type(ss)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def next_line():
    '''it is used for seding a 
    nicely formatted multi line paragraph'''
    keyboard.press(Key.shift)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.release(Key.shift)


def repeated_typing_in_next_line(ss, n=0):
    """It takes the msg as input and
    repeat the msg in same line"""
    for _ in range(n):
        keyboard.type(ss)
        next_line()
        time.sleep(0.1)


def repeated_typing_in_same_lines(ss, n=0):
    """It takes the msg as input and
    repeat the msg in same line"""
    for _ in range(n):
        keyboard.type(ss)
        keyboard.type(" ")
        time.sleep(0.1)


def type_paragrah_para_wise(para, n=1):
    '''it takes a long paragrph and 
    send it paragraph by 
    paragraph in a msg'''
    for _ in range(n):
        keyboard.type(para)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.15)


def type_paragrah_lbl_wise(para):
    '''it takes a long paragrph and 
    send it line by 
    line in a msg'''
    ck = 0
    for ltr in para:
        if(ltr == '.'):
            ck = ck + 1
        elif(ck == 1):
            ck = 0
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        elif(ck != 1):
            ck = 0
        keyboard.press(ltr)
        keyboard.release(ltr)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def send_repet(ss, n=0):
    """send a message n times"""
    for _ in range(n):
        for ltr in ss:
            keyboard.press(ltr)
            keyboard.release(ltr)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.1)


def timer_clock(t):
    """takes time input from main and behave such"""
    time.sleep(0.5)
    print("\nTime ⏱  Starts Now....\n")
    for i in range(t, 0-1, -1):
        if(i % 2 == 0):
            print(f"Time left : {i} sec ⏳ ", end="\r")
        else:
            print(f"Time left : {i} sec ⏰ ", end="\r")
        time.sleep(1)
    print("\n")
    print("Time ends 💣 \n\n")


def operations(n=0, cnt=0, msg="", msg2="",l=[],t=0.1):
    """performs the main operation"""
    if(n == 1):
        for l in range(cnt):
            type_txt(msg)
            print(f"Sent {l+1} times", end="\r")
            time.sleep(t)
        print(f"Sent {cnt} times")
    elif(n == 2):
        for l in range(cnt):
            keyboard.type(msg)
            keyboard.type(" ")
            print(f"Typed {l+1} times", end="\r")
            time.sleep(t)
        print(f"Typed {cnt} times")
    elif(n == 3):
        paste_txt_n_send(cnt,t)
        print(f"Sent {cnt} times", )
    elif(n == 4):
        for l in range(cnt):
            paste_txt()
            keyboard.type(" ")
            print(f"Pasted {l+1} times", end="\r")
            time.sleep(t)
        print(f"Pasted {cnt} times", )
    elif(n == 5):
        send_n_inc(msg, msg2, cnt, t)
        print(f"Sent {cnt} times")
    elif(n == 6):
        rep_msg_rep_ln(cnt,l,t)
        print(f"sent {cnt} times")


def bg_instructions():
    """print the instraction to be displayed in the begning"""
    print("🤖 Spammer is Activated 😈")
    print("\n\n Here are The Instructions --> \n Press the following numbers to activate the function...\n")
    print("1 : Send a text message repeated times. ")
    print("2 : Type same messsage repeated times.")
    print("3 : Paste & send a message repeated times.")
    print("4 : Paste a message repeated time. ")
    print("5 : Send & increase a part of the message repeated time.")
    print("6 : Send a multiple msg in different lines repeated times.")
    # print("7 : Send a long paragraph line by line. \n\n")


def rep_msg_rep_ln(cnt,l,t=0.1):
    '''send text messages in repeated lines'''
    for i in range(0, cnt):
        for ltr in l:
            if(ltr == "pstPP"):
                paste_txt_send()
            else:
                type_txt(ltr)
        print(f"sent {i+1} times", end="\r")
        time.sleep(t)


# time.sleep(5)
if __name__ == "__main__":
# declaration part
    msg=""
    msg2=""
    l=[]
    cnt=0
    n=0
    time_t=5
    latency_t=0
# fist instractions
    bg_instructions()
# choosing part
    print("\n")
    n = int(input("Enter Your choice : "))
    print("\n")
# msg input part
    if(n != 3 and n != 4 and n != 6):
        msg = input("Enter Your Message : ")
    if(n == 5):
        msg2 = input("Enter increasing part of your message : ")
# code to send multiple line msg
    if(n == 6):
        n6 = int(input("How many msg you want to send  : "))
        l = []
        for i in range(0, n6):
            sn = input(f"Enter {i+1}th msg (\"pstPP\" for paste) : ")
            sn = str(sn)
            l.append(sn)
# count taking part
    print("\n")
    cnt = int(input("Enter number of times it would repeat [default 0] : "))
# latency taking part 
    print("\n")
    latency_t=float(input("Enter time gap between 2 messages : "))
# timer time taking part
    time_t = int(input("Enter Timer time : "))
    timer_clock(time_t)
# other operation parts
    operations(n, cnt, msg, msg2,l,latency_t)
#last successful msg showing part
    print("\n")
    print("Spamming successfull")
