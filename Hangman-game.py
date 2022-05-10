import os
import random

def clear():
    os.system("clear")




def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s




def read_data(filepath="./archivos/data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return words




def run():
    x=0
    data=read_data(filepath="./archivos/data.txt")
    random_word=random.choice(data)
    random_word_normalize=normalize(random_word)
    random_word_list=[letter for letter in random_word_normalize]
    random_word_list_underscore = ["_"] * len(random_word_list)
    clear()

    while x < 7:
        if random_word_list != random_word_list_underscore:
            letter_bool = False
            print(random_word_list_underscore)
            while letter_bool == False:
                letter = input("ingrese una letra:").strip().upper()
                if letter.isalpha()==False:
                    print("Solo puedes ingresar letras")
                    letter_bool=False
                else:
                    letter_bool=True
                if len(letter) > 1:
                    letter_bool=False
                    print("solo puede ingresar un caracter")
            clear()
            for i in range(len(random_word_normalize)):
                if random_word_normalize[i]==letter:
                    random_word_list_underscore[i] = letter
            x += 1
        else:
            print("ganaste!!! la palabra era:", random_word)
            break
    print("Perdiste. La palabra era:", random_word)

           
                    
    




if __name__ == "__main__":
    run()


