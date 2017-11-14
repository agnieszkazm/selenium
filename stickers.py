import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    browser = webdriver.Chrome(chrome_options=options)
    #print(browser.capabilities)
    request.addfinalizer(browser.quit)
    return browser

def test_stickers(driver):
    driver.implicitly_wait(10)
    driver.get("http://localhost/litecart")

    articleslength = driver.find_elements_by_css_selector("ul.listing-wrapper.products li")
    for i in range(len(articleslength)):
        article=driver.find_elements_by_css_selector("ul.listing-wrapper.products li")[i]
        sticker=len(article.find_elements_by_css_selector("div.image-wrapper > div.sticker"))
        assert sticker == 1
        print(sticker)


