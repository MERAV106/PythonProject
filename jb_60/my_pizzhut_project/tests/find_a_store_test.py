import time

from jb_60.my_pizzhut_project.pages.find_a_store_page import FindAStorePage



class TestFindAStore():


    def test_find_a_store(self,setup_playwright):
        print ("lets find a store")
        page = setup_playwright
        find_a_store_page=FindAStorePage(page)

        numbers_of_stores=find_a_store_page.find_a_store("Londonderry, NH")
        assert numbers_of_stores==1, f'No stores found for Londonderry, NH. found{numbers_of_stores}.'
