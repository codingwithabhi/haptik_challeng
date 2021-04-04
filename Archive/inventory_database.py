class Product(models.Model):
    name = models.CharField()
    price = models.CharField() # We can use some money field library
    description = models.CharField()

class Stock(models.Model):
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    min_alert_quantity = models.IntegerField()


class Order(models.Model):
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()


# Note we can create a trigger in our database to alert database when a product quantity goes below the a specific thresholds.