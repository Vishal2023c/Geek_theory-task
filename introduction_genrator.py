from colorama import Fore,Back,Style,init
init(convert=True)
print(Fore.LIGHTYELLOW_EX+"\n-------------Introduction Format Generator----------------\n")
print(Fore.LIGHTYELLOW_EX+"------------Enter your details----------------")

Name=input(Fore.MAGENTA+"what is your name ?:")
Place=input("Where are you from ?:")
Education=input("What is your education ?:")
Experience=input("what your experience ?:")
Hobby=input("What is your hobby ?:")
Strength=input("what your strength ?:")
Goal=input("what your goal ?:")


print(Fore.LIGHTYELLOW_EX+"\n---------------Your Introduction Format ------------------\n")
print(Fore.LIGHTCYAN_EX+"Hello sir and Hello mem.\nThank you sir and mem for giving this chance to introduce my self.")
print("\n",Fore.WHITE+"1.",Fore.MAGENTA+Name,"\n",Fore.WHITE+"2.",Fore.MAGENTA+Place,"\n",Fore.WHITE+"3.",Fore.MAGENTA+Education,"\n",Fore.WHITE+"4.",Fore.MAGENTA+Experience,"\n",Fore.WHITE+"5.",Fore.MAGENTA+Hobby,"\n",Fore.WHITE+"6.",Fore.MAGENTA+Strength,"\n",Fore.WHITE+"7.",Fore.MAGENTA+Goal,"\n",Fore.YELLOW+"That's all about me ,Thank you.")
