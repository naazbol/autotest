from playwright.sync_api import Playwright, sync_playwright, expect


def test_az(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.get_by_text("LoginAccepted usernames are:standard_userlocked_out_userproblem_userperformance_").click()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.get_by_text("LoginAccepted usernames are:standard_userlocked_out_userproblem_userperformance_").click()
    # page.locator("[data-test=\"password\"]").click()
    # page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("[data-test=\"product_sort_container\"]").select_option("hilo")
    expect (page.get_by_text("Swag Lab")).to_be_visible()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_az(playwright)
