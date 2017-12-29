from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@given(u"I am on '{url}' page")
def start_page(context, url):
    context.driver.get(url)
    wait = WebDriverWait(context.driver, 10)



@when(u"I type '{text}' in '{input}' input field")
def login(context, input, text):
    context.wait = WebDriverWait(context.driver, 10)
    login = context.driver.find_element_by_name(input)
    login.send_keys(text)

@when(u"I click '{id_button}' button")
def step_impl(context, id_button):
    context.driver.find_element_by_css_selector(id_button).click()

@then(u"I am on new page with title '{text}'")
def step_impl(context, text):

    assert context.wait.until(EC.title_is(text))

@when(u"I am browsing menu")
def step_impl(context):
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


@when(u"I click on '{id_element}' element")
def step_impl(context, id_element):
    context.driver.find_element_by_css_selector(id_element).click()


@when(u"I check status '{status_radio_button}' of radio button '{element_radio_button}'")
def step_impl(context, status_radio_button, element_radio_button):
    enable_check = context.driver.find_element_by_xpath(element_radio_button).get_attribute(status_radio_button)
    if enable_check in (None, False):
        enable = context.driver.find_element_by_xpath(element_radio_button).click()

@when (u"I fill '{text}' and '{text}' in '{input_field}' input field")
def step_impl(context, input_field, text):
    name = context.driver.find_element_by_css_selector(input_field).send_keys(text + Keys.TAB + text)

@when (u"I click on xpath '{element}' element")
def step_impl(context, element):   
    prod_group = context.driver.find_element_by_xpath(element).click()

@when (u"I fill '{text}' in '{input_field}' input field")
def step_impl(context, input_field, text):
    quantity = context.driver.find_element_by_css_selector(input_field).send_keys(text)


    #date_from = context.driver.find_element_by_css_selector("tbody [name=date_valid_from]").send_keys("11/17/2017" + Keys.TAB + "12/31/2017")

# Information tab

    #info_tab = context.driver.find_element_by_css_selector('form [href="#tab-information"]').click()
    #manufacturer = context.driver.find_element_by_css_selector('tbody [name="manufacturer_id"]').click()
    #select_manufact = context.driver.find_element_by_css_selector('tbody [name="manufacturer_id"] option:last-child').click()
 @When (u"I fill '{text} and '{text}' and '{text}' and '{text}' and '{text}' in '{input_field}' input field") 
 def step_ impl(context, text, input_field): 
    text_fields = context.driver.find_element_by_css_selector(input_field).send_keys(text + Keys.TAB + text + Keys.TAB + text + Keys.TAB + text + Keys.TAB + text)

# Prices tab

    #info_tab = context.driver.find_element_by_css_selector('form [href="#tab-prices"]').click()
@When(u"I delete existing element and add new '{text}' in '{input_field}' input field")
def step_impl(context, text, input_field):
    purchase_price = context.driver.find_element_by_css_selector(input_field).send_keys(Keys.DELETE + text)
    
    #currency_click = context.driver.find_element_by_css_selector('tbody [name="purchase_price_currency_code"]').click()
    #currency = context.driver.find_element_by_css_selector('tbody [name="purchase_price_currency_code"] option:last-child').click()
    #gross_usd = context.driver.find_element_by_css_selector('#tab-prices [name="gross_prices[USD]"]').send_keys(Keys.DELETE + "30")
    #gross_eur = context.driver.find_element_by_css_selector('#tab-prices [name="gross_prices[EUR]"]').send_keys(Keys.DELETE + "25")
    #time.sleep(2)
# Save product
    #save = context.driver.find_element_by_css_selector('.button-set [name=save]').click()
    #time.sleep(3)
# Check if product is added
@Then(u"I can see '{id_element}' element on page")
def step_impl(context, id_element)
    assert context.driver.find_element_by_css_selector(id_element)
    #time.sleep(3)tab-prices [name="gross_prices[EUR]"]