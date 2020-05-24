from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Customer')

    def __str__(self):
        return self.name


class ProjectName(models.Model):
    name = models.CharField(max_length=100, verbose_name='Project name')
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FinalProductNumber(models.Model):
    name = models.CharField(max_length=100, verbose_name='Assembly number')  # zmien na xxxxx.xx.xxx.xx
    project_name = models.ForeignKey(ProjectName, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SingleProductsNumber(models.Model):
    name = models.CharField(max_length=100, verbose_name='Single product ')
    final_product = models.ForeignKey(FinalProductNumber, on_delete=models.CASCADE)
    tool_maker = models.CharField(max_length=100, verbose_name='Tool maker', null=True)
    stock = models.IntegerField(null=True)
    gs = models.IntegerField(null=True)
    receive_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

