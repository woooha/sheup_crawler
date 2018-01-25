import scrapy

from sheup.items import QuestionItem

start_urls = [l.strip() for l in open('questions.txt').readlines()]

class QuestionSpider(scrapy.spiders.Spider):
    name = 'question'
    allowed_domains = ["www.sheup.net"]
    start_urls = start_urls

    def parse(self, response):
        question_item = QuestionItem()

        contents = response.css('.text1_s_info > p:not(.tiku_desc)::text').extract()
        others   = response.css('.tiku_green::text').extract()
        
        question_item['url'] = response.url
        question_item['title'] = contents[0]
        question_item['category'] = others[0]
        question_item['difficulty'] = others[1]
        question_item['answer'] = response.css('.tiku_answer strong::text').extract()
        question_item['options'] = []
        for content in contents[1:]:
            question_item['options'].append(content)

        yield question_item
