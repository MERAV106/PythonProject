from datetime import time



class FindAStorePage:

    def __init__(self,page):
        print('into init')
        self.page=page


    def find_a_store(self,place):
        print ("lets find a store")
        find_a_store_button = self.page.get_by_text("Carryout ")
        find_a_store_button.click()
        store_location=self.page.locator('[id="carryout-city-state-zip"]')
        store_location.fill(place)
        store_location.click()
        button_search=self.page.locator('[class*="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-cont"]')
        button_search.click()

        results_locator=self.page.locator('[class*="MuiPaper-root MuiPaper-elevation MuiPaper-elevation16 MuiDrawer-paper"]')
        results_locator.wait_for()

        results_count = self.page.locator('[class*="MuiPaper-root MuiPaper-elevation MuiPaper-elevation16 MuiDrawer-paper "]').count()
        return results_count
