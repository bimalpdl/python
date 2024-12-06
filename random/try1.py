class oddEvenFinder:
   def countOddEven(self,arr):
      self.odd = 0
      self.even = 0
      for num in arr:
        if num % 2 == 0:
            self.even += 1 
        else:
            self.odd += 1 
   # returns the result as an array 
      return [self.odd,self.even] 
 

def main():
    object = oddEvenFinder()
    arr = [1,2,3,4,5]
    arr1 = [1,3,5,9]
    print(arr)
    print(f"{object.countOddEven(arr)}: [Odd, Even]")
    print()
    print(arr1)
    print(f"{object.countOddEven(arr1)}: [Odd, Even]")



if __name__ == "__main__":
    main()
