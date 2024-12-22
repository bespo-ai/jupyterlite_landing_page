
<script>
    function removeNotebookHeaders() {
        document.getElementById('top-panel-wrapper')?.remove();
        document.getElementById('menu-panel-wrapper')?.remove();
        document.getElementsByClassName('jp-NotebookPanel-toolbar')[0]?.remove();
    }

    // Initialize notebook and remove chat containers
    function initializeNotebookAndRemoveChat() {
        // Immediately remove chat-related elements
        const chatPatterns = ['step 1:', 'Type a message', 'chat', 'I'll start by importing'];
        const chatSelectors = [
            // Chat-specific elements
            'input[placeholder*="message"]',
            'div[style*="position: fixed"]',
            '*[class*="chat"]',
            '*[id*="chat"]',
            // Input and button elements
            'input[type="text"]',
            'button:not(.jp-Button):not(.jp-ToolbarButtonComponent)',
            // Step and message elements
            'div:contains("step")',
            'div:contains("Step")',
            'div:contains("I'll start by")',
            // Empty elements
            'div:empty:not(.jp-Cell *)',
            'div.lm-Widget:empty:not(.jp-Cell *)',
            // Additional chat-related elements
            '[aria-label*="chat"]',
            '[title*="chat"]',
            '[placeholder*="Type"]',
            // Remove all cells except first two
            '.jp-Cell:nth-child(n+3)'
        ];

        function removeElement(el) {
            try {
                if (el && el.parentNode && !el.closest('.jp-Cell')) {
                    console.log('Removing element:', el.outerHTML.slice(0, 100));
                    el.remove();
                }
            } catch (e) {
                console.error('Error removing element:', e);
            }
        }

        function aggressiveCleanup() {
            console.log('Starting aggressive cleanup');
            
            // Remove all cells except first two
            const notebook = document.querySelector('.jp-Notebook');
            if (notebook) {
                const cells = Array.from(notebook.querySelectorAll('.jp-Cell'));
                cells.slice(2).forEach(cell => cell.remove());
                
                // Ensure remaining cells have correct content
                const expectedCells = [
                    { content: 'import vincent as v', index: 1 },
                    { content: 'help(v)', index: 2 }
                ];
                
                cells.slice(0, 2).forEach((cell, idx) => {
                    const expected = expectedCells[idx];
                    const editor = cell.querySelector('.jp-Editor');
                    if (editor) {
                        editor.querySelector('.CodeMirror-code').innerHTML = `<pre>${expected.content}</pre>`;
                    }
                });
            }

            // Remove chat-related elements
            chatSelectors.forEach(selector => {
                try {
                    document.querySelectorAll(selector).forEach(removeElement);
                } catch (e) {
                    console.error('Selector error:', e);
                }
            });


            // Remove by content patterns
            document.querySelectorAll('*').forEach(el => {
                if (!el.closest('.jp-Cell')) {
                    const text = (el.textContent || '').toLowerCase();
                    if (chatPatterns.some(pattern => text.includes(pattern.toLowerCase()))) {
                        removeElement(el);
                    }
                }
            });
        }

        // Function to ensure notebook cells are properly initialized
        function initializeNotebookCells() {
            // First, remove any existing cells
            document.querySelectorAll('.jp-Cell').forEach(cell => {
                if (!cell.textContent.includes('import vincent as v') && !cell.textContent.includes('help(v)')) {
                    cell.remove();
                }
            });

            // Create cells if they don't exist
            const notebook = document.querySelector('.jp-Notebook');
            if (notebook) {
                const cells = document.querySelectorAll('.jp-Cell');
                if (cells.length !== 2) {
                    // Clear notebook
                    notebook.innerHTML = '';
                    
                    // Create import cell
                    const importCell = document.createElement('div');
                    importCell.className = 'jp-Cell jp-CodeCell';
                    importCell.innerHTML = `
                        <div class="jp-Cell-inputWrapper">
                            <div class="jp-InputArea jp-Cell-inputArea">
                                <div class="jp-InputPrompt jp-InputArea-prompt">[1]:</div>
                                <div class="jp-CodeMirrorEditor jp-Editor">
                                    <div class="CodeMirror cm-s-jupyter">
                                        <div class="CodeMirror-code">
                                            <pre>import vincent as v</pre>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    `;
                    
                    // Create help cell
                    const helpCell = document.createElement('div');
                    helpCell.className = 'jp-Cell jp-CodeCell';
                    helpCell.innerHTML = `
                        <div class="jp-Cell-inputWrapper">
                            <div class="jp-InputArea jp-Cell-inputArea">
                                <div class="jp-InputPrompt jp-InputArea-prompt">[2]:</div>
                                <div class="jp-CodeMirrorEditor jp-Editor">
                                    <div class="CodeMirror cm-s-jupyter">
                                        <div class="CodeMirror-code">
                                            <pre>help(v)</pre>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    `;
                    
                    notebook.appendChild(importCell);
                    notebook.appendChild(helpCell);
                }
            }

            // Ensure all cells are visible
            document.querySelectorAll('.jp-Cell').forEach((cell, index) => {
                cell.style.cssText = 'display: block !important; visibility: visible !important; opacity: 1 !important;';
                
                const prompt = cell.querySelector('.jp-InputPrompt');
                if (prompt) {
                    prompt.textContent = `[${index + 1}]:`;
                }

                const editor = cell.querySelector('.jp-Editor');
                if (editor) {
                    editor.style.cssText = 'visibility: visible !important; display: block !important;';
                }
            });
        }

        // Initial cleanup and cell initialization
        aggressiveCleanup();
        
        // Run cleanup multiple times to catch dynamically added elements
        const cleanupTimes = [0, 100, 500, 1000, 2000, 5000];
        cleanupTimes.forEach(delay => {
            setTimeout(aggressiveCleanup, delay);
        });
        
        // Set up permanent observer for dynamic content
        const observer = new MutationObserver((mutations) => {
            let shouldCleanup = false;
            mutations.forEach(mutation => {
                if (mutation.addedNodes.length > 0 || 
                    mutation.type === 'characterData' ||
                    (mutation.type === 'attributes' && mutation.target.nodeType === 1)) {
                    shouldCleanup = true;
                }
            });
            
            if (shouldCleanup) {
                aggressiveCleanup();
                initializeNotebookCells();
            }
        });

        observer.observe(document.documentElement, {
            childList: true,
            subtree: true,
            characterData: true,
            attributes: true,
            attributeOldValue: true
        });

        console.log('Enhanced notebook initialization and chat removal started');
    }
    
    // Initialize notebook and remove chat when the document is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initializeNotebookAndRemoveChat);
    } else {
        initializeNotebookAndRemoveChat();
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
        // Enhanced Enter key handling for both desktop and mobile
        function executeCellAndSelectNext() {
            // Try multiple methods to execute the cell
            const methods = [
                // Method 1: Click the run button
                () => {
                    const runButton = document.querySelector('.jp-Toolbar-item button[data-command="notebook:run-cell-and-select-next"]');
                    if (runButton) {
                        runButton.click();
                        return true;
                    }
                    return false;
                },
                // Method 2: Trigger the command directly
                () => {
                    const notebook = document.querySelector('.jp-Notebook');
                    if (notebook && window.jupyterapp) {
                        window.jupyterapp.commands.execute('notebook:run-cell-and-select-next');
                        return true;
                    }
                    return false;
                },
                // Method 3: Simulate Shift+Enter keypress
                () => {
                    const event = new KeyboardEvent('keydown', {
                        key: 'Enter',
                        code: 'Enter',
                        shiftKey: true,
                        bubbles: true,
                        cancelable: true
                    });
                    document.activeElement.dispatchEvent(event);
                    return true;
                }
            ];

            // Try each method until one works
            for (const method of methods) {
                if (method()) break;
            }
        }

        // Handle both keydown and keyup events for better mobile support
        ['keydown', 'keyup'].forEach(eventType => {
            document.addEventListener(eventType, function(event) {
                // Only handle Enter key without shift
                if (event.key !== 'Enter' || event.shiftKey) return;

                const activeElement = document.activeElement;
                const cell = activeElement?.closest('.jp-Cell');
                
                // Don't interfere with text input
                if (!cell || activeElement.matches('textarea, input, [contenteditable="true"]')) return;

                // Prevent default only on keydown to avoid double execution
                if (eventType === 'keydown') {
                    event.preventDefault();
                    event.stopPropagation();
                    executeCellAndSelectNext();
                }
            }, true);
        });

        // Add touch event support for mobile
        document.addEventListener('touchend', function(event) {
            const target = event.target;
            const cell = target?.closest('.jp-Cell');
            
            // Check if we're in a cell but not in an input area
            if (cell && !target.matches('textarea, input, [contenteditable="true"]')) {
                // Small delay to allow virtual keyboard events to process
                setTimeout(() => {
                    const activeElement = document.activeElement;
                    if (activeElement === target) {
                        executeCellAndSelectNext();
                    }
                }, 100);
            }
        }, true);

        console.log('Enhanced Enter key and touch handlers installed');
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
