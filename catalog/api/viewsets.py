
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from catalog.api.serializers import MovieSerializer, ShowSerializer
from catalog.models import Movie, Show

"""
Views for the Movie APIs.
"""

class MovieViewSet(viewsets.ModelViewSet):
    """
    View for managing movie APIs.
    """
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    

    def get_queryset(self):
        """Retrieve movies for authenticated user"""
        # return self.queryset.filter(user=self.request.user).order_by('-id')
        return self.queryset.order_by('-id')

    


"""
Views for the Show APIs.
"""

class ShowViewSet(viewsets.ModelViewSet):
    """
    View for managing show APIs.
    """
    serializer_class = ShowSerializer
    queryset = Show.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    def get_queryset(self):
        """Retrieve movies for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')