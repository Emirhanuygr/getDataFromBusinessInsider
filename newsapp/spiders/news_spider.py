import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"

    start_urls = [
        "https://www.businessinsider.com/sai"
    ]

    def parse(self, response):
        newstitle = response.css("section.river-item.featured-post section div.tout-text-wrapper.default-tout h2 a::text").extract()
        contentlink = response.css("section.river-item.featured-post section div.tout-text-wrapper.default-tout h2 a::attr(href)").extract()
        aciklama = response.css("section.river-item.featured-post section div.tout-text-wrapper.default-tout div::text").extract()
        image = response.css("section.river-item.featured-post section div.tout-image-wrapper.default-tout a div img::attr(src)").extract()
        
        i = 0
        while(i< 30):
            yield {
                "newstitle" : newstitle[i],
                "image" : image[i],
                "contentlink" : "https://www.businessinsider.com/" + contentlink[i],
                "aciklama" : aciklama[i],
            }
            i += 1