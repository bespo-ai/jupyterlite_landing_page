from bs4 import BeautifulSoup

# Load the existing HTML file
input_file_path = 'dist/notebooks/index.html'
output_file_path = 'dist/notebooks/index.html'

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

print(f'Modified HTML saved to ')
# Create the new script and style tags
new_script = '''
<script>
    function removeNotebookHeaders() {
        document.getElementById('top-panel-wrapper')?.remove();
        document.getElementById('menu-panel-wrapper')?.remove();
        document.getElementsByClassName('jp-NotebookPanel-toolbar')[0]?.remove();
    }

    // Remove any existing chat containers
    function removeExistingChatContainers() {
        // Function to remove chat-related elements
        function removeChatElements(node) {
            if (!node) return;
            
            // If this is the chat container itself, remove it
            if (node.nodeType === 1) { // Element node
                if (node.textContent && node.textContent.includes('step 1: I\'ll start by importing')) {
                    node.remove();
                    return;
                }
                
                // Check for chat input
                if (node.tagName === 'INPUT' && node.getAttribute('placeholder') === 'Type a message...') {
                    let element = node;
                    while (element && element.tagName !== 'BODY') {
                        const parent = element.parentElement;
                        element.remove();
                        element = parent;
                    }
                    return;
                }
            }
        }
        
        // Initial cleanup
        document.querySelectorAll('*').forEach(removeChatElements);
        
        // Set up an observer to watch for new elements
        const observer = new MutationObserver((mutations) => {
            mutations.forEach((mutation) => {
                // Handle new nodes
                mutation.addedNodes.forEach(removeChatElements);
                
                // Also check the modified node itself
                removeChatElements(mutation.target);
            });
        });
        
        // Start observing the entire document
        observer.observe(document.documentElement, {
            childList: true,
            subtree: true,
            characterData: true
        });
    }
    
    // Call removeExistingChatContainers when the document is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', removeExistingChatContainers);
    } else {
        removeExistingChatContainers();
    }

    // Apply theme immediately
    const darkThemeStyle = document.createElement('style');
    darkThemeStyle.textContent = `
        :root[data-jp-theme-name="JupyterLab Night"] {
            --jp-layout-color0: #111111;
            --jp-layout-color1: #212121;
            --jp-layout-color2: #424242;
            --jp-layout-color3: #616161;
            --jp-layout-color4: #757575;
            
            --jp-content-font-color0: rgba(255, 255, 255, 1);
            --jp-content-font-color1: rgba(255, 255, 255, 0.87);
            --jp-content-font-color2: rgba(255, 255, 255, 0.54);
            --jp-content-font-color3: rgba(255, 255, 255, 0.38);
            
            --jp-brand-color0: #82b1ff;
            --jp-brand-color1: #2979ff;
            --jp-brand-color2: #2962ff;
            --jp-brand-color3: #2962ff;
        }
        
        body {
            background-color: var(--jp-layout-color0) !important;
            color: var(--jp-content-font-color1) !important;
        }
        
        .jp-Notebook {
            background-color: var(--jp-layout-color1) !important;
        }
        
        .jp-Cell {
            background-color: var(--jp-layout-color1) !important;
        }
        
        .jp-InputArea-editor {
            background-color: var(--jp-layout-color2) !important;
            color: var(--jp-content-font-color1) !important;
        }
        
        .jp-OutputArea-output {
            background-color: var(--jp-layout-color1) !important;
            color: var(--jp-content-font-color1) !important;
        }
    `;
    document.head.appendChild(darkThemeStyle);
    
    function setDarkTheme() {
        document.documentElement.setAttribute('data-jp-theme-name', 'JupyterLab Night');
        document.documentElement.setAttribute('data-jp-theme-light', 'false');
        console.log('Applied JupyterLab Night theme');
    }

    function triggerInitialScroll() {
        // Minimal scroll to trigger notebook render without visible movement
        window.scrollBy({
            top: 1,
            behavior: 'instant'
        });
    }

    function changeKeyboardShortcuts() {
        // Add event listener for Enter key on cells
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Enter' && !event.shiftKey) {
                const activeElement = document.activeElement;
                const cell = activeElement?.closest('.jp-Cell');
                
                if (cell && !activeElement.matches('textarea, input')) {
                    event.preventDefault();
                    event.stopPropagation();
                    
                    // Find and click the run button
                    const runButton = document.querySelector('.jp-Toolbar-item button[data-command="notebook:run-cell-and-select-next"]');
                    if (runButton) {
                        runButton.click();
                    }
                }
            }
        }, true);
        
        console.log('Enter key shortcut handler installed');
    }

    function pollForHeaders() {
        if (document.querySelector('button.jp-Notebook-footer')) {
            // Apply theme first to prevent flash of light theme
            setDarkTheme();
            removeNotebookHeaders();
            // Remove any chat containers that might exist
            removeExistingChatContainers();
            // Trigger initial scroll after a short delay to ensure content is loaded
            setTimeout(triggerInitialScroll, 100);
            // Initialize keyboard shortcuts
            changeKeyboardShortcuts();
            // Load manifesto content with retry
            loadManifestoWithRetry();
        } else {
            setTimeout(pollForHeaders, 50);
        }
    }
    
    function loadManifestoWithRetry(retries = 3) {
        loadManifesto().catch(error => {
            console.error('Error loading manifesto:', error);
            if (retries > 0) {
                setTimeout(() => loadManifestoWithRetry(retries - 1), 1000);
            }
        });
    }
    
    async function loadManifesto() {
        try {
            // Load marked.js library
            if (!window.marked) {
                const markedScript = document.createElement('script');
                markedScript.src = 'https://cdn.jsdelivr.net/npm/marked/marked.min.js';
                await new Promise((resolve, reject) => {
                    markedScript.onload = resolve;
                    markedScript.onerror = reject;
                    document.head.appendChild(markedScript);
                });
            }
            
            const response = await fetch('../../data/manifesto.md');
            if (!response.ok) throw new Error('Failed to load manifesto');
            const text = await response.text();
            console.log('Loaded manifesto:', text);
            
            // Add manifesto content to notebook
            const cell = document.querySelector('.jp-Cell');
            if (cell) {
                const markdown = cell.querySelector('.jp-RenderedMarkdown');
                if (markdown) {
                    // Wait for marked to be available
                    if (window.marked) {
                        markdown.innerHTML = marked.parse(text);
                    } else {
                        console.error('marked library not loaded');
                    }
                }
            }
        } catch (error) {
            console.error('Error loading manifesto:', error);
        }
    }

    // Start polling
    pollForHeaders();
</script>
'''

