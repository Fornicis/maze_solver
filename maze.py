from cell import Cell
import random
import time

class Maze:
    def __init__(self, 
                x1,
                y1, 
                num_rows, 
                num_cols, 
                cell_size_x, 
                cell_size_y, 
                win):
        self._cells = []  # List to hold maze cells
        self._x1 = x1  # Starting x-coordinate
        self._y1 = y1  # Starting y-coordinate
        self._num_rows = num_rows  # Number of rows in the maze
        self._num_cols = num_cols  # Number of columns in the maze
        self._cell_size_x = cell_size_x  # Width of each cell
        self._cell_size_y = cell_size_y  # Height of each cell
        self._win = win  # Window to draw the maze on

        self._create_cells()  # Initialize and draw cells

    def _create_cells(self):
        # Create a grid of cells
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))  # Create cell and add to column
            self._cells.append(col_cells)  # Add column to maze

        # Draw each cell in the grid
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        # Calculate cell coordinates
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)  # Draw the cell
        self._animate()  # Animate the drawing process

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()  # Redraw the window
        time.sleep(0.04)  # Pause for animation effect (4ms)
