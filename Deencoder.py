import os
import pyttsx3
from colorama import Fore           
import os
import datetime
import platform 
import winsound
import time
import keyboard
import mouse

def playdot():
   winsound.Beep(2000, 150)

def playdash():
   winsound.Beep(2000, 650)

def left():
   keyboard.press('-')   

def right():
   keyboard.press('.')

def middle():
   keyboard.press(' ')

def back():
   keyboard.press('backspace')

dot = '.'
dash =  '-'

tts = True


file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin\\settings.txt")
file_path2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin\\mem.txt")

oname = platform.system()

now = datetime.datetime.now()

print('checking system requirements... ')
playdot()
with open(file_path, 'r') as settings:
   content = settings.readline()
   if content.strip().lower() == 'tts/on':
      tts = True
   if content.strip().lower() == 'tts/off':
      tts = False
#saves to mem file
with open(file_path2, 'a+') as mem:
         mem.writelines(f"""
                        File opened at {now}
""")
         mem.close()

if oname.lower() == 'windows':
    print('Your system is compatable with this software.')
    os.system('cls')
    ()
else:
    print('Your system is not compatable with this software.')
    print('You can exit at anytime.')
    while True:
        pass

print(f""" _____    ______   ______   _   _    _____    ____    _____    ______   _____  
|  __ \  |  ____| |  ____| | \ | |  / ____|  / __ \  |  __ \  |  ____| |  __ \  login time: {"%s/%s/%s %s:%s:%s" % (now.month,now.day,now.year,now.hour,now.minute,now.second)}
| |  | | | |__    | |__    |  \| | | |      | |  | | | |  | | | |__    | |__) | email the creator @: deencodergit@gmail.com
| |  | | |  __|   |  __|   | . ` | | |      | |  | | | |  | | |  __|   |  _  /  github - https://github.com/Bjornhotline/DeenCoderRemastered
| |__| | | |____  | |____  | |\  | | |____  | |__| | | |__| | | |____  | | \ \  Developed by username8bit on github
|_____/  |______| |______| |_| \_|  \_____|  \____/  |_____/  |______| |_|  \_\ [v0.0.4 Remastered]
------------------------------------------------------------------------------------------------------------------------------""")

t1 = 'DeenCoder-Main'
t2 = 'DeenCoder-Morse to English'
t3 = 'DeenCoder-English to Morse' 

ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', '+': '.-.-.', '=': '-...-',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', '!': '-.-.--', ')': '-.--.-', '"': ".-..-.",
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', '/': '-..-.', '(': '-.--.', ':': '---...',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',  '?': '..--..', '@': '.--.-.', ';': '-.-.-.',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '+': '.-.-.', '&': '.-...'}


MORSE_TO_ENGLISH = {}
for key, value in ENGLISH_TO_MORSE.items():
    MORSE_TO_ENGLISH[value] = key


def english_to_morse(message):
    morse = []  
    for char in message:
        if char in ENGLISH_TO_MORSE:
            morse.append(ENGLISH_TO_MORSE[char]) 
    return " / ".join(morse)

def morse_to_englishtxt(message):
    message = message.split(" ")
    english = []  
    for code in message:
        if code in MORSE_TO_ENGLISH:
            english.append(MORSE_TO_ENGLISH[code])
    return " ".join(english)  


