

class FindCareerInPizzahutPage():

    def __init__(self,page):
        print("into init")
        self.page = page

    def find_career_in_pizzahut(self,place):
        print("lets find job")

        with self.page.context.expect_page() as new_page_event:
            find_career =self.page.locator('[href="https://jobs.pizzahut.com/"]')
            find_career.click()
        self.page = new_page_event.value

        self.page.wait_for_url("**/jobs.pizzahut.com/**")
        self.page.wait_for_selector('[id="filtercategory"]')
        career_position =self.page.locator('[id="filtercategory"]')
        # career_position=self.page.get_by_role("select", name="filter[category][]")
        # career_position.select_option(index=1)
        career_position.select_option(value="Above Restaurant Leader")
        career_location =self.page.locator('[id="searchlocation"]')
        career_location.fill(place)
        career_location.click()
        search_jobs=self.page.locator('[class="Form__button Button Button--primary-light"]')
        search_jobs.click()

        self.page.wait_for_selector('[id="results-counter"]')
        search_results=self.page.locator('[id="results-counter"]').text_content()
        first_word=search_results.split()[0]
        return int(first_word)
