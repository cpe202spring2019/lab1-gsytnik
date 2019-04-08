
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError("Must be list")
   else:
      if len(int_list) < 1:
         return None
      max = int_list[0]
      for val in int_list:
         if val > max:
            max = val
      return max


def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError("Must be a list")
   else:
      if len(int_list) == 0:
         return int_list
      return reverse_rec(int_list[1:]) + [int_list[0]]


def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None:
      raise ValueError("Must be a list")
   if low > high:
      return None
   if int_list[low] == target:
      return low
   if int_list[high] == target:
      return high
   return bin_search(target, low + 1, high - 1, int_list)

