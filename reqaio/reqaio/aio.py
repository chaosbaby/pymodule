import aiohttp
import asyncio
from fake_useragent import UserAgent

async def fetch(session, url, callback):
    
    async with session.get(url) as response:
        text = await response.text(errors="ignore")
        callback(url, text)


async def send_requests(urls, callback,headers={},cookies={}):
    if not headers:
        headers={"User-Agent": UserAgent().random} 
    async with aiohttp.ClientSession(headers=headers,cookies=cookies) as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(fetch(session, url, callback))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

def run(urls, callback,headers=None,cookies=None):
    asyncio.run(send_requests(urls, callback,headers,cookies))

    
def test():
    ids = range(1, 3)
    urlTemp = "http://www.dpxq.com/hldcg/search/view_m_%d.html"
    urls = [urlTemp % id for id in ids]

    def ubb_crawl_cb(url, data):
        print(data)

    run(urls, ubb_crawl_cb)


if __name__ == "__main__":
    test()
