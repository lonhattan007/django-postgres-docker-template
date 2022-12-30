from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.Serializer):
    class Meta:
        model = Transaction
        fields = (
            "notes",
            "amount",
            "category",
            "currency",
            "date",
        )
