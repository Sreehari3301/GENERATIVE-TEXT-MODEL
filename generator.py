import torch
from transformers import pipeline, set_seed
import argparse

def generate_coherent_paragraph(topic_prompt, max_length=150, temperature=0.7):
    """
    Generates a coherent paragraph based on a topic prompt using GPT-2.
    """
    print(f"Loading model and generating text for: '{topic_prompt}'...\n")
    
    # Initialize the text generation pipeline with PyTorch framework
    generator = pipeline('text-generation', model='gpt2', framework='pt')
    set_seed(42)

    results = generator(
        topic_prompt, 
        max_length=max_length, 
        num_return_sequences=1, 
        truncation=True,
        temperature=temperature,
        top_k=50,
        top_p=0.95,
        pad_token_id=50256
    )
    
    return results[0]['generated_text']

def main():
    parser = argparse.ArgumentParser(description="Generate coherent paragraphs on specific topics.")
    parser.add_argument("--prompt", type=str, help="The topic or starting sentence for the paragraph.")
    parser.add_argument("--length", type=int, default=150, help="Maximum length of the generated text.")
    parser.add_argument("--temp", type=float, default=0.7, help="Creativity temperature (0.0 to 1.0).")
    
    args = parser.parse_args()

    if args.prompt:
        output = generate_coherent_paragraph(args.prompt, args.length, args.temp)
        print("--- Generated Text ---")
        print(output)
    else:
        # Default demonstration if no prompt is provided
        default_prompt = "The integration of renewable energy into the power grid is essential because"
        output = generate_coherent_paragraph(default_prompt)
        print("--- Demo Generated Text ---")
        print(output)

if __name__ == "__main__":
    main()
