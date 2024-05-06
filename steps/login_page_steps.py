from behave import given, when, then
from pages.login_page import LoginPage

@given('I am on the login page')
def step_impl(context):
    context.driver.get('https://example.com/login')
    context.login_page = LoginPage(context.driver)

@when('I enter valid credentials')
def step_impl(context):
    context.login_page.enter_credentials('username', 'password')
    context.login_page.click_login()

@then('I should be logged in successfully')
def step_impl(context):
    assert 'Welcome' in context.driver.title