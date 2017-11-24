from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'I am on store page')
def start_page(context):
    context.driver.get("http://localhost/litecart/admin")


@when(u'I am logged in as admin')
def loggin(context):
    wait = WebDriverWait(context.driver, 10)
    login = context.driver.find_element_by_name("username").send_keys("admin")
    passwort = context.driver.find_element_by_name("password").send_keys("admin")
    submit_button = context.driver.find_element_by_css_selector(".footer [type='submit']").click()
    #assert "My Store" in driver.title
    assert wait.until(EC.title_is("My Store"))

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
    #submenuheaderList,menuheaderList = browsing()
    print(context.submenuheaderList, context.menuheaderList)