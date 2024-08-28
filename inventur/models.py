from django.db import models


class Boxitem(models.Model):
    def __str__(self):
        return self.item_name
    
    item_name = models.CharField(max_length=50)
    item_amount = models.IntegerField()
    
class Boxtyp(models.Model):
    def __str__(self):
        return self.typ_name
    
    typ_name = models.CharField(max_length=50)
    typ_description = models.CharField(max_length=200)
    boxitems = models.ManyToManyField(
        Boxitem, related_name='boxtyp_item', blank=True)
    
class Location(models.Model):
    def __str__(self):
        return self.loc_name
    
    boxtyp = models.ForeignKey(Boxtyp, on_delete=models.CASCADE)
    loc_name = models.CharField(max_length=50)
    loc_description = models.CharField(max_length=200)

class Inventur(models.Model):
    def __str__(self):
        return self.inv_name
    
    inv_name = models.CharField(max_length=50)
    inv_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, default='Sunrise Roboter')
    #items vielleicht direkt hier speichern? Zu erst boxtyp aufrufen schauen was es drin habe muss und es direkt hier speichern?
    

class Inventuritem(models.Model):
    def __str__(self):
        return self.inv_name
    
    inv_id = models.ForeignKey(Inventur, on_delete=models.CASCADE)
    inv_name = models.CharField(max_length=50)
    item_amount_soll = models.IntegerField()
    item_amount_ist = models.IntegerField()
    inv_comment = models.CharField(max_length=50)



    
    


