import scrapy

class Dataspider(scrapy.Spider):
    name = 'agents'
    start_urls = [
        'https://www.bhhsamb.com/bio/FredTichauer'
        # 'https://www.bhhsamb.com/agents'
    ]
    # def start_request(self,response):
    #     links = response.css('a.site-roster-card-image-link::attr(href)').extract()
    #     for link in links:
    #         agent_url = f'https://www.bhhsamb.com/{link}'
    #         yield scrapy.Request(agent_url, callback=self.parse)
    
    def parse(self, response):
                name = response.css('p.rng-agent-profile-contact-name::text').get().strip(),
                job_title = response.css('span.rng-agent-profile-contact-title::text').get(),
                image_url = response.css('img.rng-agent-profile-photo::attr(src)').get(),
                address = response.css('li.rng-agent-profile-contact-address strong::text').get().strip() + response.css('ul.rng-agent-profile-contact li::text').get().strip()
                contact_details = {
                'Office' : response.css('.rng-agent-profile-contact-phone a::attr(href)').get()
                 # cell = response.css(' ::attr(href)').get(),
                 # fax = response.css(' ::attr(href)').get(),
                }
                social_accounts = {
                'facebook' : response.css('li.social-facebook a::attr(href)').get(),
                'twitter' : response.css('li.social-twitter a::attr(href)').get(),
                'linkedin' : response.css('li.social-linkedin a::attr(href)').get(),
                'youtube' : response.css('li.social-youtube a::attr(href)').get(),
                'pinterest' : response.css('li.social-pinterest a::attr(href)').get(),
                'instagram' : response.css('li.social-instagram a::attr(href)').get(),
                }
                
                # offices = response.css('div#team_offices a::text').getall(),
                languages =  ''.join(response.css('p.rng-agent-profile-languages::text').getall()).replace("\xa0"," "),
                description =  ''.join(response.css('div#body-text-1-preview-5500-4537565 >p::text').getall()).replace("\xa0"," ")

                yield {
                "name" : name,
                "job_title" : job_title,
                "image_url" : image_url,
                "address" : address,
                "contact_details" : contact_details,                
                "social_accounts" : social_accounts,        
                # "offices" : office,
                "languages" : languages,
                "description" :  description
            }
            


