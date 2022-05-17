from django.shortcuts import render
from .models import Url
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from bs4 import BeautifulSoup
import requests
#import bs4


def index(request):
    return render(request, 'wpmin/index.html')

def contacts(request):
    return render(request, 'wpmin/contacts.html')

def add_url(request):

    #this function extracts text from the url given
    def extract_text(url):
        result = requests.get(url)
        html = BeautifulSoup(result.text, "html.parser")
        counted_sum = html.get_text()           #this gets text from the webpage
        return counted_sum

    #this function counts the number of words in a given text_list, assuming a certain word length
    def count_words_in_text(text_list, word_length):
        total_words = 0
        for current_text in text_list:
            total_words += len(current_text)/word_length
        return total_words

    WORD_LENGTH=5
    WPM=200

    #this func estimates reading time, utilizes the extract func and the total words func
    def estimate_reading_time(url):
        texts = extract_text(url)
        #filtered_text = filter_visible_text(texts) 
        #total_words = count_words_in_text(filtered_text, WORD_LENGTH)
        total_words = count_words_in_text(texts, WORD_LENGTH)
        return float("{:.2f}".format(total_words/WPM))


    #saved_url = Url.objects.get(url_text=request.POST['url_added'])
    #typed_url = request.POST['url_added'] #this fetches data from the name field in html form (test to confirm)
    #url_text = Url.objects.create(url_text=typed_url)
    url_text = Url(url_text=request.POST['url_added'])
    url_text.save()

    processed = estimate_reading_time(url_text)

    return render(request, 'wpmin/index.html', {'processed' : processed})

    #return HttpResponse(print(str(processed)))
    #return HttpResponseRedirect(reverse('wpm:index', args=(processed,)))

def get_contacts(request):

    #extract text from page
    def extract_contacts(url):
        #result = requests.get(url)
        html = requests.get(url).content
  
        # creating soup object
        data = BeautifulSoup(html, 'html.parser')


        temp = data.find(title='Anmelden')
        print(temp.prettify()) 
        
        # finding parent <ul> tag
        parent = data.find("body").find("li")
        
        # finding all <li> tags
        text = list(parent.descendants)
        
        #printing the content in <li> tag
        print(text)
        for i in range(2, len(text), 2):
            print(text[i], end=" ")

    url_text = Url(url_text=request.POST['url_added'])
    url_text.save()

    contact_list = extract_contacts(url_text)

    return render(request, 'wpmin/contacts.html', {'contact_list' : contact_list})