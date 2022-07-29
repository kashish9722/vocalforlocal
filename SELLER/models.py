from django.db import models
class  product (models.Model):
    pid = models.AutoField(primary_key=True) 
    pname = models.CharField(max_length=30) 
    username = models.CharField(max_length=100) 
    category= models.CharField(max_length=10)
   
    img = models.ImageField(upload_to='Profile/%Y/%m/%d/images') 
    
    iurl = models.URLField(max_length=32)
    desc=models.CharField( max_length=300)
    #seller = models.ForeignKey("login.pSELLER",  on_delete=models.CASCADE)
    def __str__(self):
        return self.pname
    def get_products_by_id(ids):
            return product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return product.objects.filter(category = category_id)
        else:
            return product.get_all_products();

