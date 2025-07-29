import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

async def main():
    url = 'https://www.wantgoo.com/stock/2330/technical-chart'
    #url = 'https://www.wantgoo.com/stock/2317/technical-chart'
    #建立一個BrowserConfig,讓chromium的瀏覽器顯示
    #BrowserConfig實體
    browser_config = BrowserConfig(
        headless=False
    )
    # 建立一個AsyncWebCrawler的實體，並傳入BrowserConfig實體
    # 這樣可以讓爬蟲等待瀏覽器載入頁面，並且可以在瀏覽器中看到爬蟲的操作，方便除錯
    run_config = CrawlerRunConfig(
        wait_for_images=True,  # 等待圖片載入
        scan_full_page=True,  # Tells the crawler to try scrolling the entire page
        scroll_delay=0.5,     # Delay (seconds) between scroll steps
        #page_timeout=800000,               # 80秒超時
        #js_code=["document.querySelector('.my-drawer-toggle-btn').click();"],
        cache_mode=CacheMode.BYPASS,
        verbose=True
    )
    # 使用AsyncWebCrawler的實體來爬取網頁
    # 加入run_config參數
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=url,config=run_config)
        print(result.markdown) #

if __name__ == '__main__':
    asyncio.run(main())
    