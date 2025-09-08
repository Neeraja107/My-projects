from behave import given,when,then
from selenium import webdriver
from features.pages.swaglabs import LoginPage
@given(u'Opening the website')
def step_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()
    context.obj = LoginPage(context.driver)

@when(u'The user enter the username and password')
def step_enter_credentials(context):
    context.obj.login("standard_user", "secret_sauce")

@then(u'The user should login to the website')
def step_verify_login(context):
    assert context.obj.verify_text() == "Swag Labs"

@when(u'The user click on add to cart')
def step_addtocart(context):
   context.obj.add_to_cart()

@then(u'The items should be added into cart')
def step_verify_products(context):
    assert "Sauce Labs Backpack" == context.obj.verify_cart_product1()
    assert "Sauce Labs Bike Light" == context.obj.verify_cart_product2()
    assert "Sauce Labs Bolt T-Shirt" == context.obj.verify_cart_product3()


@when(u'The user enter firstname, lastname, zipcode')
def step_enter_checkout_details(context):
    context.obj.add_checkout_details("Neeraja","Tanuku",534211)

@then(u'The user should checkout and see the text "Checkout: Overview"')
def step_verify_checkout(context):
    assert "Checkout: Overview" == context.obj.verify_checkout()


@when(u'The user finishes checkout')
def step_finish(context):
   context.obj.finish()

@then(u'The user should see the success message')
def step_verify_thanks(context):
    assert "Thank you for your order!" == context.obj.verify_finish()

@when(u'The user click logout button')
def step_logout(context):
    context.obj.logout_button()

@then(u'The user should logout')
def step_verify_logout(context):
    assert "Swag Labs" == context.obj.verify_logout_text()