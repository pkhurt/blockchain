from django.db import models
from django.utils import timezone

class Blockchain(models.Model):
    previous_hash = models.CharField(max_length=255)
    hash = models.CharField(max_length=255)
    proof = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Block({self.hash}) generated on {self.timestamp}."
    
    def was_forged_recently(self):
        return self.timestamp >= timezone.now() - datetime.timedelta(days=1)
    
class Transaction(models.Model):
    sender = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    amount = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Transaction from {self.sender} to {self.recipient} for {self.amount} coins."
    
class ConfirmedTransactions(models.Model):
    block = models.ForeignKey(Blockchain, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return f"Block {self.block} contains transaction {self.transaction}."
