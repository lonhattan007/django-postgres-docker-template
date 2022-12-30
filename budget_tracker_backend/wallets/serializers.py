from rest_framework import serializers
from .models import Wallet


class WalletSerializer(serializers.Serializer):
    class Meta:
        model = Wallet
        fields = ("name", "init_balance")
