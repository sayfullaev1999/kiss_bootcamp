from rest_framework import serializers

from course.models import Course


class CourseListSerializer(serializers.ModelSerializer):
    """List of Course"""
    # mentor = serializers.SlugRelatedField(
    #     slug_field='name',
    #     read_only=True,
    #     many=True
    # )

    class Meta:
        model = Course
        exclude = ('slug',)


class CourseDetailSerializer(serializers.ModelSerializer):
    """Detail of Course"""
    # mentor = serializers.SlugRelatedField(
    #     slug_field='user.get_username()',
    #     read_only=True,
    #     many=True
    # )

    class Meta:
        model = Course
        exclude = ('slug',)
