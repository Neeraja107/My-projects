Feature: Login into website and logout

  Scenario: Login and logout
    Given Opening the website
    When The user enter the username and password
    Then The user should login to the website
    When The user click on add to cart
    Then The items should be added into cart
    When The user enter firstname, lastname, zipcode
    Then The user should checkout and see the text "Checkout: Overview"
    When The user finishes checkout
    Then The user should see the success message
    When The user click logout button
    Then The user should logout
