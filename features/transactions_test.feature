Feature: View different transaction types

  # Can make balance, type of card, number of statements into variables
Background:
 Given I have a customer
 And I create an account with 2000 balance
 And I create a physical card
 And I use my card

Scenario: View the transaction details
  Given I am on the account summary page
  When I go to the "transactions" page
  And I see a list of my recent transactions
  And I can select the first transaction in the list
  Then I see the details of the transaction

Scenario: Filter the transactions
  Given I am on the account summary page
  When I go to the "transactions" page
  And I filter the list by Transaction Type
  Then I see the expected transactions