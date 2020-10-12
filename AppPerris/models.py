from django.db import models

# 
# FORMULARIO INGRESO DE MASCOTA
ESTADO_ANIMALES=(('rescatado','Rescatado'),('disponible','Disponible'),('adoptado','Adoptado'))
class Rescatado(models.Model):
 foto= models.CharField(max_length=200 , blank=False , null=False)
 nombre= models.CharField(max_length=200 , blank=False , null=False)
 raza= models.CharField(max_length=80 , blank=False , null=False)
 descripcion= models.TextField(blank=False, null=False)
 estado= models.CharField(max_length=70 , choices=ESTADO_ANIMALES)





def __str__(self):
        return self.nombre




