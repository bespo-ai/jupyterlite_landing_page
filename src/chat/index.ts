import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { ChatWidget } from './widget';

/**
 * A JupyterLab frontend plugin that adds a chat interface
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlite-chat',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    console.log('JupyterLite Chat Plugin is activated!');

    // Create and add the chat widget to the main area
    const widget = new ChatWidget();
    app.shell.add(widget, 'main');
  }
};

export default plugin;
