import os
import itertools
import xlrd
import time
start_time = time.time()

# ! Excel sheet
sheet = xlrd.open_workbook(
    'ByNiels/NavneTilNetworkAnalysis.xlsx').sheet_by_index(0)

# ! Output sheet
Output_document = open("output.txt", "r+", encoding="utf-8")
# ! Clear document
Output_document.truncate()


# ! Output
def toOutput(OutStr):
    Output_document.write(OutStr + "\n")


# ! Read this document for relations
document = open("ByNiels/AllePlatonTekster.txt", "r",
                encoding="Latin-1").read().split()


# ! Combination class, for our custom DataType
class combis:
    radius = 1000

    def __init__(self, fir, sec):
        self.first = fir.lower()
        self.second = sec.lower()
        self.counter = 0
        self.firMet = []
        self.secMet = []
        self.complete = fir + sec

    def wake(self, meeting, indexNumber):
        if meeting.startswith(self.first):
            self.firMet.append(indexNumber)
        elif meeting.startswith(self.second):
            self.secMet.append(indexNumber)

    def countWithInRadius(self):
        for Subject in self.firMet:
            val1 = Subject
            for val2 in self.secMet:
                if (val1 < val2 and val1 >= val2 - self.radius) or (val1 > val2 and val1 <= val2 + self.radius):
                    self.counter += 1

    def result(self):
        return self.first + " & " + self.second + " : " + str(self.counter)


combinations_Array = []

# ! Create relationskombinationerne
sheet_iteration = 0
reading_sheet = True
while reading_sheet:
    try:
        first_value = sheet.cell_value(sheet_iteration, 0)
        second_value = sheet.cell_value(sheet_iteration, 1)
        combinations_Array.append(combis(first_value, second_value))
    except IndexError as error:
        print('Sheet read with a combination length of ' +
              str(len(combinations_Array)))
        reading_sheet = False
        break
    sheet_iteration += 1

# ! Checking words in document, and giving them an index number
word_index = 0
for word in document:
    w = word.lower()
    for combination in combinations_Array:
        combination.wake(w, word_index)
    word_index += 1
print('Document read and index numbers saved to combinations.')

for combination in combinations_Array:
    combination.countWithInRadius()
    toOutput(combination.result())

# ! For fun and resaerch
print("Program took", str((time.time() - start_time) / 60), " minutes to run")
