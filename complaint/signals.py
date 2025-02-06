# complaint/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Complaint


@receiver(post_save, sender=Complaint)
def send_complaint_email(sender, instance, created, **kwargs):
    if created:  # Si la instancia de Complaint es nueva
        subject = 'Nueva queja recibida'

        # Crear el mensaje con todos los datos de la queja
        message = f"""
        Gracias por informarnos de la inquietud, estamos aqui para ayudar.
        En las proximas horas se comunicará un representante por este medio.
        
        Detalle de la información enviada:

        Nombre: {instance.name}
        DNI: {instance.DNI}
        Edad: {instance.age}
        Teléfono: {instance.phone}
        Dirección: {instance.address}
        Correo: {instance.email}
        Padre o Madre: {instance.parents}
        Servicio: {instance.service}
        Descripción: {instance.description}
        Tipo de queja: {instance.complaintType}
        Detalles de la queja: {instance.complaintDetail}
        """

        from_email = 'juliob.jr2024@gmail.com'
        destination_list = [instance.email]

        send_mail(subject, message, from_email, destination_list)
