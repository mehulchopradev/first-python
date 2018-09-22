class InsufficientFundsError(Exception):

    def __init__(self, message):
        super().__init__(message)

class Account:

    count = 0 # class property
    # shared by all the objects of that class

    def __init__(self, name, acctype, balance):
        # object properties
        self.name = name
        self.acctype = acctype
        self.balance = balance

        Account.count += 1

    def deposit(self, amt):
        self.balance += amt
        return self.balance

    def withdraw(self, amt):
        print('Transaction starts...')
        # try-except
        # try-finally
        # try-except-else
        # try-except-except
        # try-except-finally
        try:
            if amt <= 0:
                raise ValueError('Amt passed to be non zero positive value')
            if self.balance - amt < 500:
                # exceptional condition that has occured in ur withdraw function
                # raise an exception(error) to the caller of this function!!!
                raise InsufficientFundsError("Balance of {0} is insufficient for this trans".format(self.balance))

            # this code
            self.balance -= amt
            return self.balance
        finally:
            print('Transaction ends')

    def getdetails(self):
        return "Name: {0}\nAcc Type: {1}\nBalance: {2}".format(self.name, self.acctype, self.balance)
