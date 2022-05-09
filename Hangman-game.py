import os
import random

os.system("clear")



def read_data(filepath="./archivos/data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return words

def run():
    
    data=read_data(filepath="./archivos/data.txt")
    chosen_word=random.choice(data)
    chosen_word_list=[letter for letter in chosen_word]
    chosen_word_list_underscore = ["_"] * len(chosen_word_list)
    print(chosen_word_list_underscore)






if __name__ == "__main__":
    run()


