

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_comment_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_count',
        ),
    ]
