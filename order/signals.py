from django.db.models.signals import pre_save
from django.dispatch import receiver
from order.utils import generate_tracking_code
from order.models import Declaration


@receiver(pre_save, sender=Declaration)
def declaration_tracking_pre_save(sender, instance, **kwargs):
    if not instance.tracking_code:
            while True:
                code = generate_tracking_code()
                if not Declaration.objects.filter(tracking_code=code).exists():
                    instance.tracking_code = code
                    break
        
