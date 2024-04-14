from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    tg_id = models.BigIntegerField(unique=True)

    subscription = models.BooleanField(default=False)

    discount = models.IntegerField(default=0)
    subscribe_date = models.CharField(max_length=15, blank=True)
    expiration_date = models.CharField(max_length=15, blank=True)

    referrals = ""

    key = ""

    payments = ""

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return f"User(id={self.id!r}, username={self.username!r})"

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
