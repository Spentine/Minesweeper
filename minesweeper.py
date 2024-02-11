import random

class Minesweeper:
  def __init__(self, settings):
    self.width = settings["width"]
    self.height = settings["height"]
    self.mines = settings["mines"]
    self.field = []
    self.marks = []
    self.playing = True
    self.revealed = 0

    for i in range(self.height):
      self.field.append([0] * self.width)
      self.marks.append([0] * self.width)

    remainingTiles = self.width * self.height
    remainingMines = self.mines
    for row in self.field:
      for i in range(self.width):
        if random.random() < remainingMines / remainingTiles:
          row[i] = -1
          remainingMines -= 1
        remainingTiles -= 1

  def returnNeighbors(self, row, column):
    checkR = [row - 1, row, row + 1]
    checkC = [column - 1, column, column + 1]
    if row == self.height - 1:
      del checkR[2]
    if row == 0:
      del checkR[0]
    if column == self.width - 1:
      del checkC[2]
    if column == 0:
      del checkC[0]
    return checkR, checkC

  def calculateNeighbors(self, row, column):
    checkR, checkC = self.returnNeighbors(row, column)

    neighbors = 0

    for i in checkR:
      for j in checkC:
        neighbors += int(self.field[i][j] == -1)

    return neighbors

  def reveal(self, row, column):
    row = int(row)
    column = int(column)
    if self.field[row][column] == -1:
      self.playing = False
      return False
    self.field[row][column] = 1

    if self.calculateNeighbors(row, column) == 0:
      checkR, checkC = self.returnNeighbors(row, column)
      for i in checkR:
        for j in checkC:
          if self.field[i][j] == 0:
            self.reveal(i, j)

  def consoleField(self):
    assignment = {
      0: ":;",
      -1: "[]",
    }
    r = ""
    for i in range(self.height):
      for j in range(self.width):
        k = self.field[i][j]
        if k == 1:
          r += str(self.calculateNeighbors(i, j)) + "_"
        else:
          r += assignment[k]
      r += "\n"
    return r

settings = {
  "width": 10,
  "height": 10,
  "mines": 10,
}
x = Minesweeper(settings)
while x.playing:
  print(x.consoleField())
  x.reveal(input("row "), input("column "))
