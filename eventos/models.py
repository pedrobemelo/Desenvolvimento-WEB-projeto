from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class Evento(models.Model):
    class Status(models.TextChoices):
        PLANEJADO = "PLANEJADO", "Planejado"
        CONFIRMADO = "CONFIRMADO", "Confirmado"
        CANCELADO = "CANCELADO", "Cancelado"
        FINALIZADO = "FINALIZADO", "Finalizado"

    organizador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="eventos",
    )
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField(null=True, blank=True)

    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=200, blank=True)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    uf = models.CharField(max_length=2, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PLANEJADO,
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["data_inicio"]
        indexes = [
            models.Index(fields=["data_inicio"]),
            models.Index(fields=["status"]),
            models.Index(fields=["cidade"]),
        ]

    def clean(self):
        super().clean()
        if self.data_fim and self.data_inicio and self.data_fim <= self.data_inicio:
            raise ValidationError({"data_fim": "A data final deve ser posterior à data inicial."})

    @property
    def endereco_completo(self):
        partes = [
            self.logradouro,
            self.numero,
            self.complemento,
            self.bairro,
            self.cidade,
            self.uf,
        ]
        return ", ".join(str(parte).strip() for parte in partes if parte and str(parte).strip())

    def __str__(self):
        return self.titulo
