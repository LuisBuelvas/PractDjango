# Generated by Django 3.0.1 on 2019-12-30 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0003_subcategoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('descripcion', models.CharField(help_text='Descripción del producto', max_length=100, unique=True)),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.SubCategoria')),
            ],
            options={
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
