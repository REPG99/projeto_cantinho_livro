from django.db import models

class Livro(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    autor = models.CharField(max_length=200)

    def __str__(self):
        texto_nome = str(self.nome)
        texto_autor = str(self.autor)
        resultado = texto_nome + " - " + texto_autor
        return resultado