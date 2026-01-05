from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from transformers import pipeline, set_seed
import torch

app = Flask(__name__, static_url_path='', static_folder='.', template_folder='.')
CORS(app)

# Initialize the generator globally for reuse
print("Loading model... this might take a moment.")
generator = pipeline('text-generation', model='gpt2', framework='pt')
set_seed(42)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    max_length = int(data.get('length', 150))
    temperature = float(data.get('temperature', 0.7))

    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    print(f"--- Received generation request for prompt: {prompt[:50]}...")
    try:
        results = generator(
            prompt,
            max_new_tokens=max_length, # Use max_new_tokens to avoid conflict with max_length
            num_return_sequences=1,
            truncation=True,
            temperature=temperature,
            top_k=50,
            top_p=0.95,
            pad_token_id=50256
        )
        generated_text = results[0]['generated_text']
        print(f"--- Generation successful result length: {len(generated_text)}")
        return jsonify({'generated_text': generated_text})
    except Exception as e:
        print(f"--- Generation error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
