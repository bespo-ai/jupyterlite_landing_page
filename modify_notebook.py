import nbformat
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

def modify_notebook():
    # Read the notebook
    notebook_path = 'content/landing_page.ipynb'
    try:
        # Create a completely new notebook
        notebook = new_notebook()
        
        # Add import vincent cell
        import_cell = new_code_cell(source='import vincent as v')
        import_cell.metadata = {
            'trusted': True,
            'editable': True,
            'deletable': True,
            'execution_count': 1
        }
        import_cell.outputs = []  # Ensure clean outputs
        
        # Add help(v) cell
        help_cell = new_code_cell(source='help(v)')
        help_cell.metadata = {
            'trusted': True,
            'editable': True,
            'deletable': True,
            'execution_count': 2
        }
        help_cell.outputs = []  # Ensure clean outputs
        
        # Set notebook metadata
        notebook.metadata = {
            'kernelspec': {
                'display_name': 'Python 3 (ipykernel)',
                'language': 'python',
                'name': 'python3'
            },
            'language_info': {
                'codemirror_mode': {
                    'name': 'ipython',
                    'version': 3
                },
                'file_extension': '.py',
                'mimetype': 'text/x-python',
                'name': 'python',
                'nbconvert_exporter': 'python',
                'pygments_lexer': 'ipython3',
                'version': '3.8.10'
            },
            'jupyterlab': {
                'themes': {
                    'theme': 'JupyterLab Night'
                }
            }
        }
        
        # Add cells to notebook
        notebook.cells = [import_cell, help_cell]
        
        # Write the notebook
        nbformat.write(notebook, notebook_path)
        print(f'Successfully created notebook: {notebook_path}')
        print('Cell contents:')
        for i, cell in enumerate(notebook.cells):
            print(f'Cell {i + 1}: {cell.source}')
            
    except Exception as e:
        print(f'Error creating notebook: {str(e)}')
        raise

if __name__ == '__main__':
    modify_notebook()
