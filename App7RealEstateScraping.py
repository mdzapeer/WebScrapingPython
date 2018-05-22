
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


r=requests.get('https://ajman.dubizzle.com/search/?keywords=Ajman+Pearl&is_basic_search_widget=1&is_search=1')
c=r.content


# In[3]:


soup=BeautifulSoup(c,"html.parser")
print(soup.prettify())


# In[4]:


all=soup.find_all("div",{"class":"cf item"})


# In[5]:


all[0].find("div",{"class":"price"}).text.replace("\n","").replace(" ","")


# In[20]:


for listing in all:
    try:
        for features in listing.find_all("ul",{"class":"features"}):
            for li in features.find_all("li"):
                if "Bedrooms: " in li:
                    print(li.text)
                    print(li.find("strong").text)
                if "Bathrooms: " in li:
                    print(li.text)
                    print(li.find("strong").text)
                if "Price / SqFt: " in li:
                    print(li.text)
                    print(li.find("strong").text)
                if "Size: " in li:
                    print(li.text)
                    print(li.find("strong").text)
        print(" ")
    except:
        print(None)


# In[6]:


for listing in all:
    print(listing.find("span",{"class":"title"}).text)
    print(listing.find("div",{"class":"price"}).text.replace("\n","").replace(" ",""))
    try:
        print(listing.find_all("ul",{"class":"features"})[0].find_all("li"))
    except:
        print(None)
    try:
        print(listing.find_all("ul",{"class":"features"})[0].find_all("li")[0].find("strong").text)
    except:
        print(None)
    try:
        print(listing.find_all("ul",{"class":"features"})[0].find_all("li")[1].find("strong").text)
    except:
        print(None)  
    try:
        print(listing.find_all("ul",{"class":"features"})[1].find_all("li"))  
    except:
        print(None)
    try:
        print(listing.find_all("ul",{"class":"features"})[1].find_all("li")[0].find("strong").text)
    except:
        print(None)
    try:
        print(listing.find_all("ul",{"class":"features"})[1].find_all("li")[1].find("strong").text)
    except:
        print(None)     


# In[53]:


pages=soup.find_all("span",{"class":"paginator-simple"})[0].find_all("strong")[1].text
pages


# In[61]:


url_part1="https://ajman.dubizzle.com/search/?page="
url_part2="&keywords=Ajman+Pearl&is_basic_search_widget=1&is_search=1"

for page in range(1,int(pages)+1):
    print(url_part1+str(page)+url_part2)


# In[22]:


for listing in all:
    print(listing.find("span",{"class":"title"}).text)
    print(listing.find("div",{"class":"price"}).text.replace("\n","").replace(" ",""))
    try:
        for features in listing.find_all("ul",{"class":"features"}):
            for li in features.find_all("li"):
                if "Bedrooms: " in li:
                    print(li.text)
                    print(li.find("strong").text)
                if "Bathrooms: " in li:
                    print(li.text)
                    print(li.find("strong").text)
                if "Price / SqFt: " in li:
                    print(li.text)
                    print(li.find("strong").text)
                if "Size: " in li:
                    print(li.text)
                    print(li.find("strong").text)
        print(" ")
    except:
        print(None)


# In[62]:


import pandas
import requests
from bs4 import BeautifulSoup


l=[]
r=requests.get('https://ajman.dubizzle.com/search/?keywords=Ajman+Pearl&is_basic_search_widget=1&is_search=1')
c=r.content
soup=BeautifulSoup(c,"html.parser")
pages=soup.find_all("span",{"class":"paginator-simple"})[0].find_all("strong")[1].text
url_part1="https://ajman.dubizzle.com/search/?page="
url_part2="&keywords=Ajman+Pearl&is_basic_search_widget=1&is_search=1"

for page in range(1,int(pages)+1):
    print(url_part1+str(page)+url_part2)
    r=requests.get(url_part1+str(page)+url_part2)
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    
    all=soup.find_all("div",{"class":"cf item"})
    for listing in all:
        d={}
        d["title"]=listing.find("span",{"class":"title"}).text.replace("\n","")
        d["price"]=listing.find("div",{"class":"price"}).text.replace("\n","").replace(" ","")
        try:
            for features in listing.find_all("ul",{"class":"features"}):
                for li in features.find_all("li"):
                    if "Bedrooms: " in li:
                        #print(li.text)
                        d["Bedrooms"]=li.find("strong").text
                    if "Bathrooms: " in li:
                        #print(li.text)
                        d["Bathrooms"]=li.find("strong").text
                    if "Price / SqFt: " in li:
                        #print(li.text)
                        d["Price/Sqft"]=li.find("strong").text
                    if "Size: " in li:
                        #print(li.text)
                        d["Size"]=li.find("strong").text

            #print(" ")
        except:
            None
        l.append(d)

df=pandas.DataFrame(l)
df.to_csv("extract.csv")

