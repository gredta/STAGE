# Generated by Django 4.0.3 on 2022-03-27 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Favorites',
            new_name='Favorite',
        ),
        migrations.RenameModel(
            old_name='FavoritesItem',
            new_name='FavoriteItem',
        ),
        migrations.AlterField(
            model_name='historyitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.history'),
        ),
        migrations.AlterField(
            model_name='historyitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product'),
        ),
    ]
