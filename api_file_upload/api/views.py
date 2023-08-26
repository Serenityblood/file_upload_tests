from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .checker import check_files
from .models import File
from .serializer import FileSerializer


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(new=True, review=None)

    @action(methods=['GET'], detail=False)
    def reviews(self, request):
        response = check_files(File.objects.filter(new=True))
        return Response(FileSerializer(response, many=True).data)
