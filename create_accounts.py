from account import Account
from account import InsufficientFundsError

print('No of account objects ' + str(Account.count))

a1 = Account(name='mehul chopra', acctype='savings', balance=9000)
# print(a1.deposit(900))
# Account.deposit(a1, 900)

print('No of account objects ' + str(Account.count))

try:
    ub = a1.withdraw(8900)
except InsufficientFundsError as e:
    print(e)
    print('U do not have sufficient funds for this withdrawl to happen')
except ValueError as e:
    # one try can have multiple except blocks
    print(e)

a2 = Account(acctype='current', name='xyz pvt ltd', balance=10000)
print(a2.getdetails())

a3 = Account(name='jane', acctype='savings', balance=3000)

print('No of account objects ' + str(Account.count))
# print('No of account objects ' + str(a3.count)) # class property can be accessed using object references
# of that class. But avoid that
