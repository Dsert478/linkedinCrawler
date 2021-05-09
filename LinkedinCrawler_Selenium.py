from selenium import webdriver


class LinkedInScraper:

    def __init__(self):
        self.job_list = []
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--headless")
        self.firefox = webdriver.Firefox(firefox_options=firefox_options)

    def scrape_jobs(self):
        self.firefox.get("https://www.linkedin.com/")
        self.firefox.find_element_by_class_name("intent-module__button").click()
        jobs = self.firefox.find_element_by_class_name("jobs-search__results-list").find_elements_by_tag_name("li")
        for job in jobs:
            d = job.find_element_by_class_name("result-card__contents")
            title = d.find_element_by_tag_name("h3").text
            company = d.find_element_by_tag_name("h4").text
            s = d.find_element_by_class_name("result-card__meta")
            location = s.find_element_by_tag_name("span").text
            time_stamp = s.find_element_by_tag_name("time").text
            job_detials = {"title": title,
                           "company": company,
                           "location": location,
                           "time": time_stamp}
            self.job_list.append(job_detials)

        return self.job_list


x = LinkedInScraper()
x.scrape_jobs()