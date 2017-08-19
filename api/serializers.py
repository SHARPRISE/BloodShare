from rest_framework import serializers

from blood_alert.models import Alert
from people.models import User
from .models import Centres, Articles, Statistique, Demande, Planifier


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'blood_type', 'phone', 'adresse', 'qteSang', 'photo_url')


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ('id', 'name', 'blood_type', 'phone', 'location', 'date_time_posted','message','resolved')


class CentresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Centres
        fields = ('id', 'lieu', 'telephone', 'type', 'lat', 'long', 'qteDisponible')


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('id', 'title', 'contenu', 'date', 'photo')


class StatistiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistique
        fields = ('id', 'critere', 'date', 'pourcentage')


class DemandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demande
        fields = ('id', 'text', 'qte', 'date', 'etat', 'user')


class PlanifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planifier
        fields = ('id', 'qtePrevue', 'date', 'etat', 'user')