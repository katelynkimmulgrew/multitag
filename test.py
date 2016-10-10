import simplejson
import pytumblr
import math


with open('credentials.json', 'r') as f:
    credentials = simplejson.loads(f.read())
    client = pytumblr.TumblrRestClient(credentials['consumer_key'], credentials['consumer_secret'], credentials['oauth_token'], credentials['oauth_token_secret'])



#firstTag = client.tagged("jane austen", limit=15)
#restOfTags  = ['persuasion','books']

#both = []
#for f in firstTag:
#    if set(restOfTags).issubset(map((lambda str:str.lower()), f["tags"])):
#        both.append(f)
blogHandle = 'janeites'
blogName = blogHandle + ".tumblr.com"
blogDict = client.blog_info(blogName)
print(type(blogDict))
for key, value in blogDict.items():
    print(key, value)
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
numResults = 1
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
            isBreak=True
            break
    if isBreak:
        break
for r in result: 
    print(r["id"])                                
                                                    #for b in both:
                                                    #    print(b['tags'])
