import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from insiders_page import InsiderHomePage, InsiderNavbar, InsiderCareerPage, InsiderQAJobPage, LeverApplicationFormPage

BROWSER = "firefox"  # Change this to "firefox" to run the test in Firefox


class TestInsiderScenario(unittest.TestCase):
    def setUp(self):
        if BROWSER == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.headless = True
            self.driver = webdriver.Chrome(options=chrome_options)
        elif BROWSER == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.headless = True
            self.driver = webdriver.Firefox(options=firefox_options)
        else:
            raise ValueError("Invalid browser specified")

    def test_scenario(self):
        try:
            home_page = InsiderHomePage(self.driver)
            home_page.open_home_page()

            navbar = InsiderNavbar(self.driver)
            navbar.click_more()
            navbar.click_careers()

            career_page = InsiderCareerPage(self.driver)
            career_page.click_see_all_teams()
            career_page.click_quality_assurance()

            qa_job_page = InsiderQAJobPage(self.driver)
            qa_job_page.click_see_all_qa_jobs()
            qa_job_page.filter_jobs_by_location_and_department("Istanbul, Turkey", "Quality Assurance")

            self.assertTrue(qa_job_page.check_presence_of_jobs_list())

            jobs = qa_job_page.get_jobs()
            for job in jobs:
                self.assertTrue(qa_job_page.job_contains_text(job, "Quality Assurance"))
                self.assertTrue(qa_job_page.job_contains_text(job, "Istanbul, Turkey"))
                self.assertTrue(qa_job_page.job_has_apply_now_button(job))

            qa_job_page.click_apply_now(jobs[0])  # Click "Apply Now" for the first job

            lever_application_form_page = LeverApplicationFormPage(self.driver)
            self.assertTrue(lever_application_form_page.is_at())

        except Exception as e:
            self.driver.save_screenshot("failure_screenshot.png")
            raise e

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
