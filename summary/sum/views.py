from django.shortcuts import render
from gensim.summarization import summarize

# Create your views here.

def mainlist(request):
    with open("sum/input.txt",mode='r+') as f:
        lines = f.readlines()
        print(lines)
        # sentence_list = [sentence for sentence in lines if not '\n' in sentence]
        # print(sentence_list)
        # sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
        # print(sentence_list)
        article = ' '.join(lines)
        print(article)
        summary = summarize(article, ratio=0.4)
        print(summary)

        return render(request,"home/index.html",context={"summary" : summary})