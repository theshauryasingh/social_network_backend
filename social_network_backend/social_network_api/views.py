from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from .models import CustomUser, Friendrequest
from django.db import IntegrityError
from .serializers import CustomUserSerializer, FriendRequestSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'], authentication_classes=[], permission_classes=[AllowAny])
    def signup(self, request):
        print(' signup req')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], authentication_classes=[], permission_classes=[AllowAny])
    def signin(self, request):
        print(' signin req')
        username = request.data.get('username')
        password = request.data.get('password')
        user = CustomUser.objects.filter(username=username).first()
        if user and user.check_password(password):
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)


class FriendRequestViewSet(viewsets.ModelViewSet):
    print(' FriendRequestViewSet 1')
    queryset = Friendrequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['patch'])
    def updatestatus(self, request):
        friend_request = self.get_object(pk = request.data.get('pk'))
        new_status = request.data.get('status')

        if new_status:
            friend_request.status = new_status
            friend_request.save()
            return Response({'message': 'Friend request status updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Status field is required'}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        try:
            serializer.save(fromuser=self.request.user)
        except IntegrityError:
            return Response(
                {"error": "Friend request already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def get_queryset(self):
        status = self.request.query_params.get('status')
        if status:
            return Friendrequest.objects.filter(touser=self.request.user, status=status)
        return Friendrequest.objects.filter(touser=self.request.user)