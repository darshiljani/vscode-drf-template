from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="%(class)s_created_by", null=True
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="%(class)s_updated_by", null=True
    )

    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

    @classmethod
    def objects(cls):
        return SoftDeleteQuerySet(cls)


class SoftDeleteQuerySet(models.QuerySet):
    def exclude_soft_deleted(self):
        return self.filter(is_deleted=False)
