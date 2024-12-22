import nbformat
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

def modify_notebook():
    # Read the notebook
    notebook_path = 'content/landing_page.ipynb'
    try:
        notebook = nbformat.read(notebook_path, nbformat.NO_CONVERT)
        
        # Create fresh cells list
        new_cells = []
        
        # Add import vincent cell
        import_cell = new_code_cell(source='import vincent as v')
        new_cells.append(import_cell)
        
        # Add help(v) cell
        help_cell = new_code_cell(source='help(v)')
        new_cells.append(help_cell)
        
        # Create a new notebook with only these cells
        fresh_notebook = new_notebook()
        fresh_notebook.cells = new_cells
        fresh_notebook.metadata = notebook.metadata
        
        # Replace the notebook entirely
        notebook = fresh_notebook
        
        # Write the modified notebook
        nbformat.write(notebook, notebook_path)
        print(f'Successfully modified notebook: {notebook_path}')
        print('New cell contents:')
        for i, cell in enumerate(new_cells):
            print(f'Cell {i + 1}: {cell.source[:50]}...')
            
    except Exception as e:
        print(f'Error modifying notebook: {str(e)}')
        raise

if __name__ == '__main__':
    modify_notebook()
