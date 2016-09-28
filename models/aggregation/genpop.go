package main

import "fmt"

type Cell struct {
	colony           *Colony
	large_aggregates int
	small_aggregates int
	is_mother        bool
}

type Colony struct {
	cells []Cell
}

func (c *Cell) bud() {
	daughter_large_aggregates := int(float64(c.large_aggregates) * 0.4)
	daughter_small_aggregates := int(float64(c.small_aggregates) * 0.4)
	var new_c Cell
	new_c.large_aggregates = daughter_large_aggregates
	new_c.small_aggregates = daughter_small_aggregates
	new_c.colony = c.colony
	c.colony.cells = append(c.colony.cells, new_c)
	c.large_aggregates -= daughter_large_aggregates
	c.small_aggregates -= daughter_small_aggregates
}

func (col *Colony) bud_all_cells() {
	num_cells := len(col.cells)
	for i := 0; i < num_cells; i++ {
		col.cells[i].bud()
	}
	fmt.Printf("There are now %v cells\n", num_cells*2)
}

func (col *Colony) enumerate_cells() {
	var large_aggregates, small_aggregates, psi_minus int
	for _, cell := range col.cells {
		if cell.large_aggregates == 0 && small_aggregates == 0 {
			psi_minus++
		} else {
			large_aggregates += cell.large_aggregates
			small_aggregates += cell.small_aggregates
		}
	}
	fmt.Printf("%v%% of cells are psi-\n", float64(psi_minus)/float64(len(col.cells)))
}

func main() {
	var c Cell
	var col Colony
	c.colony = &col
	c.large_aggregates = 60
	col.cells = append(col.cells, c)
	for i := 0; i < 16; i++ {
		col.bud_all_cells()
		col.enumerate_cells()
	}
}
