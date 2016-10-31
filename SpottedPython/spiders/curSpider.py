import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "curSpider"
    start_urls = [
        'http://www.thecurrent.org/playlist/2016-10-17',
    ]

    def cleanSong(self,str):
        newStr = str[:-9]
        return newStr

    def cleanArtist(self,str):
        newStr = str[:-7]
        return newStr

    def parse(self, response):
        for quote in response.css("article.row.song"):
            yield {

                'song': self.cleanSong(quote.css("h5.title::text").extract_first()),
                'artist': self.cleanArtist(quote.css("h5.artist::text").extract_first())

            }



        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
