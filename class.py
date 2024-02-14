class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __del__(self):
    print('Object is being deconstructed!')

p = Person('Lena', 25)
p2 = Person('Rustam', 28)
