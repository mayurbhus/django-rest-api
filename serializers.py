from rest_framework import serializers
from .models import Book, Member, Record

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
    
class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(RecordSerializer, self).to_representation(instance)
        rep['book'] = instance.book.title
        rep['member'] = instance.member.name
        return rep