from rest_framework import permissions
from rest_framework import viewsets

from app.api.models import Application
from app.api.serializers import ApplicationSerializer


class AppViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated,]


class AppDetailView(viewsets.ReadOnlyModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated,]
