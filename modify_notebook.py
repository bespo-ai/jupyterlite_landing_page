import nbformat
from nbformat.v4 import new_notebook, new_code_cell

def create_clean_notebook():
    """Create a completely clean notebook with only two cells and proper configuration."""
    notebook = new_notebook()
    
    # Set comprehensive notebook metadata
    notebook.metadata = {
        'kernelspec': {
            'display_name': 'Python 3 (ipykernel)',
            'language': 'python',
            'name': 'python3'
        },
        'language_info': {
            'codemirror_mode': {'name': 'ipython', 'version': 3},
            'file_extension': '.py',
            'mimetype': 'text/x-python',
            'name': 'python',
            'nbconvert_exporter': 'python',
            'pygments_lexer': 'ipython3',
            'version': '3.8.10'
        },
        'jupyterlab': {
            'themes': {
                'theme': 'JupyterLab Night',
                'settings': {
                    '@jupyterlab/notebook-extension:tracker': {
                        'codeCellConfig': {
                            'autoClosingBrackets': True,
                            'lineNumbers': True
                        }
                    },
                    '@jupyterlab/shortcuts-extension:shortcuts': {
                        'notebook:run-cell': [{'selector': '.jp-Notebook:focus', 'keys': ['Enter']}]
                    }
                }
            }
        },
        'widgets': {},
        'notify_time': 0,
        'varInspector': {'cols': {'lenName': 16, 'lenType': 16, 'lenVar': 40}, 'kernels_config': {'python': {'delete_cmd_prefix': 'del ', 'delete_cmd_postfix': '', 'library': 'var_list.py', 'varRefreshCmd': 'print(var_dic_list())'}, 'r': {'delete_cmd_prefix': 'rm(', 'delete_cmd_postfix': ') ', 'library': 'var_list.r', 'varRefreshCmd': 'cat(var_dic_list())'}, 'julia': {'delete_cmd_prefix': '', 'delete_cmd_postfix': '', 'library': 'var_list.jl', 'varRefreshCmd': 'print(var_dic_list())'}}},
        'toc': {'base_numbering': 1, 'nav_menu': {}, 'number_sections': True, 'sideBar': True, 'skip_h1_title': False, 'title_cell': 'Table of Contents', 'title_sidebar': 'Contents', 'toc_cell': False, 'toc_position': {}, 'toc_section_display': True, 'toc_window_display': False}
    }
    
    # Create cells with minimal metadata
    cells = []
    
    # Import cell
    import_cell = new_code_cell(source='import vincent as v')
    import_cell.metadata = {
        'trusted': True,
        'editable': True,
        'deletable': True,
        'execution_count': 1,
        'jupyter': {'source_hidden': False}
    }
    import_cell.outputs = []
    cells.append(import_cell)
    
    # Help cell
    help_cell = new_code_cell(source='help(v)')
    help_cell.metadata = {
        'trusted': True,
        'editable': True,
        'deletable': True,
        'execution_count': 2,
        'jupyter': {'source_hidden': False}
    }
    help_cell.outputs = []
    cells.append(help_cell)
    
    notebook.cells = cells
    return notebook

def write_notebook(notebook_path='content/landing_page.ipynb'):
    """Write the notebook to file and verify its contents."""
    try:
        notebook = create_clean_notebook()
        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbformat.write(notebook, f)
        
        print(f'Successfully created notebook: {notebook_path}')
        print('Cell contents:')
        for i, cell in enumerate(notebook.cells):
            print(f'Cell {i + 1}: {cell.source}')
        return True
    except Exception as e:
        print(f'Error creating notebook: {str(e)}')
        raise

if __name__ == '__main__':
    write_notebook()
