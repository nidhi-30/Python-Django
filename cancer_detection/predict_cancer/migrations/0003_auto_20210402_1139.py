# Generated by Django 3.1.7 on 2021-04-02 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict_cancer', '0002_auto_20210402_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predresults',
            name='classification',
            field=models.FloatField(),
        ),
    ]