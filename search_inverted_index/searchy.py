import re
import string
import gzip
import json

def tokenize(text):
    
    # Define a list of common words and conjunctions to be removed
    common_words = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'did', 'do', 'does', 'doing', 'don', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'itself', 'just', 'me', 'more', 'most', 'my', 'myself', 'no', 'nor', 'not', 'now', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 's', 'same', 'she', 'should', 'so', 'some', 'such', 't', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'you', 'your', 'yours', 'yourself', 'yourselves']
    
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

def build_inverted_index(corpus):
    inverted_index = {}
    for doc_id, doc_text in corpus.items():
        for word in tokenize(doc_text):
            if word not in inverted_index:
                inverted_index[word] = []
            if doc_id not in inverted_index[word]:
                inverted_index[word].append(doc_id)
    return inverted_index


def search_inverted_index(inverted_index,search_word):
    if search_word in inverted_index:
        print(f'The word "{search_word}" appears in the following documents: {inverted_index[search_word]}')
    else:
        print(f'The word "{search_word}" does not appear in any documents.')



def search_index(inverted_index, query):
    words = query.split()
    if len(words) == 0:
        return []
    elif len(words) == 1:
        return inverted_index.get(words[0], [])
    else:
        posting_lists = [set(inverted_index.get(word, [])) for word in words]
        result = set.intersection(*posting_lists)
        return list(result)




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











# Convert dictionary to JSON string
#my_dict_json = json.dumps(ii)

# Compress the JSON string using gzip
#compressed_data = gzip.compress(my_dict_json.encode())/

# Decompress the data and convert back to dictionary
#decompressed_data = gzip.decompress(compressed_data)
#my_dict_again = json.loads(decompressed_data.decode())

#print(my_dict_again)
# Output: {'foo': 42, 'bar': 'hello world'}



