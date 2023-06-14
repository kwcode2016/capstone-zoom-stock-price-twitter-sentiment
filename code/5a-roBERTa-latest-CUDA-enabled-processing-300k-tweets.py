# Summary: Using roBERTa to Label 300K Tweets
# Step 1: load the 300k Zoom Stock Tweets
# Step 2: Load the finetuned roBERTa model
# Step 3: Run the model on CUDA
# Step 4: Save the output to file for the webapp


import pandas as pd

# Load 300K Tweets zm-6-2019-04-01-2022-12-11-all-zm-tweets.jsonl
file_path = 'zm-6-2019-04-01-2022-12-11-all-zm-tweets.jsonl' #full file. 
df = pd.read_json(file_path, lines=True)

print(df.info())

texts = df['content']
texts = list(texts)

print(len(texts))

# WORKING WITH CUDA and adding 300k tweets to test

# code wtih cuda reporting.

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import RobertaTokenizer, RobertaForSequenceClassification

path = 'SAVED_ROBERTA_finetuned_model_CUDA'


# Check if CUDA is available
cuda_available = torch.cuda.is_available()
print("CUDA available:" if cuda_available else "CUDA not available")

# Load the RoBERTa tokenizer and model
model_name = f'cardiffnlp/twitter-roberta-base-sentiment-latest'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = RobertaForSequenceClassification.from_pretrained(path).to("cuda" if cuda_available else "cpu")

# Set the batch size (you may need to adjust this based on your GPU memory)
batch_size = 32

# Function to classify sentiment in a batch of texts
def classify_sentiment(texts_batch):
    # print(texts_batch) #shows the batch of text for sentiment analysis
    encoded_input = tokenizer(texts_batch, padding=True, truncation=True, return_tensors="pt")
    encoded_input = {key: value.to("cuda" if cuda_available else "cpu") for key, value in encoded_input.items()}
    with torch.no_grad():
        logits = model(**encoded_input).logits
    probabilities = torch.softmax(logits, dim=1)
    max_indices = torch.argmax(probabilities, dim=1)
    # Map indices to labels
    labels_map = {0: 'negative', 1: 'neutral', 2: 'positive'}
    labels = [labels_map[index.item()] for index in max_indices]
    return labels

# Process the texts in batches
sentiments = []
num_batches = len(texts) // batch_size + int(len(texts) % batch_size > 0)

for i in range(0, len(texts), batch_size):
    texts_batch = texts[i:i + batch_size]
    sentiments_batch = classify_sentiment(texts_batch)
    sentiments.extend(sentiments_batch)
    
    # Print progress
    batches_completed = i // batch_size + 1
    batches_left = num_batches - batches_completed
    print(f"Batch {batches_completed}/{num_batches} completed. Batches left: {batches_left}")

# Print the first 10 sentiment labels
print(sentiments[:50])

# adding sentiments new column to df
df['sentiment_r_latest'] = sentiments

# saving the full df
df.to_csv('full300k_w_r_latest_sentiment_with_finetuning.csv')

