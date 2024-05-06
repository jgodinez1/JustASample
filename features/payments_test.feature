Feature: Verify the payment page and navigation

  # Can make balance, type of card, number of statements into variables
Background:
 Given I have a customer
 And I create an account with 2000 balance
 And I create a physical card
 And I make payments for the card

Scenario: View most recent payment
  Given I am on the account summary page
  When I go to the "payments" page
  And I see a list of my recent payments
  And I can select the first payment in the list
  Then I see the details of the first payment

Scenario: Make a payment
  Given I am on the account summary page
  And I go to the "payments" page
  Then I can make a payment for my card