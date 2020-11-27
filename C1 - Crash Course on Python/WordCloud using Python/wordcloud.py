import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys
def _upload():
    _upload_widget = fileupload.FileUploadWidget()
    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()
    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()


def calculate_frequencies(file_contents):
    ans=[]
    final={}
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is","in","for", "than", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # LEARNER CODE START HERE

    for words in file_contents.split():
        if words.isalpha() and words.lower() not in uninteresting_words:
            ans.append(words.lower())
    for words in ans:
        if words not in final:
            final[words] = 1
            final[words]+=file_contents.split().count(words) -1
    return final



# Display your wordcloud image
t=calculate_frequencies(file_contents)
cloud = wordcloud.WordCloud().generate_from_frequencies(t)
plt.imshow(cloud, interpolation = 'nearest')
plt.axis('off')
plt.show()
