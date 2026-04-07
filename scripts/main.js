/**
 * Raymond A. Mason School of Business - AI for Skeptics Course
 * Basic JavaScript for interactive elements
 */

document.addEventListener('DOMContentLoaded', () => {
    console.log('AI for Skeptics Course website loaded successfully.');

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Add visual feedback to download buttons
    const downloadBtns = document.querySelectorAll('.btn-secondary');
    downloadBtns.forEach(btn => {
        if (btn.innerText.includes('Download')) {
            btn.addEventListener('click', () => {
                console.log('Download initiated for:', btn.innerText);
                // In a real app, this would trigger the actual file download
            });
        }
    });

    // Consolidated Chat Logic
    const setupChat = (inputSelector, sendSelector, messagesSelector, buttonSelector, windowSelector, closeSelector) => {
        const chatInput = document.getElementById(inputSelector);
        const sendChat = document.getElementById(sendSelector);
        const chatMessages = document.getElementById(messagesSelector);
        const chatButton = document.getElementById(buttonSelector);
        const chatWindow = document.getElementById(windowSelector);
        const closeChat = document.getElementById(closeSelector);

        if (!chatInput || !sendChat || !chatMessages) return;

        if (chatButton && chatWindow) {
            chatButton.addEventListener('click', () => {
                chatWindow.classList.toggle('hidden');
            });
            if (closeChat) {
                closeChat.addEventListener('click', () => {
                    chatWindow.classList.add('hidden');
                });
            }
        }

        const appendMessage = (text, type) => {
            const msgDiv = document.createElement('div');
            msgDiv.className = `message ${type}`;
            
            if (type === 'agent' && typeof marked !== 'undefined') {
                msgDiv.innerHTML = marked.parse(text);
            } else {
                msgDiv.innerText = text;
            }
            
            chatMessages.appendChild(msgDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
            return msgDiv;
        };

        const createLoadingIndicator = () => {
            const indicator = document.createElement('div');
            indicator.className = 'typing-indicator';
            indicator.innerHTML = '<div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div>';
            chatMessages.appendChild(indicator);
            chatMessages.scrollTop = chatMessages.scrollHeight;
            return indicator;
        };

        const handleSend = async () => {
            const message = chatInput.value.trim();
            if (message) {
                appendMessage(message, 'user');
                chatInput.value = '';

                const loadingIndicator = createLoadingIndicator();

                try {
                    const response = await fetch('/chat', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ message })
                    });
                    const data = await response.json();
                    
                    loadingIndicator.remove();

                    if (data.response) {
                        appendMessage(data.response, 'agent');
                    } else if (data.error) {
                        appendMessage(`Error: ${data.error}`, 'system');
                    }
                } catch (error) {
                    loadingIndicator.remove();
                    console.error('Chat error:', error);
                    appendMessage('Sorry, something went wrong. Please try again.', 'system');
                }
            }
        };

        sendChat.addEventListener('click', handleSend);
        chatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                handleSend();
            }
        });
    };

    // Setup Floating Chat
    setupChat('chat-input', 'send-chat', 'chat-messages', 'chat-button', 'chat-window', 'close-chat');
    
    // Setup Full Page Assistant
    setupChat('full-chat-input', 'full-send-chat', 'full-chat-messages');
});
