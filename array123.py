def array123(nums):
  n = len(nums)
  for i in nums[0:n]:
    if i == 1:
      print(i)
      for j in nums [i:n]:
        if j ==2:
          print(j)
          for k in nums [j+1:n]:
            if k == 3:
              print(k)
              return True
  return False


s = [1,2,3]
print(array123(s))