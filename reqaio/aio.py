import aiohttp
import asyncio
from fake_useragent import UserAgent

async def fetch(session, url, callback):
    async with session.get(url, headers={"User-Agent": UserAgent().random}) as response:
        data = await response.content.read()
        callback(url, data)


async def send_requests(urls, callback):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(fetch(session, url, callback))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

def run(urls, callback):
    asyncio.run(send_requests(urls, callback))

    
def test():
    ids = range(1, 3)
    urlTemp = "http://www.dpxq.com/hldcg/search/view_m_%d.html"
    urls = [urlTemp % id for id in ids]
    print(urls)

    def ubb_crawl_cb(url, data):
        print(url)
        print(data)

    run(urls, ubb_crawl_cb)


if __name__ == "__main__":
    test()
