from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Comment
from .serializers import CommentSerializer

# Create your views here.

class CommentView(APIView):

    def post(self, request):
        serializer = CommentSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)


class CommentSingleView(APIView):

    def patch(self, request, id):  #pk
        comment = Comment.objects.filter(id = id).first()   #pk = pk

        if comment is None:
            return Response({'error': 'Bad Request'}, status = status.HTTP_400_BAD_REQUEST)
        serializer = CommentSerializer(comment, data = request.data, partial = True)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data, status = status.HTTP_200_OK)

    def delete(self, request, id):  #pk
        place = get_object_or_404(Comment, id = id)  #pk = pk
        place.delete()
        return Response('Comentario eliminado', status = status.HTTP_204_NO_CONTENT)
