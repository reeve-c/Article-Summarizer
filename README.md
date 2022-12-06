# Article-Summarizer
I implmented a model to summarize blogposts and articles using the Hugging Face Library and some Natural Language Processing Techniques.

## Web Scraping
Web scraping (or data scraping) is a technique that is used to collect data from websites. I used Beautiful Soup to extract all the titles and subtitles along with their coressponding paragraphs from the desired website.

## Chunking
There is a maximum limit of a sequence that Summarization pipeline can process at once. So, we need to break the article into pieces of 500 words each. For this, we performed chunking and broke the text into individual chunks of size within the maximum limit, in order to achieve the most optimum results.

## Summarization
To Summarize the article (or blogpost) we imported and intialized the Summarization Model from the Hugging Face Library. I found that this model summarized the articles in the most natural manner while preserving its important information.
