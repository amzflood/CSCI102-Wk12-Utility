def NotIn(list1, list2):
      result = set(list2) & set(list1)
      result = list(result)
      count = 0
      while count < len(result):
            tracking = result[count]
            list2.remove(tracking)
            count += 1
      return list2
