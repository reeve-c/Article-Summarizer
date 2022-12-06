# 1. Importing Necessary Libraries
from transformers import pipeline
from bs4 import BeautifulSoup
import requests

# 2. Loading the Summarization Pipeline
summarizer = pipeline("summarization")

# 3. Web Scraping using Beautiful Soup
URL = "https://www.slashfilm.com/783792/wait-is-the-batman-the-best-batman-movie/"
r = requests.get(URL)

soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all(['h1', 'p'])

text = [result.text for result in results]
title = text[0]

# 4. Chunking
article = article.replace('.', '.<eos>')
article = article.replace('?', '?<eos>')
article = article.replace('!', '!<eos>')
sentences = article.split('<eos>')


article = ' '.join(text)


chunk_limit = 500
current_chunk = 0 
chunks = []


for sentence in sentences:
    if chunks: 
        if len(chunks[current_chunk]) + len(sentence.split(' ')) <= chunk_limit:
            chunks[current_chunk].extend(sentence.split(' '))
        else:
            current_chunk += 1
            chunks.append(sentence.split(' '))
    else:
        chunks.append(sentence.split(' '))
 
for chunk_index in range(len(chunks)):
    chunks[chunk_index] = ' '.join(chunks[chunk_index])

# 5. Summarization using Hugging Face
res = summarizer(chunks, max_length = 150, min_length = 50, do_sample=False)

# 6. The Result
summary = ''.join([summ['summary_text'] for summ in res])

title += ('\n\n' + summary)
print(title)

with open('article_summary.txt', 'w') as f:
    f.write(title)
