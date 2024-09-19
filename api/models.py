from django.db import models

# Branch Model
class Branch(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    branch_code = models.CharField(max_length=100)

    def json_object(self):
        return {
            "name": self.name,
            "address": self.address,
            "branch_code": self.branch_code,
        }

    def __str__(self):
        return self.name


# Bank Model
class Bank(models.Model):
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)  # Added on_delete

    def json_object(self):
        return {
            "name": self.name,
            "branch": self.branch.json_object(),  # Include branch JSON object
        }

    def __str__(self):
        return self.name


# Clint Model
class Clint(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)

    def json_object(self):
        return {
            "name": self.name,
            "address": self.address,
        }

    def __str__(self):
        return self.name


# ClintManager Model
class ClintManager(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)

    def json_object(self):
        return {
            "name": self.name,
            "address": self.address,
        }

    def __str__(self):
        return self.name


# Accounts Model
class Accounts(models.Model):
    clint = models.ForeignKey(Clint,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    open_date = models.CharField(max_length=100)  # Corrected typo from open_dete to open_date
    account_type = models.CharField(max_length=100)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)  # Added on_delete

    def json_object(self):
        return {
            "name": self.name,
            "open_date": self.open_date,
            "account_type": self.account_type,
            "bank": self.bank.json_object(),  # Include bank JSON object
        }

    def __str__(self):
        return self.account_type


# Transfer Model
class Transfer(models.Model):
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)  # Added on_delete
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)  # Added on_delete

    def json_objects(self):
        return {
            "account": self.account.json_object(),
            "branch": self.branch.json_object(),
        }

    def __str__(self) -> str:
        return f"Account transfer to the {self.branch.name} Branch"


# Withdraw Model
class Withdraw(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)  # Added on_delete

    def __str__(self):
        return f"Withdraw {self.amount} from {self.account}"


# Deposit Model
class Deposit(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)  # Added on_delete

    def __str__(self):
        return f"Deposit {self.amount} to {self.account}"
