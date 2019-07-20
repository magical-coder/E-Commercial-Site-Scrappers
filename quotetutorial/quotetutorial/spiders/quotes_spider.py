import scrapy
from ..items import QuotetutorialItem
class QuoteSpider(scrapy.Spider):
	name = 'quotes'
	start_urls = [
		'http://quotes.toscrape.com/'
	]

	def parse(self,response):
		all_div_quotes=response.css('div.quote')

		items = QuotetutorialItem()


		for quotes in all_div_quotes:
			title = quotes.css('span.text::text').extract()
			author = quotes.css('.author::text').extract()
			tag = quotes.css('.tag::text').extract()

			items['title']=title
			items['author']=author
			items['tag']=tag

			yield items
			
		next_page= response.css('li.next a::attr(href)').get()
		print(next_page)
		if next_page is not None:
			yield response.follow(next_page, callback= self.parse)
