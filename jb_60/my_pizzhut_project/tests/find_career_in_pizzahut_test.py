from jb_60.my_pizzhut_project.pages.find_career_in_pizzahut_page import FindCareerInPizzahutPage


class TestFindCareerInPizzahut():


    def test_find_career_in_pizzahut(self,setup_playwright):
        print ("lets find a job")
        page = setup_playwright
        find_career_in_pizzahut_page= FindCareerInPizzahutPage(page)
        # find_career_in_pizzahut_page.find_career_in_pizzahut('London,Canada')

        search_count=find_career_in_pizzahut_page.find_career_in_pizzahut('London,Canada')
        assert search_count==0, f'there are no jobs in London,Canada, but got {search_count}.'


