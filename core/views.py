from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer


# Create your views here.

class API(APIView):

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors)
        

class APIDetails(APIView):

    def get_person(self, id):
        try:
            id = int(id)
            try:
                person = Person.objects.get(id=id)
            except Person.DoesNotExist:
                return None
        except (ValueError, TypeError):
            try:
                person = Person.objects.get(name=id)
            except Person.DoesNotExist:
                return None
        return person

    def get(self, request, id):
        try:
            person = self.get_person(id)
            if person is None:
                return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
            serializer = PersonSerializer(person)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as err:
            return Response({"error": "An error occurred"}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id):
        person = self.get_person(id)
        if person is None:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "An error occurred"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        person = self.get_person(id)
        if person is None:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
