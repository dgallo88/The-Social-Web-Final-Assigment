from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from hashtag_by_country import hashtag_by_country
from hashtag_comparison import hashtag_comparison
from keyword_twitter_vs_reddit import keyword_twitter_vs_reddit
from two_keywords_twitter_and_reddit import two_keywords_twitter_and_reddit


def index(request):
   # hashtag = request.GET['hashtag']
    # context =  {'hashtag': hashtag}
    return render(request, 'polls/index.html',  )
    #return HttpResponse("Hello, world. You're at the polls index." + hashtag)

def countryform(request):
    return render(request, 'polls/countryform.html', )
    #return HttpResponse("Hello, world. You're at the polls index." + hashtag)

def countryanalysis(request):
    hashtag = request.GET['hashtag']
    #hashtag = "happy"
    # context =  {'hashtag': hashtag}
    hashtag_by_country(q=hashtag)
    return render(request, 'polls/countryform.html', )
    #return HttpResponse("Hello, world. You're at the polls index." + hashtag)

def twohashtagfrecuencyform(request):
    return render(request, 'polls/twohashtagform.html', )

def twohashtagfrecuencyanalisis(request):
    hashtag1 = request.GET['hashtag1']
    hashtag2 = request.GET['hashtag2']

    hashtag_comparison(q1=hashtag1, q2=hashtag2)

    return render(request, 'polls/twohashtagform.html', )

def countrytwohashtagform(request):
      return render(request, 'polls/twohashtagcountryform.html', )

def countrytwohashtaganalisis(request):
    hashtag1 = request.GET['hashtag1']
    hashtag2 = request.GET['hashtag2']
    country= request.GET['country']
    print '***************************'
    print hashtag1
    print hashtag2
    print country

    hashtag_comparison(q1=hashtag1, q2=hashtag2, loc= country)

    return render(request, 'polls/twohashtagcountryform.html', )

def keywordintwitterandredditform(request):
     return render(request, 'polls/keywordintwitterandredditform.html', )


def keywordintwitterandredditanalisis(request):

    keyword = request.GET['keyword']
    keyword_twitter_vs_reddit(keyword)

    return render(request, 'polls/keywordintwitterandredditform.html', )

def twokeywordintwitterandredditform(request):
     return render(request, 'polls/twokeywordintwitterandredditform.html', )

def twokeywordintwitterandredditanalisis(request):

    keyword1 = request.GET['keyword1']
    keyword2 = request.GET['keyword2']

    two_keywords_twitter_and_reddit(keyword1, keyword2)

    return render(request, 'polls/twokeywordintwitterandredditform.html', )