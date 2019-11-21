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