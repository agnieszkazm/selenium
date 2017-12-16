from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u"I am on '{url}' page")
def start_page(context, url):
    context.driver.get(url)


@when(u"I type '{text}' in '{input}' input field")
def login(context, text, input):
    wait = WebDriverWait(context.driver, 10)
    login = context.driver.find_element_by_name('input_id'.format(input_id=input))
    login.send_keys(text)

@when(u"I click '{zaloguj}' button")
    context.driver.find_element_by_css_selector('zaloguj_id'.format(zaloguj_id=zaloguj)).click()

@then(u"I am on new page with title '{text}'")
    assert wait.until(EC.title_is(text))

@when(u"I am browsing menu")
def step_impl(context)
    menulenght = context.driver.find_elements_by_css_selector("ul#box-apps-menu li")
    submenulength = 0
    context.menuheaderList = []
    context.submenuheaderList = []
    for i in range(len(menulenght)):
        menu = context.driver.find_elements_by_css_selector("ul#box-apps-menu li")[i+submenulength].click()
        submenulength = len(context.driver.find_elements_by_css_selector('ul#box-apps-menu ul li'))
        header1 = context.driver.find_element_by_css_selector("h1").text
        context.menuheaderList.append(header1)

        for j in range(submenulength):
            submenu = context.driver.find_element_by_css_selector("ul#box-apps-menu ul li:nth-child(" + str(j + 1) + ")").click()
            header2 = context.driver.find_element_by_css_selector("h1").text
            context.submenuheaderList.append(header2)

    return (context.submenuheaderList, context.menuheaderList)

@then(u"I get header of subpage")
def step_impl(context):
    print(context.submenuheaderList, context.menuheaderList)


@when(u"I click on '{menu_element}' menu element")
def step_impl(context, menu_element)
    driver.find_element_by_css_selector('menu_element_id'.format(menu_element_id=menu_element)).click()


@when(u"I check status '{status_radio_button}' of radio button '{element_radio_button}'")
def step_impl(context, status_radio_button, element_radio_button)
    enable_check = driver.find_element_by_xpath('element_radio_button_id'.format(element_radio_button_id=element_radio_button)).get_attribute('status_radio_button_id'.format(status_radio_button_id=element_radio_button))
    if enable_check in (None, False):
        enable = driver.find_element_by_xpath(element_radio_button_id,format(element_radio_button_id=element_radio_button)).click()


    name = driver.find_element_by_css_selector('tbody [name="name[en]"]').send_keys("SuperDuck" + Keys.TAB + "SD")
    prod_group = driver.find_element_by_xpath(".//*[@id='tab-general']/table/tbody/tr[7]/td/div/table/tbody/tr[2]/td[1]/input").click()
    quantity = driver.find_element_by_css_selector("tbody [name=quantity]").send_keys("100")
    date_from = driver.find_element_by_css_selector("tbody [name=date_valid_from]").send_keys("11/17/2017" + Keys.TAB + "12/31/2017")

# Information tab
    info_tab = driver.find_element_by_css_selector('form [href="#tab-information"]').click()
    manufacturer = driver.find_element_by_css_selector('tbody [name="manufacturer_id"]').click()
    select_manufact = driver.find_element_by_css_selector('tbody [name="manufacturer_id"] option:last-child').click()
    text_fields = driver.find_element_by_css_selector('tbody [name="keywords"]').send_keys("SuperDuck, female" + Keys.TAB + "groovy female super duck" + Keys.TAB + "New female SuperDuck inspired by comicbook super heros. A must-have for Wonder Woman fans :-)" + Keys.TAB + "SuperDuck - super hero help" + Keys.TAB + "SuperDuck - super fun")

# Prices tab
    info_tab = driver.find_element_by_css_selector('form [href="#tab-prices"]').click()
    purchase_price = driver.find_element_by_css_selector('#tab-prices [name=purchase_price]').send_keys(Keys.DELETE + "25")
    currency_click = driver.find_element_by_css_selector('tbody [name="purchase_price_currency_code"]').click()
    currency = driver.find_element_by_css_selector('tbody [name="purchase_price_currency_code"] option:last-child').click()
    gross_usd = driver.find_element_by_css_selector('#tab-prices [name="gross_prices[USD]"]').send_keys(Keys.DELETE + "30")
    gross_eur = driver.find_element_by_css_selector('#tab-prices [name="gross_prices[EUR]"]').send_keys(Keys.DELETE + "25")
    #time.sleep(2)
# Save product
    save = driver.find_element_by_css_selector('.button-set [name=save]').click()
    #time.sleep(3)
# Check if product is added
    assert driver.find_element_by_css_selector(".notice.success")
    #time.sleep(3)