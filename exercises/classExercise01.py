"""
   https://www.w3resource.com/python-exercises/class-exercises/
   Exercise 01
"""


class Converter(object):


  def __init__(self):
    self.nums = [1, 5, 10, 50, 100, 500, 1000]
    self.romes = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    self._representation = ''
    print(self.nums)
    print(self.romes)


  def convertPart(self, amount):
    result = ''
    sign = self.romes.pop()
    for i in range(amount):
        result += sign
    print('convertPart:{}'.format(result))
    return result


  def convertFull(self,number):
    # find char for highest mod
    maxval = self.nums.pop()
    # print('Maxval:{}'.format(maxval))

    # find part to replace
    replace = number//maxval
    rest = number%maxval
    # print('self.representation:{}'.format(self._representation))
    # return or recursion
    if rest == 0 and replace > 0:
        return self.convertPart(replace)
    elif rest > 0 and replace == 0:
        self.romes.pop()
        return self.convertFull(rest)
    elif rest > 0 and replace > 0:
        self._representation += self.convertPart(replace)
        self._representation += self.convertFull(rest)

    #subtractive notation
    return self._representation

if __name__ == '__main__':
  aClass = Converter()
  print('Ergebnis Test 8: {}'.format(aClass.convertFull(8)))
  aClass = Converter()
  print('Ergebnis Test 9: {}'.format(aClass.convertFull(9)))
  aClass = Converter()
  print('Ergebnis Test 56: {}'.format(aClass.convertFull(56)))
  aClass = Converter()
  print('Ergebnis Test 803: {}'.format(aClass.convertFull(803)))
