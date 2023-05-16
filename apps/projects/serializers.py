from rest_framework import serializers

from apps.projects.models import Appeal, Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id',
            'title',
            'description',
            'image',
            'link',
        )


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = (
            'id',
            'name',
            'email',
            'message',
        )
