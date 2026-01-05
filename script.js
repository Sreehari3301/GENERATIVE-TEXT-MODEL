document.addEventListener('DOMContentLoaded', () => {
    const promptInput = document.getElementById('prompt');
    const lengthInput = document.getElementById('length');
    const lengthVal = document.getElementById('length-val');
    const tempInput = document.getElementById('temperature');
    const tempVal = document.getElementById('temp-val');
    const generateBtn = document.getElementById('generate-btn');
    const resultContainer = document.getElementById('result-container');
    const outputText = document.getElementById('output-text');
    const loader = document.getElementById('loader');
    const copyBtn = document.getElementById('copy-btn');

    // Update range labels
    lengthInput.addEventListener('input', (e) => lengthVal.textContent = e.target.value);
    tempInput.addEventListener('input', (e) => tempVal.textContent = e.target.value);

    // Generate Text
    generateBtn.addEventListener('click', async () => {
        const prompt = promptInput.value.trim();
        if (!prompt) {
            alert('Please enter a topic or starting phrase.');
            return;
        }

        // UI State
        generateBtn.disabled = true;
        loader.style.display = 'block';
        document.querySelector('.btn-text').textContent = 'Architecting...';

        try {
            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    prompt: prompt,
                    length: parseInt(lengthInput.value),
                    temperature: parseFloat(tempInput.value)
                }),
            });

            const data = await response.json();

            if (data.generated_text) {
                outputText.textContent = data.generated_text;
                resultContainer.classList.remove('hidden');
                resultContainer.scrollIntoView({ behavior: 'smooth' });
            } else {
                throw new Error(data.error || 'Failed to generate text');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error generating text: ' + error.message);
        } finally {
            generateBtn.disabled = false;
            loader.style.display = 'none';
            document.querySelector('.btn-text').textContent = 'Architect Paragraph';
        }
    });

    // Copy to clipboard
    copyBtn.addEventListener('click', () => {
        const text = outputText.textContent;
        navigator.clipboard.writeText(text).then(() => {
            const originalText = copyBtn.textContent;
            copyBtn.textContent = 'Copied!';
            copyBtn.style.background = '#2dd4bf';
            setTimeout(() => {
                copyBtn.textContent = originalText;
                copyBtn.style.background = 'rgba(255, 255, 255, 0.1)';
            }, 2000);
        });
    });
});
