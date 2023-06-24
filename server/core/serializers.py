from rest_framework import serializers

from .models import Wallet
from .services.wallet_service import WalletService


class WalletCreateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['currency']


class WalletCreateResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'currency', 'public_key']


class WalletSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()

    class Meta:
        model = Wallet
        fields = ['id', 'currency', 'public_key', 'balance']

    def get_balance(self, obj):
        wallet_service: WalletService = self.context.get("wallet_service")
        return wallet_service.get_balance(obj.public_key)
