class Stiffener:
  def __init__(self, width, height, length):
    self.width = width
    self.height = height
    self.length = length
  def cross_section(width, height):
    area = width * height
    return area
  def volume(area, length):
    volume = area * length
    return volume


