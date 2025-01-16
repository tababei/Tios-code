class Stiffener:
  def __init__(self, width, height, length, density):
    self.width = width
    self.height = height
    self.length = length
    self.density = density
  @property
  def cross_section(self):
    area = self.width * self.height
    return area
  @property
  def volume(self):
    volume = self.cross_section * self.length
    return volume
  @property
  def mass(self):
    mass = self.volume * (10 ** (-9)) * self.density
    return mass


def sum(a,b):
  return a+b