from distutils.command.build_scripts import first_line_re
from typing_extensions import Required
from rest_framework import serializers
from .models import Student
 

# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField(required=False)

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         return super().update(instance, validated_data)
#         instance.first_name = validated_data.get('first_name',instance.first_name)
#         instance.last_name = validated_data.get('last_name',instance.last_name)
#         instance.number = validated_data.get('number',instance.number)
#         instance.save()
#         return instance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "number"]
        # fields = '__all__'
        # exclude = ['number']
    def validate(self, data):
        if data['first_name'] == data ['last_name']:
            raise serializers.ValidationError("first name and lastname are same")
        return data

    def validate_number(self,value):
        if value < 1000:
            raise serializers.ValidationError("number must be bigger than 1000")