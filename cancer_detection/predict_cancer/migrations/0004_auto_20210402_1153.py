# Generated by Django 3.1.7 on 2021-04-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict_cancer', '0003_auto_20210402_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predresults',
            name='classification',
            field=models.CharField(max_length=30),
        ),
    ]
