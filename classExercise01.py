"""
   https://www.w3resource.com/python-exercises/class-exercises/
   Exercise 01
"""


class Converter(object):
  
  
  def __init__(self):
    self.conv = {
      'I' : 1,
      'V' : 5,
      'X' : 10,
      'L' : 50,
      'C' : 100,
      'D' : 500,
      'M' : 1000
    }
    
    self._representation = None
    
    print(self.conv)
    
  def reduceOrder(self):
    print('Reduce Order')
    pass  
  
  def representation(self, roman):
    if roman is None:
      return self._representation
    else:
      self._representation = roman
      
  def convertPart(self, number):
    for k,v in self.conv.items():
      if v == number:
        self.representation(k)
    
  def convertFull(self,number):
    # find char for highest mod
    max = max(self.conv.values)
    print('Max of conv:{}'.format(max))
    
    # find part to replace
    replace = number//max
    rest = number//max
    
    # leave recursion
    if rest == 0 and replace > 0:
      self.convertPart(replace)
      return self
    elif rest > 0 and replace > 0:
      self.convertPart(replace)
      
    
    #subtractive notation
    return romanString
    
if __name__ == '__main__':
  aclass = Converter()
