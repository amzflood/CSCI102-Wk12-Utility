import string

def LoadFile(file):
      with open (file) as f:
            lines = f.read().splitlines()
      return lines
