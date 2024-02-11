import random

class Minesweeper:
  def __init__(self, settings):
    self.width = settings["width"]
    self.height = settings["height"]
    self.mines = settings["mines"]
    self.field = []
    for i in range(self.height):
      self.field.append([0] * self.width)
    remainingTiles = self.width * self.height
    remainingMines = self.mines
    for row in self.field:
      for i in range(self.width):
        if random.random() < remainingMines / remainingTiles:
          row[i] = -1
          remainingMines -= 1
        remainingTiles -= 1

  def consoleField(self):
    assignment = {
      0: ":;",
      -1: "##",
    }
    r = ""
    for i in self.field:
      for j in i:
        r += assignment[j]
      r += "\n"
    return r

settings = {
  "width": 10,
  "height": 10,
  "mines": 10,
}
x = Minesweeper(settings)
print(x.consoleField())
