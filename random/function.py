def sum(*numbers):
  count = 0
  for num in numbers:
    count = count + num
  return count

returnedValue = sum(10,25,20)
print(returnedValue)


returnedValue = sum(10,25)
print(returnedValue)
