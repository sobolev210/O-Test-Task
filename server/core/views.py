from rest_framework import status, viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .models import Wallet
from .serializers import WalletSerializer, WalletCreateRequestSerializer, WalletCreateResponseSerializer
from .services.wallet_service import WalletService
from core.utils import get_ethereum_node_connection


class WalletViewSet(viewsets.GenericViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    wallet_service = WalletService(get_ethereum_node_connection())

    def list(self, request):
        data = self.serializer_class(
            self.get_queryset(), many=True, context={"wallet_service": self.wallet_service}
        ).data
        return Response(data)

    @extend_schema(
        request=WalletCreateRequestSerializer,
        responses={201: WalletCreateResponseSerializer}
    )
    def create(self, request):
        serializer = WalletCreateRequestSerializer(data=request.data)
        if serializer.is_valid():
            wallet = self.wallet_service.create_wallet(currency=serializer.validated_data.get("currency"))
            return Response(WalletCreateResponseSerializer(wallet).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