def main():
    while True:
        os.system(f'title {t1}')
        print("")
        print('DeenCoder - Please choose 1/2/3/4 or ''help'' for additional options - Please note that DeenCoder is still in the beta stages!')
        response = input("""[1] to Convert Morse Code to English
[2] to Convert English to Morse Code
[3] to Print a Morse Code Chart
[4] to Exit DeenCoder
[?~] """)
        if response == "1":
         os.system(f'title {t2}')
         print("")
         print('example: -.. . . -. -.-. --- -.. . .-.> DeenCoder')
         print("Enter Morse code (with a space after each code): ")
         with open(file_path, 'r') as settings:
           content = settings.readlines()
           if 0 <= 2 - 1 < len(content):
              line = content[2 - 1].strip()
              if line == 'mouse/off':
               ()
              if line == 'mouse/on':
               mouse.on_click(left)
               mouse.on_right_click(right)
               mouse.on_middle_click(middle)
         morse = input("~> ")
         mouse.unhook_all()
         settings.close()
         print("")
         english = morse_to_englishtxt(morse)
         englishtxt = morse_to_englishtxt(morse)
         print('')
         print(Fore.GREEN + '### English version ###')
         print(Fore.GREEN + english)
         print(Fore.GREEN + '### English version ###')
         print(Fore.WHITE + '')
         #mem
         now = datetime.datetime.now()
         with open(file_path2, 'a') as mem:
          mem.writelines(f'''
                         morse to english: {now}, {morse} = {english}
''')
          mem.close()
         if english == '': 
            print(Fore.RED + '!Error in translation!')
            print(Fore.WHITE + '')
            main()
         print(Fore.WHITE + '')
         print("")
         if tts == True:
          yn = input('Play message (y/n): ')
          if yn.lower() == 'y':
             print("")
             print(Fore.YELLOW + f"saying - {englishtxt}")
             print(Fore.WHITE + "")
             text_speech = pyttsx3.init()
             text_speech.say(english)
             text_speech.runAndWait()
          if yn.lower() == 'n':
             ()
          if tts == False:
            ()
          else:
             ()
        
        elif response == "2":
         os.system(f'title {t3}')
         print("")
         print('example: DeenCoder> -.. . . -. -.-. --- -.. . .-.')
         print("Enter English text: ")
         english = input("~> ").upper()
         print("")
         morse = english_to_morse(english)
         print('')
         print(Fore.GREEN + '### Morse Code version ###')
         print(Fore.GREEN + morse)
         print(Fore.GREEN + '### Morse Code version ###')
         print(Fore.WHITE + '')
         #mem
         now = datetime.datetime.now()
         with open(file_path2, 'a') as mem:
          mem.writelines(f'''
                         english to morse: {now}, {english} = {morse}
''')
          mem.close()
         if morse == '': print(Fore.RED + '!Error in translation!')
         print(Fore.WHITE + '')
         if tts == True:
          yn = input('Play message (y/n): ')
          if yn.lower() == 'y':
             print("")
             print(Fore.YELLOW + f"playing - {morse}")
             print(Fore.WHITE + "")
             for signal in morse:
                   if signal == '.':
                      playdot()
                   elif signal == '-':
                      playdash()
                   time.sleep(.05) 
          if yn.lower() == 'n':
             ()
          if tts == False:
            ()
          else:
             ()
        elif response == "4":
         exit()
    
        elif response == "3":
   
         print(Fore.GREEN + '')
         print("""A	.-	B	-...
C	-.-.	D	-..
E	.	F	..-.
G	--.	H	....
I	..	J	.---
K	-.-	L	.-..
M	--	N	-.
O	---	P	.--.
Q	--.-	R	.-.
S	...	T	-
U	..-	V	...-
W	.--	X	-..-
Y	-.--	Z	--..
0	-----	1	.----
2	..---	3	...--
4	....-	5	.....
6	-....	7	--...
8	---..	9	----.
.      .-.-.-   ,       --..--
?      ..--..   /       -..-.
!      -.-.--   +       .-.-.
@      .--.-.   &       .-...
(      -.--.    )       -.--.-
=      -...-    ;       -.-.-.
:      ---...   "       .-..-.""")        
         print(Fore.WHITE + '')

        elif response.lower() == 'res' or response.lower() == 'reset':
            os.system('cls')
        elif response.lower() == 'clrmem':
           with open(file_path2, 'w') as mem:
              ()
              mem.close()
        elif response.lower() == 'listmem':
           with open(file_path2, 'r') as memread:
             memcontent = memread.read()
             print(Fore.RED + "")
             print(memcontent, "clrmem to clear file contents")
             print(Fore.WHITE + "")
        
        elif response.lower() == 'help':
           print(Fore.RED+'')
           print("""
                 res or reset to clear terminal
                 listmem to veiw translation memory
                 clrmem to reset the memory file""")
           print(Fore.WHITE+'')
        elif response == '':
          ()

        else:
           print(" ")
           print(Fore.RED + 'Please Enter a valid oporation!')
           print(Fore.WHITE + '')
   


if __name__ == "__main__":

    main()

