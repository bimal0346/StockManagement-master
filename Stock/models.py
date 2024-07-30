from django.db import models

# Create your models here.
class All_Stock(models.Model):
    status_choice = (
    ('BUY', 'BUY'),
    ('SELL', 'SELL'),
    )
    Stock_name = models.CharField(max_length=150)
    status = models.CharField(max_length=100,choices=status_choice)
    quantity = models.IntegerField(default='1')
    amount  = models.DecimalField(max_digits=8, decimal_places=2)
    transaction_date = models.DateTimeField( auto_now_add=True)

class User_stock(models.Model):
    choose_stock = models.ForeignKey(All_Stock,on_delete=models.CASCADE)
    status_choice = (
    ('BUY', 'BUY'),
    ('SELL', 'SELL'),
    )
    transaction_type =  models.CharField(max_length=100,choices=status_choice)
    quantity = models.IntegerField(default='1')
    transaction_price = models.DecimalField(max_digits=8, decimal_places=2)
    transaction_date =  models.DateTimeField( auto_now=False, auto_now_add=False)

    def total_transaction_price(self):
        return (self.All_Stock.amount * self.quantity)

class Individual_Stock(models.Model):
    stock_name = models.ForeignKey(All_Stock,on_delete=models.CASCADE) 

    def __str__(self):
        return self.All_Stock.Stock_name
    def total_unit(self):
        return self.All_Stock.quantity
    
    def total_amount(self):
        return (self.All_Stock.quantity * self.All_Stock.amount )

    def total_amount_sold(self):
        return (self.User_stock.quantity * self.User_stock.transaction_price)

    


class Inventory(models.Model):
    total_unit = models.IntegerField()
    
    total_investment = models.DecimalField(max_digits=8, decimal_places=2)
    Sold_amount = models.DecimalField(max_digits=8, decimal_places=2)
    Current_amount = models.DecimalField(max_digits=8, decimal_places=2)
    Over_all_profit = models.DecimalField(max_digits=8, decimal_places=2)

    

    