##  ##

## what it is about
a small lib to asyncly make request and get results

## what it is for
for me to use it as a async crawler

## what is the requires
aiohttp
fake_useragent

## how to install it
pip install -e .

## how to use it
with all the urls 
and callback function to deal with the results



## comparison with others
  pass

## examples the way to use it
 ``` py
from reqaio import aio
urls = ['http://www.baidu.com', 'http://www.baidu.com']
def aio_cb(url,data):
  print(url)
  print(data)
aio.run(urls,aio_cb)
```

## some recommendations
  pass

