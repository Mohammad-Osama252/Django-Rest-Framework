from rest_framework import serializers
from .models import Student


### using custom serializer ###

# def city_kar(value):
#     if value[0] != 'K':
#         raise serializers.ValidationError('City Starts With K')
#     return value
#
#
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100, validators=[city_kar])
#
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance
#
#     ###
#     def validate_roll(self, value):
#         if value >= 200:
#             raise serializers.ValidationError('Seat Full')
#         return value
#
#     def validate(self, data):
#         name = data.get('name')
#         city = data.get('city')
#         if name == 'Osama' and city == 'Karachi':
#             raise serializers.ValidationError('Name !Osama and city in !Karachi')
#         return data


class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=10)

    class Meta:
        model = Student
        fields = '__all__'


