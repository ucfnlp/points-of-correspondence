import os
import vis_functions
import json
from tqdm import tqdm

# Directory to write HTML visuailizations
visualizations_dir = 'PoC_visualizations'
if not os.path.exists(visualizations_dir):
    os.makedirs(visualizations_dir)

# Load Points of Correspondence dataset as JSON
with open('PoC_dataset.json', encoding='utf-8') as f:
    examples = json.load(f)

for example_idx, example in enumerate(tqdm(examples)):
    # Split Article and Summary into tokenized sentences
    article_sent_tokens = [sent.strip().split(' ') for sent in example['Full_Article'].split('\t')]
    summary_sent_tokens = [sent.strip().split(' ') for sent in example['Full_Summary'].split('\t')]
    sent1_idx = example['Sentence_1_Index']
    sent2_idx = example['Sentence_2_Index']
    fused_sent_idx = example['Sentence_Fused_Index']
    pocs = example['PoCs']

    # Create HTML with highlight Points of Correspondence
    extracted_sents_in_article_html = vis_functions.html_highlight_poc(summary_sent_tokens, article_sent_tokens, sent1_idx, sent2_idx, fused_sent_idx, pocs)

    # Write HTML to file
    vis_functions.write_highlighted_html(extracted_sents_in_article_html, visualizations_dir, example_idx)