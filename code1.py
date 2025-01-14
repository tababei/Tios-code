class Stiffener:
  def __init__(self, width, height, length):
    self.width = width
    self.height = height
    self.length = length
  @property
  def cross_section(self):
    area = self.width * self.height
    return area
  @property
  def volume(self):
    volume = self.cross_section * self.length
    return volume

