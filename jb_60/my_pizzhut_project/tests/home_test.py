from operator import contains

from jb_60.my_pizzhut_project.pages.home_page import homePage


class TestHome():


    def test_go_in_the_site(self,setup_playwright):
        print("Going to Pizza Hut")
        page = setup_playwright
        home_page =homePage(page)




        assert page.url == 'https://www.pizzahut.com/', 'page URL is not as expected after login'


