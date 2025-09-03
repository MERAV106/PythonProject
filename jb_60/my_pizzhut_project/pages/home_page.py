


class homePage():

    def __init__(self,page):
        print("into init")
        self.page = page

    def get_in_the_site(self):
        print("Pizza Hut")
        home_page =self.page.locator('[class="jss8799"]')
        home_page.click()






