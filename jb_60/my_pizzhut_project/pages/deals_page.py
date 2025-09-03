
import re

class DealsPage():


    def __init__(self,page):
        print('into init')
        self.page=page

    def find_deals(self):
        print("lets find out what are the deals")
        deals_button = self.page.locator('[data-testid="link-nav-deals"]')
        deals_button.click()
        self.page.wait_for_url('**/deals')

    def get_first_deal_price(self):

        first_deal_card = self.page.locator('[data-testid*="menu-tile-container"]').first
        first_deal_card.wait_for()

        full_text = first_deal_card.inner_text()
        print(f"Full text of first deal card: {full_text}") # הדפסת הטקסט לצרכי ניפוי באגים

        price_match = re.search(r'\d+(\.\d+)?', full_text)

        if price_match:
           price_as_number = float(price_match.group(0))
           print(f"Extracted price: {price_as_number}")  # הדפסת המחיר שחולץ
        else:
            raise ValueError("Could not find a valid price in the text.")


        return price_as_number



