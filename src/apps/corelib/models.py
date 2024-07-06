import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UUIDModel(models.Model):
    """
    Abstract base model that includes a UUID field for unique identification.

    Fields:
        uuid (UUIDField): A unique identifier for each instance, generated automatically upon creation.

    Meta:
        abstract (bool): This model is intended to be an abstract base class and should not be instantiated directly.

    Example:
        class MyModel(UUIDModel):
            name = models.CharField(max_length=255)
    """

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True,
        auto_created=True,
    )

    class Meta:
        abstract = True


class UUIDPrimaryKeyModel(models.Model):
    """
    Abstract base model that uses a UUID as the primary key.

    Fields:
        id (AutoField): An automatically-incremented primary key field.
        uuid (UUIDField): A unique identifier for each instance, generated automatically upon creation and set as the primary key.

    Meta:
        abstract (bool): This model is intended to be an abstract base class and should not be instantiated directly.

    Example:
        class MyModel(UUIDPrimaryKeyModel):
            name = models.CharField(max_length=255)
    """

    id = models.AutoField()
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True,
        auto_created=True,
        primary_key=True,
    )

    class Meta:
        abstract = True


class TimestampedModel(models.Model):
    """
    Abstract base model that includes timestamp fields for tracking the creation and modification times.

    Fields:
        created_at (DateTimeField): The date and time when the instance was created. Automatically set on instance creation.
        updated_at (DateTimeField): The date and time when the instance was last updated. Automatically set on instance update.

    Meta:
        abstract (bool): This model is intended to be an abstract base class and should not be instantiated directly.

    Example:
        class MyModel(TimestampedModel):
            name = models.CharField(max_length=255)
    """

    created_at = models.DateTimeField(
        _("created at"), default=timezone.now, editable=False
    )
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        abstract = True


class AbstractBaseModel(UUIDModel, TimestampedModel):
    """
    Abstract base model that includes UUID and timestamp fields.

    Inherits from:
        UUIDModel: Adds a UUID field for unique identification.
        TimestampedModel: Adds fields for tracking creation and modification times.

    Meta:
        abstract (bool): This model is intended to be an abstract base class and should not be instantiated directly.

    Example:
        class MyModel(AbstractBaseModel):
            name = models.CharField(max_length=255)
    """

    class Meta:
        abstract = True


class AbstractBaseUUIDModel(UUIDPrimaryKeyModel, TimestampedModel):
    """
    Abstract base model that uses a UUID as the primary key and includes timestamp fields.

    Inherits from:
        UUIDPrimaryKeyModel: Uses a UUID as the primary key.
        TimestampedModel: Adds fields for tracking creation and modification times.

    Meta:
        abstract (bool): This model is intended to be an abstract base class and should not be instantiated directly.

    Example:
        class MyModel(AbstractBaseUUIDModel):
            name = models.CharField(max_length=255)
    """

    class Meta:
        abstract = True
