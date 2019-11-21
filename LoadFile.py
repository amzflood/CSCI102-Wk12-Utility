import string

def LoadFile(file):
      original_word_list = []
      temp_list = []
      with open (file) as f:
            lines = f.read().splitlines()
      return lines
