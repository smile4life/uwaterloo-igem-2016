# import modules
import matplotlib.pyplot as plt

# Yeast cell
class Cell(object):

    # Class initialization
    def __init__(self, cells, large_aggregates, small_aggregates = 0, is_mother = False):
        self.cells = cells
        self.large_aggregates = large_aggregates
        self.small_aggregates = small_aggregates
        self.is_mother = is_mother

    def bud(self):
        # TODO: Add probabalistic ratios suring cell division
        daughter_large_aggregates = int(self.large_aggregates * 0.4)
        daughter_small_aggregates = int(self.small_aggregates * 0.4)
        self.cells.append(Cell(cells, daughter_large_aggregates, daughter_small_aggregates))
        self.large_aggregates -= daughter_large_aggregates
        self.small_aggregates -= daughter_small_aggregates
        # print(len(self.cells))

def bud_all_cells(cells):
    # NOTE: not the same as iterating through cells (budding appends to cells)
    for i in range(len(cells)):
        cells[i].bud()

def enumerate_cells(cells):
    large_aggregates = 0
    small_aggregates  = 0
    psi_minus = 0
    for cell in cells:
        if cell.large_aggregates == 0 and cell.small_aggregates == 0:
            psi_minus += 1
        else:
            large_aggregates += cell.large_aggregates
            small_aggregates += cell.small_aggregates
    # print("There are " + str(len(cells)) + " cells")
    # print("There are " + str(large_aggregates) + " large aggregates")
    # print("There are " + str(small_aggregates) + " small aggregates")
    print(str(psi_minus / len(cells)) + "% of cells are psi-")
    psi_minus_vals.append(psi_minus / len(cells))

cells = []
cells.append(Cell(cells, 60, 0, True))

psi_minus_vals = []

for i in range(12):
    bud_all_cells(cells)
    enumerate_cells(cells)
# enumerate_cells(cells)

plt.plot([1 - x for x in psi_minus_vals])
plt.ylabel('Psi+%')
plt.xlabel('Generation #')
plt.show()
