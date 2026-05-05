from playwright.sync_api import expect

def test_auth(page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standart_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.locator("#login-button").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_invalid_user_login(page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("invalid_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.locator("#login-button").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    error = page.locator("h3[data-test='error']")
    expect(error).to_be_visible()
    expect(error).to_contain_text("Epic sadface: Username and password do not match any user in this service")

    
def test_logout_standart_user(page):
    #---Логин---

    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standart_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.locator("#login-button").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    #---Логаут---

    page.locator("#react-burger-menu-btn").click()
    page.locator("#logout_sidebar_link").click()

    #---Проверяем что вернулись на станицу логина

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.locator("#login-button")).to_be_visible()

def test_logout_visual_user(page):

    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("visual_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.locator("#login-button").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


    page.locator("#react-burger-menu-btn").click()
    page.locator("#logout_sidebar_link").click()


    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.locator("#login-button")).to_be_visible()