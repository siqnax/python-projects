import time                         # To create a time counter to mimic transaction loading

# Customer registered details
saved_password = 1234
saved_balance = 9081726354
customer_phone = '08091234567'

# Global variables
list_of_banks = ['Gtbank', 'UBA', 'First Bank', 'Wema Bank', 'Heritage', 'Ecobank', 'Zenith Bank']
ussd_service = False
ussd = ''
bar = 5            # Number of times customer is allowed to type a wrong password

print(' Favour Bank '.center(30, '*'))

# Check for wrong USSD code and ValueError
try:
    ussd = int(input('Enter 101 to access Favour Bank USSD Service: '))
    if ussd == 101:
        ussd_service = True
    else:
        print('Invalid Request')

except ValueError:
    print('Invalid Request')

# Main Program Loop
while ussd_service is True:
    try:
        print('Choose a transaction\n'
              '1. Check Balance\n'
              '2. Send Money\n'
              '3. Purchase airtime\n'
              '4. Cancel')

        customer_choice = int(input('Enter: '))

        # CHECK BALANCE
        if customer_choice == 1:

            customer_password = int(input('Enter password: '))

            # Check for correct password
            if customer_password == saved_password:
                print('Balance:', saved_balance)

            else:
                bar = bar - 1
                print('Wrong paasword!\nYou would be barred after ' + str(bar) + ' wrong tries\n')

                if bar > 0:
                    continue
                else:
                    print('You have been barred. Visit our nearest branch to unblock your account.')
                    break

        # MONEY TRANSFER
        elif customer_choice == 2:
            bank_choice = int(input('1. Favour Bank\n'
                                    '2. Other Banks\n'
                                    'Enter: '))

            if bank_choice == 1:
                print('Favour Bank')

            if bank_choice == 2:
                print('Select bank')

                # List out all other banks from bank list
                count = 1
                for bank in list_of_banks:
                    print(str(count) + '. ' + bank)
                    count = count + 1

                bank_name = int(input('Enter: '))

                print(list_of_banks[bank_name - 1])

            print('Balance:', saved_balance)

            # Input amount to send and details of recipient
            amount_to_transfer = int(input('Enter amount: '))
            account_number = int(input('Enter account number: '))

            password_check = int(input('Enter your password: '))

            # Password check
            if password_check == saved_password:

                # Loading timer
                for i in range(5):
                    print('.', end='')
                    time.sleep(0.25)

                saved_balance = saved_balance - amount_to_transfer
                print('\n' + str(amount_to_transfer) + ' sent to ' + str(account_number))
                print('Balance:', saved_balance)

            else:
                bar = bar - 1
                print('Wrong password!\nYou would be barred after ' + str(bar) + ' wrong tries\n')

                if bar > 0:
                    continue

                else:
                    print('You have been barred. Visit the nearest branch to unblock your account.')
                    break

        # BUY AIRTIME
        elif customer_choice == 3:
            card_purchase = int(input('1. Buy card for yourself\n'
                                      '2. Buy for others\n'
                                      'Enter: '))

            phone_number = ''

            if card_purchase == 1:
                phone_number = customer_phone

            elif card_purchase == 2:
                phone_number = input('Enter phone number: ')

            else:
                print('Invalid entry!')
                continue

            card_amount = int(input('Enter amount: '))

            password_check = int(input('Enter your password: '))

            if password_check == saved_password:

                # Loading timer
                for i in range(5):
                    print('.', end='')
                    time.sleep(0.25)

                saved_balance = saved_balance - card_amount
                print('\n' + phone_number + ' has been credited with ' + str(card_amount))
                print('Balance:', saved_balance)

            else:
                bar = bar - 1
                print('Wrong password!\nYou would be barred after ' + str(bar) + ' wrong tries\n')

                if bar > 0:
                    continue

                else:
                    print('You have been barred. Visit the nearest branch to unblock your account.')
                    break

        # CANCEL USSD SERVICE
        elif customer_choice == 4:
            break

        # WRONG CHOICE INPUT
        else:
            print('Wrong input!\n')
            continue

        # PERFORM ANOTHER TRANSACTION
        # Ask if another transaction is to be carried out
        print('\nDo you want to carry out another transaction?\n'
              '1. Yes\n'
              '2. No')

        another_transaction = int(input('Enter: '))

        if another_transaction == 1:
            ussd_service = True
        else:
            print('Goodbye')
            ussd_service = False

    except ValueError:
        print('Invalid entry\n')

# TODO: Possible additions: a dictionary for each bank containing dummy account details can be created.
# When the customer types the account detail, the name on the account gets displayed.
