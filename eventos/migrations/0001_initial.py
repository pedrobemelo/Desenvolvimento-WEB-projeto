# Generated for the project baseline.
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Evento",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=150)),
                ("descricao", models.TextField(blank=True)),
                ("data_inicio", models.DateTimeField()),
                ("data_fim", models.DateTimeField(blank=True, null=True)),
                ("cep", models.CharField(max_length=9)),
                ("logradouro", models.CharField(blank=True, max_length=200)),
                ("numero", models.CharField(max_length=20)),
                ("complemento", models.CharField(blank=True, max_length=100)),
                ("bairro", models.CharField(blank=True, max_length=100)),
                ("cidade", models.CharField(blank=True, max_length=100)),
                ("uf", models.CharField(blank=True, max_length=2)),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("longitude", models.FloatField(blank=True, null=True)),
                ("status", models.CharField(choices=[("PLANEJADO", "Planejado"), ("CONFIRMADO", "Confirmado"), ("CANCELADO", "Cancelado"), ("FINALIZADO", "Finalizado")], default="PLANEJADO", max_length=20)),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
                ("atualizado_em", models.DateTimeField(auto_now=True)),
                ("organizador", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="eventos", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["data_inicio"]},
        ),
        migrations.AddIndex(
            model_name="evento",
            index=models.Index(fields=["data_inicio"], name="eventos_eve_data_in_9c74b9_idx"),
        ),
        migrations.AddIndex(
            model_name="evento",
            index=models.Index(fields=["status"], name="eventos_eve_status_2f2165_idx"),
        ),
        migrations.AddIndex(
            model_name="evento",
            index=models.Index(fields=["cidade"], name="eventos_eve_cidade_7fc251_idx"),
        ),
    ]
