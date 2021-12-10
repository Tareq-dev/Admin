from django.db import models


class QuoteCategory(models.Model):
    title = models.CharField(max_length=50)


#  code e defult vabe name deya thake. ota valovabe dynamicly bujha jawar jnno ei dan dan function use hoy.

    def __str__(self):
        return self.title


class Quote(models.Model):
    quote = models.TextField()

    quote_category = models.ForeignKey(
        'QuoteCategory',
        on_delete=models.CASCADE
    )


#  code e defult vabe name deya thake. ota valovabe dynamicly bujha jawar jnno ei dan dan function use hoy.

    def __str__(self):
        if len(self.quote) > 50:
            return self.quote[:50] + "..."
            return self.quote
