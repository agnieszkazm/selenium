Feature: menu

  Background: login
    Given I am on 'http://localhost/litecart/admin' page
    When I type 'admin' in 'username' input field
    When I type 'admin' in 'password' input field
    When I click '.footer [type="submit"]' button
    Then I am on new page with title 'My Store'

 Scenario: browsing menu
    And I am browsing menu
    Then I get header of subpage

  Scenario: add new duck
  	When I click on 'ul#box-apps-menu li:nth-child(2)' menu element
  	When I click on '#content .button:nth-child(2)' menu element
  	When I check status 'checked' of radio button './/*[@id='tab-general']/table/tbody/tr[1]/td/label[1]/input'