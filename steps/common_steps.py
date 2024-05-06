from behave import given, when, then
from pages.payments_page import PaymentPage
# import all the pages


@when('I go to the "{page}" page')
def step_impl(context,page):
    context.payments_page = PaymentPage()
    #do verification you are on the right page
