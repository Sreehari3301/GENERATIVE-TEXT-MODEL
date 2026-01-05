# Coherent Text Generation Model

This project provides a pre-trained transformer-based model (GPT-2) to generate coherent paragraphs based on specific topics.

## Components
- `text_generator.ipynb`: Interactive notebook for experimentation.
- `generator.py`: CLI script for command-line generation.
- `app.py`: Flask backend for the web interface.
- `index.html`: Premium web interface (requires `app.py`).

## Web Interface (Recommended)
This provides a beautiful, modern UI to interact with the model.
1. Start the server:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to `http://127.0.0.1:5000`

## CLI Usage
Run the script directly from your terminal:
```bash
python generator.py --prompt "Your topic here"
```

## Getting Started
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Open `text_generator.ipynb` in your preferred notebook editor (VS Code, Jupyter, Google Colab).
3. Run the cells to see the demonstration.

## Example Topics Provided
- Artificial Intelligence in Healthcare
- Mars Exploration
- Sustainable Energy
- Social Media Impact
