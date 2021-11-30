import requests


r=requests.get("https://en.wikipedia.org/wiki/Main_Page")   #it saves the comtext(sorce code )  of the site in the file obj

print(r.text)    #to print the content saves by obj

#for getting satus code

# print(r.status_code)


# using requests.post
# url="www.something.com"   #this is my sending url
# data={                     #this is my data
#     "pi":4,
#     "p2":5,
# }
# r2=requests.post(url=url,data=data)
# # this will send this to the respective server and give me a response