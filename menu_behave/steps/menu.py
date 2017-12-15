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

@when(u'I am browsing menu')
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

@then(u'I get header of subpage')
def step_impl(context):
    print(context.submenuheaderList, context.menuheaderList)