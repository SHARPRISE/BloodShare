from rest_framework import status, renderers, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from blood_alert.models import Alert
from .models import Centres, Articles, Statistique, Demande, Planifier
from people.models import User
from api.serializers import AlertSerializer, CentresSerializer, ArticlesSerializer, StatistiqueSerializer, UserSerializer, DemandeSerializer, PlanifierSerializer
# Create your views here.

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET', 'POST'])
def user_list(request, format=None):
    "List all alerts, or create a new one"
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlertList(APIView):
    def get(self, request, format=None):
        alerts = Alert.objects.all()
        serializer = AlertSerializer(alerts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CentreList(APIView):
    def get(self, request, format=None):
        centres = Centres.objects.all()
        serializer = CentresSerializer(centres, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CentresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleList(APIView):
    def get(self, request, format=None):
        articles = Articles.objects.all()
        serializer = ArticlesSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticlesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DemandeList(APIView):
    def get(self, request, format=None):
        demandes = Demande.objects.all()
        serializer = DemandeSerializer(demandes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DemandeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PlanifierList(APIView):
    def get(self, request, format=None):
        planifiers = Planifier.objects.all()
        serializer = PlanifierSerializer(planifiers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlanifierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class StatistiqueList(APIView):
    def get(self,request, format=None):
        statistiques = Statistique.objects.all()
        serializer = StatistiqueSerializer(statistiques, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StatistiqueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AlertDetail(APIView):
    def get_object(self, pk):
        try:
            alert = Alert.objects.get(pk=pk)
            return alert
        except Alert.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        alert = self.get_object(pk)
        serializer = AlertSerializer(alert)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        alert = self.get_object(pk)
        serializer = AlertSerializer(alert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        alert = self.get_object(pk)
        alert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CentresDetail(APIView):
    def get_object(self, pk):
        try:
            centres = Centres.objects.get(pk=pk)
            return centres
        except Centres.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        centre = self.get_object(pk)
        serializer = CentresSerializer(centre)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        centre = self.get_object(pk)
        serializer = CentresSerializer(centre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        centre = self.get_object(pk)
        centre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleDetail(APIView):
    def get_object(self, pk):
        try:
            articles = Articles.objects.get(pk=pk)
            return articles
        except Articles.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticlesSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticlesSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StatistiqueDetail(APIView):
    def get_object(self, pk):
        try:
            statistiques = Statistique.objects.get(pk=pk)
            return statistiques
        except Statistique.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        statistique = self.get_object(pk)
        serializer = StatistiqueSerializer(statistique)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        statistique = self.get_object(pk)
        serializer = StatistiqueSerializer(statistique, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        statistique = self.get_object(pk)
        statistique.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DemandeDetail(APIView):
    def get_object(self, pk):
        try:
            demandes = Demande.objects.get(pk=pk)
            return demandes
        except Demande.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        demande = self.get_object(pk)
        serializer = DemandeSerializer(demande)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        demande = self.get_object(pk)
        serializer = DemandeSerializer(demande, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        demande = self.get_object(pk)
        demande.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlanifierDetail(APIView):
    def get_object(self, pk):
        try:
            planifiers = Planifier.objects.get(pk=pk)
            return planifiers
        except Planifier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        planifier = self.get_object(pk)
        serializer = DemandeSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        planifier = self.get_object(pk)
        serializer = Planifier(planifier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        planifier = self.get_object(pk)
        planifier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'alerts': reverse('alert-list', request=request, format=format),
        'centres': reverse('centre-list', request=request, format=format),
        'articles': reverse('article-list', request=request, format=format),
        'statistiques': reverse('statistique-list', request=request, format=format),
        'demandes': reverse('demande-list', request=request, format=format),
        'planifiers': reverse('planifier-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format)
    })
