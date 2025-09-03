from jb_60.my_pizzhut_project.pages.deals_page import DealsPage


class TestDeals():

    def test_deals(self, setup_playwright):
        print("lets find out what are the deals")
        page = setup_playwright
        deals_page =DealsPage(page)
        deals_page.find_deals()


        assert 'deals' in page.url, 'Page URL is not as expected after clicking on deals.'

    def test_order_if_first_deal_is_under_10(self, setup_playwright):
        deals_page = DealsPage(setup_playwright)
        deals_page.find_deals()
        first_deal_price = deals_page.get_first_deal_price()


        assert isinstance(first_deal_price, (int, float)), "The extracted price is not a valid number."
        print(f"Successfully extracted price: {first_deal_price}")

        if first_deal_price < 10:
            print(f'first deal price is {first_deal_price}$, which is less than 10$. adding to cart.')
            deals_page.add_first_deal_to_cart()

            assert setup_playwright.locator('button:has-text("View Cart")').is_visible(), "View Cart button is not visible."
        else:
            print(f'first deal is {first_deal_price}$, which is not less than 10$. Skipping')














