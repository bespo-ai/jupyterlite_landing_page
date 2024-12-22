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

    function typeText(element, text, delay = 50) {
        let i = 0;
        return new Promise((resolve) => {
            const interval = setInterval(() => {
                if (i < text.length) {
                    element.value += text.charAt(i);
                    i++;
                } else {
                    clearInterval(interval);
                    resolve();
                }
            }, delay);
        });
    }

    function addChatInterface() {
        // Function to hide all cells except the first one
        function hideNonHeroCells() {
            const cells = document.querySelectorAll('.jp-Cell');
            for (let i = 1; i < cells.length; i++) {
                cells[i].style.display = 'none';
            }
        }

        const addCell = document.querySelector('button.jp-Notebook-footer');
        addCell.style.marginBottom = "50px";

        // Wait for notebook cells to load and hide non-hero cells
        const checkNotebook = setInterval(() => {
            const cells = document.querySelectorAll('.jp-Cell');
            if (cells.length > 0) {
                clearInterval(checkNotebook);
                hideNonHeroCells();
            }
        }, 100);

        const chatInterface = document.createElement('div');
        chatInterface.id = 'chat-interface';
        
        // Create step message
        const stepMessage = document.createElement('div');
        stepMessage.className = 'step-message';
        stepMessage.textContent = "step 1: I'll start by importing ..";
        chatInterface.appendChild(stepMessage);
        
        chatInterface.innerHTML += `
            <div class="chat-container">
                <input type="text" id="chat-input" placeholder="Type a message..." />
                <div style="display: flex; align-items: end; padding: 15px;">
                    <button class="send-button">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512">
                            <path d="M214.6 41.4c-12.5-12.5-32.8-12.5-45.3 0l-160 160c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L160 141.2 160 448c0 17.7 14.3 32 32 32s32-14.3 32-32l0-306.7L329.4 246.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3l-160-160z"/>
                        </svg>
                    </button>
                </div>
            </div>
        `;
        addCell.parentNode.insertBefore(chatInterface, addCell.nextSibling);
        
        // Start typing animation after a short delay
        setTimeout(async () => {
            const chatInput = document.getElementById('chat-input');
            await typeText(chatInput, "I'm trying to get users excited. Please analyze Vincent's unique features and use cases...", 50);
            // Highlight send button after typing completes
            const sendButton = document.querySelector('.send-button');
            sendButton.classList.add('send-button-highlight');
            
            // Add click handler to send button to show and run cells
            sendButton.addEventListener('click', () => {
                // Show all cells
                const cells = document.querySelectorAll('.jp-Cell');
                for (let i = 1; i < cells.length; i++) {
                    cells[i].style.display = '';
                }
                
                // Find and click all run buttons for each cell
                const runButtons = document.querySelectorAll('.jp-RunIcon');
                runButtons.forEach(button => {
                    button.click();
                });
            });
            
            // Add new cell with import pandas
            const addCellButton = document.querySelector('button.jp-Notebook-footer');
            if (addCellButton) {
                addCellButton.click();
                // Wait for the new cell to be created
                setTimeout(() => {
                    const cells = document.querySelectorAll('.jp-Cell-inputArea');
                    const lastCell = cells[cells.length - 1];
                    if (lastCell) {
                        const editor = lastCell.querySelector('.jp-Editor');
                        if (editor) {
                            editor.textContent = 'import pandas';
                        }
                    }
                }, 500);
            }
        }, 1000);
    }

    function setDarkTheme() {
        // Let JupyterLab Night theme handle dark mode
        // This function is kept for potential future theme-related needs
        console.log('Using JupyterLab Night theme');
    }

    function triggerInitialScroll() {
        // Minimal scroll to trigger notebook render without visible movement
        window.scrollBy({
            top: 1,
            behavior: 'instant'
        });
    }

    function changeKeyboardShortcuts() {
        // Wait for Jupyter notebook to be fully initialized
        if (window.jupyter && window.jupyter.notebook) {
            // Replace Shift+Enter with Enter for running cells
            const runShortcut = {
                command: 'notebook:run-cell-and-select-next',
                keys: ['Enter'],
                selector: '.jp-Notebook:focus'
            };
            
            // Remove old shortcut and add new one
            try {
                const commandRegistry = window.jupyter.commands;
                if (commandRegistry) {
                    // Remove the old Shift+Enter binding
                    commandRegistry.removeKeyBinding('shift-enter');
                    // Add the new Enter binding
                    commandRegistry.addKeyBinding(runShortcut);
                    
                    // Add direct keydown event listener for mobile compatibility
                    document.addEventListener('keydown', (event) => {
                        if (event.key === 'Enter' && !event.shiftKey) {
                            const activeCell = document.querySelector('.jp-Notebook-cell.jp-mod-active');
                            if (activeCell && document.activeElement.tagName !== 'INPUT') {
                                event.preventDefault(); // Prevent default only when we're handling it
                                const runButton = activeCell.querySelector('.jp-RunIcon');
                                if (runButton) {
                                    runButton.click();
                                }
                            }
                        }
                    }, { capture: true }); // Use capture to handle event before default handlers
                }
            } catch (error) {
                console.warn('Failed to update keyboard shortcuts:', error);
            }
        } else {
            // Retry after a short delay if Jupyter is not ready
            setTimeout(changeKeyboardShortcuts, 100);
        }
    }

    function pollForHeaders() {
        if (document.querySelector('button.jp-Notebook-footer')) {
            removeNotebookHeaders();
            setDarkTheme();
            addChatInterface();
            // Trigger initial scroll after a short delay to ensure content is loaded
            setTimeout(triggerInitialScroll, 1000);
            // Initialize keyboard shortcuts
            changeKeyboardShortcuts();
        } else {
            setTimeout(pollForHeaders, 50);
        }
    }

    // Start polling
    pollForHeaders();
</script>
'''

new_style = '''
<style>
    #chat-interface {
        position: fixed;
        left: 0;
        bottom: 0;
        width: calc(100% - 54px);
        background: transparent;
        margin: 0;
        padding: 0 20px 20px 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 10000;
    }

    .step-message {
        color: var(--jp-content-font-color1);
        margin-bottom: 10px;
        font-style: italic;
        background-color: var(--jp-layout-color2);
        padding: 8px 16px;
        border-radius: 8px;
    }

    .chat-container {
        display: flex;
        justify-content: space-between;
        max-width: 800px;
        background-color: var(--jp-layout-color2);
        border-radius: 30px;
        width: 100%;
        color: var(--jp-content-font-color1);
        min-height: 100px;
    }

    #chat-input {
        border: 0;
        color: var(--jp-content-font-color1);
        border-radius: 30px;
        background-color: var(--jp-layout-color2);
        max-width: calc(100vw - 20px);
        width: calc(100% - 150px);
        padding: 10px;
        margin: 0 10px;
        z-index: 100000;
    }

    input#chat-input::placeholder {
        color: var(--jp-content-font-color3);
    }

    .send-button {
        border-radius: 50%;
        width: 30px;
        height: 30px;
        border: none;
        padding: 3px 6px 6px 6px;
        transition: box-shadow 0.3s ease;
    }

    .send-button-highlight {
        box-shadow: 0 0 10px rgba(0, 255, 0, 0.8);
    }

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