new_style = '''
<style>
    /* Removed chat-related styles */

    /* Mobile markdown rendering and zoom fixes */
    @media (max-width: 768px) {
        /* Prevent zoom on input focus */
        .jp-Notebook .jp-Cell {
            touch-action: manipulation;
            font-size: 16px !important;  /* Prevent iOS auto-zoom */
        }
        
        .jp-InputArea-editor {
            font-size: 16px !important;  /* Prevent iOS auto-zoom */
            touch-action: manipulation;
        }

        .jp-Notebook .jp-Cell .jp-RenderedMarkdown {
            font-size: 16px;
            line-height: 1.4;
            /* Ensure no overlapping or hidden overflow */
            overflow-wrap: break-word;
            padding: 8px;
            max-width: 100%;
            touch-action: manipulation;
        }

        .jp-RenderedMarkdown img {
            max-width: 100%;
            height: auto;
        }

        .jp-RenderedMarkdown pre {
            white-space: pre-wrap;
            word-break: break-word;
            touch-action: manipulation;
        }

        .jp-RenderedMarkdown table {
            display: block;
            overflow-x: auto;
            max-width: 100%;
        }
    }
</style>
'''

# Insert the new script and style after the target script
target_script.insert_after(BeautifulSoup(new_style, 'html.parser'))
target_script.insert_after(BeautifulSoup(new_script, 'html.parser'))

# Save the modified HTML to a new file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(str(soup))

print(f'Modified HTML saved to {output_file_path}')
