from Library.models import Book, Member, Record
from Library.serializers import BookSerializer, MemberSerializer, RecordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LibrarianAPI(APIView):

    #Add new member in Member table:
    def post(self, request, format=None):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #View record of all request or individual record of member if name is provided:
    def get(self, request, member_name=None, *args, **kwargs):
        if member_name:
            member_id = Member.objects.get(name=member_name).pk
            records = Record.objects.filter(member=member_id)
            serializer = RecordSerializer(records, many=True)
            return Response(serializer.data)
        else: 
            records = Record.objects.all()
            serializer = RecordSerializer(records, many=True)
            return Response(serializer.data)
        
    #Accept or deny request of book borrowing:
    #def put():

        
       
class MemberAPI(APIView):

    #Get list of books:
    def get(self, request, format=None):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)

    #Make request to borrow book:
    def post(self,request,format=None):
        data = request.data.copy()

        book_pk = Book.objects.get(title=request.data['book']).pk
        member_pk = Member.objects.get(name=request.data['member']).pk

        data['book'] = book_pk
        data['member'] = member_pk

        serializer = RecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #To see personal borrow history:
    # def get() 




#API view with @api_view decorator:

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from Library.models import Book
# from Library.serializers import BookSerializer

# @api_view(['GET','POST'])
# def book_list(request):
#     if request.method == "GET":
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET','PUT','DELETE'])
# def book_details(request, book_name):
#     #Retrieve, delete or update a book
#     try:
#         book = Book.objects.get(title = book_name)
#     except Book.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     #We got the book we wanted.

#     #To see the details of the book:
#     if request.method == "GET":
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
    
#     #To update the book details:
#     elif request.method == "PUT":
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     #To delete the book:
#     elif request.method == "DELETE":
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#API view with regular django views:

# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from Library.models import Book
# from Library.serializers import BookSerializer

# def book_list(request):
#     if request.method == 'GET': #List all books
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return JsonResponse(serializer.data,safe=False)
    
