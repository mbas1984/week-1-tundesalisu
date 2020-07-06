class Teams:
  def __init__(self, members):
    self.__myTeam = members
    self.num = 1

  def __len__(self):
    return len(self.__myTeam)

  def __iter__(self):
      return self
    
  def __next__(self):
      counter = self.num
      self.num+= 1
      return counter
    
  def __contains__(self,key):
      return key in self.__myTeam

def main():
  classmates = Teams([1, 2, 3])
  print(len(classmates))
  print(next(classmates))
  print(next(classmates))
  print( 2 in classmates)
  
  
  
  
  
  
  
  ######## Manual script to iterate.
#  it =iter([1,2,3])
#  print(next(it))
#  print(next(it))
#  print(next(it))
  
 

main()