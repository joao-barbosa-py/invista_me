from django.db import models
from datetime import datetime
# Create your models here.
class Investimento(models.Model):
    investimento = models.TextField(max_length=200)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    # Pegar o horario atual que o usuário foi cadastrado
    data = models.DateField(default=datetime.now)