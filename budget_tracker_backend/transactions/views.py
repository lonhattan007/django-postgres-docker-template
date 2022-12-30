from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer

# Create your views here.


class TransactionView(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
