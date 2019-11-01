import os
import sys

# ! Importering af tekst dokument
# todo HER SKAL DU INDSÆTTE PATH TIL TEKSTFILEN!
document = open('timaeus_engelsk_4.txt')
document_word = document.read().split()
"""
! Ordliste
* De bestemte ord som vores script skal finde i vores "document"
? Tallet (0) er vores word counter
"""
word_list = [
    "socrates",
    "critias",
    "timaeus",
    "hermocrates",
    "plato"
]

# ! Hvert emne bliver gemt sammen med deres ord index

subject_index = []

display = [
    ["Socrates & Critias: ", 0],
    ["Socrates & Timaeus: ", 0],
    ["Socrates & Hermocrates: ", 0],
    ["Socrates & Plato: ", 0],
    ["Critias & Timaeus: ", 0],
    ["Critias & Hermocrates: ", 0],
    ["Critias & Plato: ", 0],
    ["Timaeus & Hermocrates: ", 0],
    ["Timaeus & Plato: ", 0],
    ["Hermocrates & Plato: ", 0]
]

table = 600
reverse_string_counter = 0


def within600(a, e):
    if a % e <= table:
        return True
    return False


def checkword(e, i):
    e = e.lower()
    for subject in word_list:
        if e.startswith(subject):
            created_list = [e, i]
            subject_index.append(created_list)


index_counter = 1

# ! Gemmer hvert ord sammen med deres ord index
for word in document_word:
    checkword(word, index_counter)
    index_counter += 1


# ! Tjekker om vores ord ligger indenfor 600 ords rækkevidde af hinanden
for subject in subject_index:

    for compare in subject_index:
        if compare[0] == subject[0]:
            break
        else:
            within_each_other = within600(subject[1], compare[1])
            if within_each_other:
                # * Socrates & Critias
                if compare[0].startswith(word_list[0][0]) and subject[0].startswith(word_list[1][0]):
                    display[0][1] += 1
                # * Socrates & Timaeus
                elif compare[0].startswith(word_list[0][0]) and subject[0].startswith(word_list[2][0]):
                    display[1][1] += 1
                # * Socrates & Hermocrates
                elif compare[0].startswith(word_list[0][0]) and subject[0].startswith(word_list[3][0]):
                    display[2][1] += 1
                # * Socrates & Plato
                elif compare[0].startswith(word_list[0][0]) and subject[0].startswith(word_list[4][0]):
                    display[3][1] += 1
                # * Critias & Timaeus
                elif compare[0].startswith(word_list[1][0]) and subject[0].startswith(word_list[2][0]):
                    display[4][1] += 1
                # * Critias & Hermocrates
                elif compare[0].startswith(word_list[1][0]) and subject[0].startswith(word_list[3][0]):
                    display[5][1] += 1
                # * Critias & Plato
                elif compare[0].startswith(word_list[1][0]) and subject[0].startswith(word_list[4][0]):
                    display[6][1] += 1
                # * Timaeus & Hermocrates
                elif compare[0].startswith(word_list[2][0]) and subject[0].startswith(word_list[3][0]):
                    display[7][1] += 1
                # * Timaeus & Plato
                elif compare[0].startswith(word_list[2][0]) and subject[0].startswith(word_list[4][0]):
                    display[8][1] += 1
                # * Hermocrates & Plato
                elif compare[0].startswith(word_list[3][0]) and subject[0].startswith(word_list[4][0]):
                    display[9][1] += 1
                else:
                    reverse_string_counter += 1
            else:
                continue

print('Disse ord er indenfor en rækkevidde på '+str(table)+' ord af hinanden.')
for within_index in display:
    print(within_index[0]+str(within_index[1]))
