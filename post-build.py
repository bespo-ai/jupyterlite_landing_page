from bs4 import BeautifulSoup
import json

# Load the existing HTML file
input_file_path = '_output/notebooks/index.html'
output_file_path = '_output/notebooks/index.html'

with open(input_file_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find the head tag
head_tag = soup.find('head')

# Create and add viewport meta tag to prevent mobile zoom
viewport_meta = soup.new_tag('meta')
viewport_meta['name'] = 'viewport'
viewport_meta['content'] = 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no'
head_tag.append(viewport_meta)

# Find the specific <script> tag to insert after
target_script = soup.find('script', text=lambda text: text and 'index.html' in text)

# Create the new script
new_script = '''
<script>
    async function installVincent() {
        try {
            // Wait for both the notebook app and the first notebook to be fully loaded
            while (!window.jupyterapp) {
                await new Promise(resolve => setTimeout(resolve, 100));
            }
            
            // Get the first notebook and wait for its kernel to be ready
            const notebook = window.jupyterapp.shell.widgets().next().value;
            if (!notebook) {
                throw new Error("No notebook found");
            }

            // Wait for the kernel to be ready
            while (!notebook.sessionContext?.session?.kernel) {
                await new Promise(resolve => setTimeout(resolve, 100));
            }

            // Execute the installation in the notebook
            await notebook.sessionContext.session.kernel.requestExecute({
                code: `
                    import piplite
                    await piplite.install("vincent")
                `
            }).done;
            console.log("Vincent package installed successfully");
        } catch (error) {
            console.error("Error installing Vincent:", error);
        }
    }

    function removeNotebookHeaders() {
        document.getElementById('top-panel-wrapper')?.remove();
        document.getElementById('menu-panel-wrapper')?.remove();
        document.getElementsByClassName('jp-NotebookPanel-toolbar')[0]?.remove();
    }

    function triggerInitialScroll() {
        // Minimal scroll to trigger notebook render without visible movement
        window.scrollBy({
            top: 1,
            behavior: 'instant'
        });
    }

    function pollForHeaders() {
        if (document.querySelector('button.jp-Notebook-footer')) {
            removeNotebookHeaders();
            // Trigger initial scroll after a short delay to ensure content is loaded
            setTimeout(triggerInitialScroll, 1000);
            // Install Vincent after headers are removed
            installVincent();
        } else {
            setTimeout(pollForHeaders, 50);
        }
    }

    // Start polling
    pollForHeaders();
</script>
'''

# Insert the new script after the target script
target_script.insert_after(BeautifulSoup(new_script, 'html.parser'))

# Save the modified HTML to a new file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(str(soup))

print(f'Modified HTML saved to {output_file_path}')

# Update jupyter-lite.json
json_path = '_output/notebooks/jupyter-lite.json'
try:
    with open(json_path, 'r') as f:
        config = json.load(f)
    
    # Add or update the exposeAppInBrowser setting
    config['jupyter-config-data']['exposeAppInBrowser'] = True
    
    # Write the updated config back to the file
    with open(json_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f'Updated {json_path} with exposeAppInBrowser setting')
except Exception as e:
    print(f'Error updating jupyter-lite.json: {e}')
