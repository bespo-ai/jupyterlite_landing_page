import nbformat

def verify_notebook():
    notebook_path = 'content/landing_page.ipynb'
    try:
        notebook = nbformat.read(notebook_path, nbformat.NO_CONVERT)
        print('Number of cells:', len(notebook.cells))
        print('\nCell contents:')
        for i, cell in enumerate(notebook.cells):
            print(f'\nCell {i + 1}:')
            print(f'Type: {cell.cell_type}')
            print(f'Source: {cell.source[:200]}...' if len(cell.source) > 200 else f'Source: {cell.source}')
            
    except Exception as e:
        print(f'Error reading notebook: {str(e)}')
        raise

if __name__ == '__main__':
    verify_notebook()
