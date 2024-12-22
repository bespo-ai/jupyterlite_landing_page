import nbformat
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

# Read the notebook
notebook_path = 'content/landing_page.ipynb'
notebook = nbformat.read(notebook_path, nbformat.NO_CONVERT)

# Keep the first markdown cell (hero section)
new_cells = [notebook.cells[0]]

# Add import vincent cell
import_cell = new_code_cell(source='import vincent as v')
new_cells.append(import_cell)

# Add help(v) cell
help_cell = new_code_cell(source='help(v)')
new_cells.append(help_cell)

# Replace cells in notebook
notebook.cells = new_cells

# Write the modified notebook
nbformat.write(notebook, notebook_path)
print(f'Modified notebook saved to {notebook_path}')
