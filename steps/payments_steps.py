from behave import *
import selenium
from pages.payments_page import PaymentPage


@when('I see a list of my recent payments')
def step_impl(context):
    context.payements_page()  #verify list/table of payments
    context.payments_page.click_transaction()  # should take you to the details


@then('I see the details of the first payment')
def step_impl(context):
    h = get_element(payment_detail_page())  # locators should be defined in payments_page
    # code to verify we see the table/columns and values for a payment detail
