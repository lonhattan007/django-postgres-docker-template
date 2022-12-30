from rest_framework import viewsets
from .models import Wallet
from .serializers import WalletSerializer

# Create your views here.


class WalletView(viewsets.ModelViewSet):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()
