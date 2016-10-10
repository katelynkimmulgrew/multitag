from django.shortcuts import render
import simplejson
import pytumblr
import math

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")

def result(request, page_number):
    with open('myapp/credentials.json', 'r') as f:
            credentials = simplejson.loads(f.read())
            client = pytumblr.TumblrRestClient(credentials['consumer_key'], credentials['consumer_secret'], credentials['oauth_token'], credentials['oauth_token_secret'])
    blogHandle = 'janeites'
    blogName = blogHandle + ".tumblr.com"
    blogDict = client.blog_info(blogName)
    numPosts = blogDict["blog"]["total_posts"]
    numIterations = 0
    if numPosts>20:
        numIterations = int( math.ceil(numPosts/20) )
    else:
        numIterations = 1;
    #postsGrab = client.posts(blogName)
    #posts = postsGrab["posts"]
    #print(type(posts[0]))
    #for key in posts[0]:
    #    print(key)
    tags = ['pride and prejudice','gif']
    result = []
    count = 0
    numResults = 10*page_number
    #print(type(posts))
    #for key in posts:
    #    print(key)

    #print(len(posts))
    #print(posts["total_posts"]
    isBreak = False
    for i in range(0, numIterations):
        offset = 20*i
        postsGrab = client.posts(blogName, offset = offset)
        posts = postsGrab["posts"]
        for p in posts:
            if set(tags).issubset(p["tags"]):
                result.append(p)
                count+=1
            if count==numResults:
                isBreak = True
                break
        if isBreak:
            break

#    return HttpResponse("Page " + page_number + ", First Tag is " + result[0]["tags"][0] )
    newResult = result[-10:]
    context = {'result': newResult, 'page_number': page_number}
    return render(request, 'myapp/result.html', context)
