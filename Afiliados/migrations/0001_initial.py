# Generated by Django 3.0.3 on 2020-02-23 23:33

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ubicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Afiliado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizacion_polita', models.CharField(choices=[('N', 'Nacional'), ('R', 'Regional')], max_length=255, verbose_name='Alcance de la Organizacion Politica ')),
                ('organizacion_politica_region', models.CharField(blank=True, choices=[('Amazonas', 'Amazonas'), ('Ancash', 'Ancash'), ('Apurimac', 'Apurimac'), ('Arequipa', 'Arequipa'), ('Ayacucho', 'Ayacucho'), ('Cajamarca', 'Cajamarca'), ('Callao', 'Callao'), ('Cusco', 'Cusco'), ('Huancavelica', 'Huancavelica'), ('Huanuco', 'Huanuco'), ('Ica', 'Ica'), ('Junin', 'Junin'), ('La libertad', 'La libertad'), ('Lambayeque', 'Lambayeque'), ('Lima', 'Lima'), ('Loreto', 'Loreto'), ('Madre de dios', 'Madre de dios'), ('Moquegua', 'Moquegua'), ('Pasco', 'Pasco'), ('Piura', 'Piura'), ('Puno', 'Puno'), ('San martin', 'San martin'), ('Tacna', 'Tacna'), ('Tumbes', 'Tumbes'), ('Ucayali', 'Ucayali')], max_length=255, null=True, verbose_name='Region (opcional)')),
                ('fecha_afiliacion', models.DateField()),
                ('numero_dni', models.CharField(max_length=8, verbose_name='Numero de DNI ')),
                ('nombre_afiliado', models.CharField(max_length=250, verbose_name='Nombres')),
                ('apellido_paterno_afiliado', models.CharField(max_length=250, verbose_name='Apellido Paterno')),
                ('apellido_materno_afiliado', models.CharField(max_length=250, verbose_name='Apellido Materno')),
                ('fecha_nacimiento_afiliado', models.CharField(max_length=255, verbose_name='Fecha Nacimiento')),
                ('estado_civil', models.CharField(choices=[('S', 'Civil'), ('C', 'Casado'), ('V', 'Viudo/a'), ('D', 'Divorciodo/a'), ('Conv', 'Conviviente')], max_length=25, verbose_name='Estado Civil ')),
                ('sexo', models.CharField(max_length=20)),
                ('lugar_nacimiento', models.CharField(max_length=255, verbose_name='Lugar de Nacimiento ')),
                ('avenida_afiliado', models.CharField(max_length=255, verbose_name='Avenida/Calle/Jirón')),
                ('avenida_numero_afiliado', models.CharField(max_length=25, verbose_name='Numero')),
                ('urbanizacion_afiliado', models.CharField(max_length=255, verbose_name='Urbanizacion/Sector/Caserío')),
                ('urbanizacion_numero_afiliado', models.CharField(max_length=25, verbose_name='Telefono')),
                ('correo', models.EmailField(max_length=255)),
                ('region_afiliado_guardado', models.CharField(blank=True, max_length=255, null=True)),
                ('provincia_afiliado_guardado', models.CharField(blank=True, max_length=255, null=True)),
                ('distrito_afiliado_guardado', models.CharField(blank=True, max_length=255, null=True)),
                ('distrito_afiliado', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='provincia_afiliado', chained_model_field='provincia_distrito', on_delete=django.db.models.deletion.CASCADE, to='ubicacion.Distrito')),
                ('provincia_afiliado', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='region_afiliado', chained_model_field='region_provincia', on_delete=django.db.models.deletion.CASCADE, to='ubicacion.Provincia')),
                ('region_afiliado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ubicacion.Region')),
            ],
            options={
                'verbose_name': 'Afiliado',
                'verbose_name_plural': 'Afiliados',
            },
        ),
    ]
