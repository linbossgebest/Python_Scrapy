import scrapy

from first_scray.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz-odp.org"]
    start_urls = ["https://www.dmoz-odp.org/Health/Addictions/Games/"]

    # def parse(self,response):
    #     filename=response.url.split("/")[-2]
    #     with open(filename,"wb") as f:
    #         f.write(response.body)

    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//*[@id="site-list-content"]')
        items = []
        # sites = sel.xpath(
        #     '//*[@id="site-list-content"]/div').extract()
        # lens = len(sites)
        # print( '//*[@id="site-list-content"]/div[position]/div[3]/a'.replace("position",str(123123123)))

        # for i in range(1,lens+1):
        #     item = DmozItem()
        #     titlePath = '//*[@id="site-list-content"]/div[position]/div[3]/a/div/text()'.replace(
        #         "position", str(i))
        #     item["title"] = sel.xpath(titlePath).extract()
        #     linkPath='//*[@id="site-list-content"]/div[position]/div[3]/a/@href'.replace(
        #         "position", str(i))
        #     item["link"]=sel.xpath(linkPath).extract()
        #     descPath='//*[@id="site-list-content"]/div[position]/div[3]/div/text()'.replace(
        #         "position", str(i))
        #     item["desc"]=sel.xpath(descPath).extract()
        #     items.append(item)
        # return items

        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('.//div/div[3]/a/div/text()').extract()
            item['link'] = site.xpath('.//div/div[3]/a/@href').extract()
            item['desc'] = site.xpath('.//div/div[3]/div/text()').extract()
            items.append(item)

        return items

        # 测试
        # a=list(filter(None,sites))

        # for site in a:
        #     print(site+"123")
