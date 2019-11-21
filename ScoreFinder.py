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
