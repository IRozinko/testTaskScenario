from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class InsiderHomePage:
    def __init__(self, driver):
        self.driver = driver

    def open_home_page(self):
        self.driver.get("https://useinsider.com/")


class InsiderNavbar:
    def __init__(self, driver):
        self.driver = driver

    def click_more(self):
        more_menu = self.driver.find_element(By.XPATH, "//*[@id=\"mega-menu-1\"]/span[contains(text(), 'More')]")
        more_menu.click()

    def click_careers(self):
        # careers_link = self.driver.find_element(By.XPATH, "//div[@id='navbarNavDropdown']/ul[1]/li[6]//a["
        #                                                   "@href='https://useinsider.com/careers/']/h5[.='Careers']]")
        careers_link = self.driver.find_element(By.XPATH, "//div[@id='navbarNavDropdown']/ul[1]/li[6]//a["
                                                          "@href='https://useinsider.com/careers/']/p")
        careers_link.click()


class InsiderCareerPage:
    def __init__(self, driver):
        self.driver = driver

    def click_see_all_teams(self):
        see_all_teams_btn = self.driver.find_element(By.XPATH, "/html//section[@id='career-find-our-calling']//a["
                                                               "@href='javascript:void(0)']")
        see_all_teams_btn.click()

    def click_quality_assurance(self):
        quality_assurance_btn = self.driver.find_element(By.XPATH, "/html//section[@id='career-find-our-calling"
                                                                   "']/div[@class='container']/div/div[2]/div["
                                                                   "12]/div[@class='job-title mt-0 mt-lg-2 "
                                                                   "mt-xl-5']/a["
                                                                   "@href='https://useinsider.com/careers/quality"
                                                                   "-assurance/']/h3[.='Quality Assurance']")
        quality_assurance_btn.click()


class InsiderQAJobPage:
    def __init__(self, driver):
        self.driver = driver

    def click_see_all_qa_jobs(self):
        see_all_qa_jobs_btn = self.driver.find_element(By.XPATH, "/html//section[@id='page-head']/div["
                                                                 "@class='container']//a["
                                                                 "@href='https://useinsider.com/careers/open"
                                                                 "-positions/?department=qualityassurance']")
        see_all_qa_jobs_btn.click()

    def filter_jobs_by_location_and_department(self, location, department):
        location_dropdown = self.driver.find_element(By.XPATH, "//select[@id='location']")
        department_dropdown = self.driver.find_element(By.XPATH, "//select[@id='department']")

        location_option = self.driver.find_element(By.XPATH, f"//option[contains(text(), '{location}')]")
        department_option = self.driver.find_element(By.XPATH, f"//option[contains(text(), '{department}')]")

        location_option.click()
        department_option.click()

    def check_presence_of_jobs_list(self):
        jobs_list = self.driver.find_element(By.XPATH, "//ul[contains(@class, 'jobs-list')]")
        return jobs_list.is_displayed()

    def get_jobs(self):
        jobs = self.driver.find_elements(By.XPATH, "//ul[contains(@class, 'jobs-list')]/li")
        return jobs

    def job_contains_text(self, job, text):
        return text in job.text

    def job_has_apply_now_button(self, job):
        try:
            job.find_element(By.XPATH, ".//a[contains(text(), 'Apply Now')]")
            return True
        except NoSuchElementException:
            return False

    def click_apply_now(self, job):
        apply_now_btn = job.find_element(By.XPATH, ".//a[contains(text(), 'Apply Now')]")
        apply_now_btn.click()


class LeverApplicationFormPage:
    def __init__(self, driver):
        self.driver = driver

    def is_at(self):
        try:
            self.driver.find_element(By.XPATH, "//div[contains(@class, 'lever-form')]")
            return True
        except NoSuchElementException:
            return False