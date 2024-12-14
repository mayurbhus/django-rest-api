from django.urls import path
from .views import LibrarianAPI,MemberAPI

urlpatterns = [
    
    #To see book borrowing history of all members or to add member in library:
    path('member-information', LibrarianAPI.as_view()),

    #To see book borrowing history of individual member:
    path('member-information/<member_name>/', LibrarianAPI.as_view()),

    #To see list of books:
    path('books/', MemberAPI.as_view()),

]
