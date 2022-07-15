import uuid
from django.db import models
from django.core.validators import MinLengthValidator,RegexValidator
from django.utils.translation import gettext_lazy as _

class Clients(models.Model):
    id = models.UUIDField(
    primary_key=True,
    unique=True,
    auto_created=True,
    default=uuid.uuid4,
    editable=False,
    null=False,
    blank=False,
    )
    name = models.CharField(max_length=250,blank=False,null=True)
    phoneNumber = models.CharField(
        max_length=11,
        validators=[MinLengthValidator(limit_value=11,message='Phone Number must be 11 number'),RegexValidator(regex=r'01[1,2,5,0]{1}[0-9]{8}',message="must be valid Egyption Number")],
        unique=True,
    error_messages={
            'unique': _("A user with that phone number already exists."),
        },
    blank=False,
    null=False,
    )
    has_whatsapp = models.BooleanField(
        default=False,
        help_text=_('whether the user has whatsapp or not.'),
        blank=False,
        null=False
    )

    def __str__(self) -> str:
        return self.name

class Programs(models.Model):
    id = models.UUIDField(
    primary_key=True,
    unique=True,
    auto_created=True,
    default=uuid.uuid4,
    editable=False,
    null=False,
    blank=False,
    )
    title =  models.CharField(max_length=150,blank=False,null=False,)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title

class License(models.Model):
    id = models.UUIDField(
    primary_key=True,
    unique=True,
    auto_created=True,
    default=uuid.uuid4,
    editable=False,
    null=False,
    blank=False,
    )
    client_mac_id = models.CharField(max_length=150,blank=False,null=False,default="Null")
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    running_time = models.IntegerField(blank=False,null=False,default=0)
    client = models.ForeignKey(Clients,on_delete=models.CASCADE,related_name="licenses",blank=True,null=False)
    program = models.ForeignKey(Programs,on_delete=models.CASCADE,related_name="programs",blank=True,null=False)

    def __str__(self) -> str:
        return str(self.id)

