import { Widget } from '@lumino/widgets';

export class ChatWidget extends Widget {
  constructor() {
    super();
    this.addClass('jp-chat-widget');

    // Create chat interface
    const chatDiv = document.createElement('div');
    chatDiv.id = 'chat-interface';
    chatDiv.style.cssText = `
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      background: white;
      border-top: 1px solid #ccc;
      z-index: 1000;
    `;

    chatDiv.innerHTML = `
      <div id="chat-window" style="height:200px; overflow:auto;"></div>
      <input type="text" id="chat-input" style="width:80%;" placeholder="Type a message..."/>
      <button id="send-button">Send</button>
    `;

    this.node.appendChild(chatDiv);

    // Add event listeners
    const input = chatDiv.querySelector('#chat-input') as HTMLInputElement;
    const button = chatDiv.querySelector('#send-button') as HTMLButtonElement;
    const chatWindow = chatDiv.querySelector('#chat-window') as HTMLDivElement;

    button.onclick = () => this.handleMessage(input, chatWindow);
    input.onkeypress = (e) => {
      if (e.key === 'Enter') {
        this.handleMessage(input, chatWindow);
      }
    };
  }

  private handleMessage(input: HTMLInputElement, chatWindow: HTMLDivElement) {
    if (input.value.trim()) {
      const msgDiv = document.createElement('div');
      msgDiv.textContent = input.value;
      chatWindow.appendChild(msgDiv);
      input.value = '';
      chatWindow.scrollTop = chatWindow.scrollHeight;
    }
  }
}
