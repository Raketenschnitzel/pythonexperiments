"""
   https://www.w3resource.com/python-exercises/class-exercises/
   Exercise 01
"""


class Converter(object):


  def __init__(self):
    self.nums = (1, 5, 10, 50, 100, 500, 1000)
    self.romes = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
    self.numsstack = list(self.nums)
    self.romesstack = list(self.romes)
    self._representation = ''
    print(self.numsstack)
    print(self.romesstack)


  def popHighestValue(self):
    if len(self.numsstack) > 0 and len(self.romesstack) > 0:
        return self.numsstack.pop(), self.romesstack.pop()
    else:
        return None


  def convertPart(self, amount, sign):
    result = ''
    if amount < 4:
        for i in range(amount):
            result += sign
    print('convertPart({},{}):{}'.format(amount,sign,result))
    return result


  def convertFull(self,number):
    # find char for highest mod
    maxval, sign = self.popHighestValue()
    try:
        replace = number//maxval
        rest = number%maxval
    except:
        print('Corrupt floor division {}//{}'.format(number, maxval))

    # return or recursion
    if rest == 0 and replace > 0:
        self._representation += self.convertPart(replace, sign)
        return
    elif rest > 0 and replace == 0:
        if rest > (maxval - self.numsstack[-1]):
            self._representation += self.romesstack[-2] + sign
            self.popHighestValue()
            self.convertFull(rest - maxval)
        else:
            self.convertFull(rest)
    elif rest > 0 and replace > 0:
        self._representation += self.convertPart(replace, sign)
        self.convertFull(rest)

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
