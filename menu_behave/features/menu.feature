Feature: menu

  Background: login
    Given I am on 'http://localhost/litecart/admin' page
    When I type 'admin' in 'username' input field
    When I type 'admin' in 'password' input field
    When I click '.footer [type="submit"]' button
    Then I am on new page with title 'My Store'

 Scenario: browsing menu
    When I am browsing menu
    Then I get header of subpage

  Scenario: add new duck
  	When I click on 'ul#box-apps-menu li:nth-child(2)' element
  	When I click on '#content .button:nth-child(2)' element
  	When I check status 'checked' of radio button './/*[@id='tab-general']/table/tbody/tr[1]/td/label[1]/input'
  	When I fill 'SuperDuck' and 'SD' in 'tbody [name="name[en]"]' input field
  	When I click on xpath './/*[@id='tab-general']/table/tbody/tr[7]/td/div/table/tbody/tr[2]/td[1]/inp' element
  	When I fill '100' in 'tbody [name=quantity' input field
  	When I fill '11/17/2017' and '12/31/2017' in 'tbody [name=date_valid_from]' input field
  	When I click on 'form [href="#tab-information"]' element
  	When I click on 'tbody [name="manufacturer_id"]' element
  	When I click on 'tbody [name="manufacturer_id"] option:last-child' element
  	When I fill 'SuperDuck, female' and 'groovy female super duck' and 'New female SuperDuck inspired by comicbook super heros. A must-have for Wonder Woman fans :-)' and 'SuperDuck - super hero help' and 'SuperDuck - super fun' in 'tbody [name="keywords"]' input field
  	When I click on 'form [href="#tab-prices"]' element 
  	When I delete existing element and add new '25' in '#tab-prices [name=purchase_price]' input field
  	When I click on 'tbody [name="purchase_price_currency_code"]' element
  	When I click on 'tbody [name="purchase_price_currency_code"] option:last-child' element
  	When I delete existing element add new '#tab-prices [name="gross_prices[USD]' in '30' input field
  	When I delete existing element add new '#tab-prices [name="gross_prices[EUR]"]' in '25' input field
  	When I click '.button-set [name=save]' button
  	Then I can see '.notice.success' element on page