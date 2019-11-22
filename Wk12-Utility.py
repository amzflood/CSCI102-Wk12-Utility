# https://github.com/amzflood/CSCI102-Wk12-Utility
# Alicia Flood
# CSCI 102 - Section E
# Week 11 - Part B

import string

def PrintOutput(word):
    word = str(word)
    print ("OUTPUT", word)

def LoadFile(file):
      with open (file) as f:
            lines = f.read().splitlines()
      return lines
      
def UpdateString(string, replacing_variable, index):
      string = list(string)
      index = int(index)
      for i in string:
            if string[index] == i:
                  string[index] = replacing_variable
      updatedString = "".join(string)
      return print("OUTPUT", updatedString)

def FindWordCount(file, find):
      word_list = []
      for line in file:
            words = line.split(" ")
            for word in words:
                  temp_string = ""
                  for char in word:
                        if char in string.ascii_letters:
                              temp_string += char
                  word_list.append(temp_string)
      count = 0
      for i in word_list:
            if find == i:
                  count += 1
      return count

def ScoreFinder(player, score, find_score):
      P_list = ' '.join([str(i) for i in player])
      List1 = P_list.upper()
      List1 = list(List1.split(" "))
      Find = find_score.upper()
      result1 = List1.index(Find)
      result2 = score[result1]
      if result1 >= 0:
            output = print(player[result1], "got a score of", result2)
      else:
            output = print("player not found")
      return output

def Union(list1, list2):
    list3 = list1 + list2
    return list3

def Intersection(list1, list2):
      output = set(list2) & set(list1)
      return output

def NotIn(list1, list2):
      result = set(list2) & set(list1)
      result = list(result)
      count = 0
      while count < len(result):
            tracking = result[count]
            list2.remove(tracking)
            count += 1
      return list2







