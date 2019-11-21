def UpdateString(string, replacing_variable, index):
      string = list(string)
      index = int(index)
      for i in string:
            if string[index] == i:
                  string[index] = replacing_variable
      updatedString = "".join(string)
      return print("OUTPUT", updatedString)

