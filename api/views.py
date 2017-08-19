from rest_framework import status, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from blood_alert.models import Alert
from .models import Centres, Articles, Statistique, Demande, Planifier
from people.models import User
from api.serializers import AlertSerializer, CentresSerializer, ArticlesSerializer, StatistiqueSerializer, UserSerializer, DemandeSerializer, PlanifierSerializer
# Create your views here.


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


@api_view(['GET', 'POST'])
def alert_list(request, format=None):
    "List all alerts, or create a new one"
    if request.method == 'GET':
        alerts = Alert.objects.all()
        serializer = AlertSerializer(alerts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AlertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def centre_list(request, format=None):
    "List all centers, or create a new one"
    if request.method == 'GET':
        centres = Centres.objects.all()
        serializer = CentresSerializer(centres, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CentresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def article_list(request, format=None):
    "List all articles, or create a new one"
    if request.method == 'GET':
        articles = Articles.objects.all()
        serializer = ArticlesSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticlesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def demande_list(request, format=None):
    "List all alerts, or create a new one"
    if request.method == 'GET':
        demandes = Demande.objects.all()
        serializer = DemandeSerializer(demandes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DemandeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def planifier_list(request, format=None):
    "List all alerts, or create a new one"
    if request.method == 'GET':
        planifiers = Planifier.objects.all()
        serializer = PlanifierSerializer(planifiers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PlanifierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def statistique_list(request, format=None):
    "List all statistiques, or create a new one"
    if request.method == 'GET':
        statistiques = Statistique.objects.all()
        serializer = StatistiqueSerializer(statistiques, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StatistiqueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk, format=None):
    "Retrieve, update or delete an alert"
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def alert_detail(request, pk, format=None):
    "Retrieve, update or delete an alert"
    try:
        alert = Alert.objects.get(pk=pk)
    except Alert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AlertSerializer(alert)
        return Response(serializer.data)
    elif request.method == 'GET':
        serializer = AlertSerializer(alert)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AlertSerializer(alert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        alert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def centres_detail(request, pk, format=None):
    "Retrieve, update or delete an alert"
    try:
        centres = Centres.objects.get(pk=pk)
    except Centres.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AlertSerializer(centres)
        return Response(serializer.data)
    elif request.method == 'GET':
        serializer = AlertSerializer(centres)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AlertSerializer(centres, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        centres.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk, format=None):
    "Retrieve, update or delete an alert"
    try:
        article = Articles.objects.get(pk=pk)
    except Articles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AlertSerializer(article)
        return Response(serializer.data)
    elif request.method == 'GET':
        serializer = AlertSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AlertSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def statistique_detail(request, pk, format=None):
    "Retrieve, update or delete an alert"
    try:
        statistique = Statistique.objects.get(pk=pk)
    except Statistique.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AlertSerializer(statistique)
        return Response(serializer.data)
    elif request.method == 'GET':
        serializer = AlertSerializer(statistique)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AlertSerializer(statistique, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        statistique.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def demande_detail(request, pk, format=None):
    "Retrieve, update or delete an alert"
    try:
        demande = Demande.objects.get(pk=pk)
    except Demande.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DemandeSerializer(demande)
        return Response(serializer.data)
    elif request.method == 'GET':
        serializer = DemandeSerializer(demande)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DemandeSerializer(demande, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        demande.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def planifier_detail(request, pk, format=None):
    "Retrieve, update or delete an alert"
    try:
        planifier = Planifier.objects.get(pk=pk)
    except Alert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PlanifierSerializer(planifier)
        return Response(serializer.data)
    elif request.method == 'GET':
        serializer = PlanifierSerializer(planifier)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PlanifierSerializer(planifier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
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


