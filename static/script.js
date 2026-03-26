async function enhancePrompt() {
    const userPrompt = document.getElementById('userPrompt').value.trim();
    const enhancedPromptArea = document.getElementById('enhancedPrompt');
    const enhanceBtn = document.getElementById('enhanceBtn');
    const copyBtn = document.getElementById('copyBtn');
    const status = document.getElementById('status');

    if (!userPrompt) {
        showStatus('Please enter a prompt to enhance', 'error');
        return;
    }
// basic js
    enhanceBtn.disabled = true;
    copyBtn.disabled = true;
    enhancedPromptArea.value = '';
    showStatus('Enhancing your prompt...', 'loading');

    try {
        const response = await fetch('/enhance', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt: userPrompt })
        });

        const data = await response.json();

        if (response.ok) {
            enhancedPromptArea.value = data.enhanced_prompt;
            copyBtn.disabled = false;
            showStatus('Prompt enhanced successfully!', 'success');
        } else {
            showStatus(data.error || 'An error occurred', 'error');
        }
    } catch (error) {
        showStatus('Network error: ' + error.message, 'error');
    } finally {
        enhanceBtn.disabled = false;
    }
}

function copyToClipboard() {
    const enhancedPrompt = document.getElementById('enhancedPrompt');
    enhancedPrompt.select();
    document.execCommand('copy');
    showStatus('Copied to clipboard!', 'success');
}

function showStatus(message, type) {
    const status = document.getElementById('status');
    status.textContent = message;
    status.className = 'status ' + type;
    
    if (type !== 'loading') {
        setTimeout(() => {
            status.style.display = 'none';
        }, 3000);
    }
}

document.getElementById('userPrompt').addEventListener('keydown', function(e) {
    if (e.ctrlKey && e.key === 'Enter') {
        enhancePrompt();
    }
});
