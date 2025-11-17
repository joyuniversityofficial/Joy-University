# Generated manually for adding password field

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='password',
            field=models.CharField(max_length=128, default=''),
        ),
    ]
