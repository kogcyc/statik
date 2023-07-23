import re
import requests
import string

def tokenize(text):
    
    # Define a list of common words and conjunctions to be removed
    common_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'person', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us']
    
    # Make lower case
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove digits
    # text = re.sub('\d+', '', text)
    
    # Split the text into words using regular expressions
    words = re.findall(r'\b\w+\b', text)
    
    # Remove any words that are less than three characters long or in the common words list
    words = [word for word in words if len(word) > 2 and word not in common_words]
    
    return words



url = 'https://kogcyc.github.io/files/corpus.dict'
response = requests.get(url)

if response.status_code == 200:
    corpus = response.json()
    # do something with the json_data
else:
    print(f'Request failed with status code {response.status_code}')

#text1 = "This is a long string of text that we want to tokenize. It includes punctuation and other characters, so we'll need to use regular expressions to split it into words. Additionally, we'll remove common words and conjunctions."
#text2 = "Once upon a time there lived a characters who was not very interesting."
#words = tokenize(text)
#print(words)

#corpus = {
#    'doc1': text1,
#    'doc2': text2,
#    'doc3': 'This is the third document.'
#}

def build_inverted_index(corpus):
    inverted_index = {}
    for doc_id, doc_text in corpus.items():
        for word in tokenize(doc_text):
            if word not in inverted_index:
                inverted_index[word] = []
            if doc_id not in inverted_index[word]:
                inverted_index[word].append(doc_id)
    return inverted_index

inverted_index = build_inverted_index(corpus)
print(inverted_index)

search_word = 'example'

if search_word in inverted_index:
    print(f'The word "{search_word}" appears in the following documents: {inverted_index[search_word]}')
else:
    print(f'The word "{search_word}" does not appear in any documents.')




#const inv = "{'long': ['doc1'], 'string': ['doc1'], 'text': ['doc1'], 'tokenize': ['doc1'], 'includes': ['doc1'], 'punctuation': ['doc1'], 'characters': ['doc1', 'doc2'], 'need': ['doc1'], 'regular': ['doc1'], 'expressions': ['doc1'], 'split': ['doc1'], 'words': ['doc1'], 'additionally': ['doc1'], 'remove': ['doc1'], 'common': ['doc1'], 'conjunctions': ['doc1'], 'once': ['doc2'], 'upon': ['doc2'], 'lived': ['doc2'], 'was': ['doc2'], 'very': ['doc2'], 'interesting': ['doc2'], 'third': ['doc3'], 'document': ['doc3']}"

#const searchWord = 'documents';

#if (searchWord in inv) {
#  console.log(`The word "${searchWord}" appears in the following documents: ${invertedIndex[searchWord]}`);
#} else {
#  console.log(`The word "${searchWord}" does not appear in any documents.`);
#}





#function tokenize(text) {
#  text = text.toLowerCase();
#  text = text.replace(/[^\w\s]/g, ''); // Remove punctuation
#  const words = text.match(/\b\w+\b/g); // Split the text into words using regular expressions
#  return words;
#}









import gzip
import json


# Convert dictionary to JSON string
my_dict_json = json.dumps(ii)

# Compress the JSON string using gzip
compressed_data = gzip.compress(my_dict_json.encode())

# Decompress the data and convert back to dictionary
decompressed_data = gzip.decompress(compressed_data)
my_dict_again = json.loads(decompressed_data.decode())

print(my_dict_again)
# Output: {'foo': 42, 'bar': 'hello world'}



