# views.py
from rest_framework import viewsets
from django.http import HttpResponse
from django.core.mail import send_mail
from complaint.models import Complaint
from complaint.serializer import ComplaintSerializer


class ComplaintView(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Enviar el correo manualmente sin necesidad de 'instance' y 'created'
            data = serializer.validated_data
            subject = f'Nueva Queja de {data["name"]}'
            message = f'''
            Nombre: {data["name"]}
            DNI: {data["DNI"]}
            Edad: {data["age"]}
            Teléfono: {data["phone"]}
            Dirección: {data["address"]}
            Correo: {data["email"]}
            Padres: {data["parents"]}
            Servicio: {data["service"]}
            Descripción: {data["description"]}
            Tipo de Queja: {data["complaintType"]}
            Detalles de la Queja: {data["complaintDetail"]}
            '''
            from_email = 'juliob.jr2024@gmail.com'
            destination_list = ['juliob.jr2024@gmail.com']
            send_mail(subject, message, from_email, destination_list)

            # No guardamos en la base de datos
            return HttpResponse("Queja recibida, correo enviado.")
        else:
            return HttpResponse("Datos incorrectos.", status=400)
