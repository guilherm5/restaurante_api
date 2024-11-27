import os
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.conf import settings
from .models import DetailLine, GuestCheck
from .serializers import DetailLineSerializer, GuestCheckSerializer
from django.core.exceptions import ValidationError

class GetFiscalInvoiceAPIView(APIView):
    def post(self, request):
        store_id = request.data.get('storeId')
        bus_dt_str = request.data.get('busDt')

        if not store_id or not bus_dt_str:
            return Response({"error": "Both storeId and busDt are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Convertendo busDt para o formato de data
            bus_dt = datetime.strptime(bus_dt_str, "%Y-%m-%d").date()
            
            # Filtrando os registros de detail_lines
            detail_lines = DetailLine.objects.filter(
                guest_check_line_item_id=store_id, bus_dt=bus_dt
            )

            if not detail_lines.exists():
                return Response({"error": "No data found for the given guestCheckLineItemId and busDt."}, status=status.HTTP_404_NOT_FOUND)

            # Serializando os dados
            serializer = DetailLineSerializer(detail_lines, many=True)
            data = serializer.data

            # Salvando os dados no Data Lake (em JSON)
            file_path = os.path.join(settings.DATA_LAKE_PATH, 'fiscal_invoices', f'{store_id}_{bus_dt}.json')
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)

            return Response(data, status=status.HTTP_200_OK)

        except ValueError:
            return Response({"error": "Invalid busDt format, expected YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

class GetGuestChecksAPIView(APIView):
    def post(self, request):
        store_id = request.data.get('storeId')
        bus_dt_str = request.data.get('busDt')

        if not store_id or not bus_dt_str:
            return Response({"detail": "Missing parameters: storeId or busDt"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Convertendo busDt para o formato de data
            bus_dt = datetime.strptime(bus_dt_str, "%Y-%m-%d").date()

            # Filtrando os registros de guest_checks
            guest_checks = GuestCheck.objects.filter(
                guest_check_id=store_id, clsd_bus_dt=bus_dt
            )

            if not guest_checks.exists():
                return Response({"detail": "No guest checks found for this ID and date."}, status=status.HTTP_404_NOT_FOUND)

            # Serializando os dados
            serializer = GuestCheckSerializer(guest_checks, many=True)
            data = serializer.data

            # Salvando os dados no Data Lake (em JSON)
            file_path = os.path.join(settings.DATA_LAKE_PATH, 'guest_checks', f'{store_id}_{bus_dt}.json')
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)

            return Response(data, status=status.HTTP_200_OK)

        except ValueError:
            return Response({"detail": "Invalid busDt format, expected YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)

class GetTransactionsAPIView(APIView):
    def post(self, request):
        store_id = request.data.get('storeId')
        bus_dt_str = request.data.get('busDt')

        if not store_id:
            return Response({"error": "storeId is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Se bus_dt for fornecido, converte para formato de data
            if bus_dt_str:
                bus_dt = datetime.strptime(bus_dt_str, "%Y-%m-%d").date()
                guest_check = GuestCheck.objects.filter(
                    guest_check_id=store_id, clsd_bus_dt=bus_dt
                ).first()
            else:
                guest_check = GuestCheck.objects.filter(guest_check_id=store_id).first()

            if not guest_check:
                return Response({"error": "No guest check found for the given storeId."}, status=status.HTTP_404_NOT_FOUND)

            # Buscando as transações de detail_lines
            detail_lines = DetailLine.objects.filter(guest_check_id=store_id)

            if not detail_lines.exists():
                return Response({"error": "No transaction details found for the given guestCheckId."}, status=status.HTTP_404_NOT_FOUND)

            # Serializando os dados
            serializer = DetailLineSerializer(detail_lines, many=True)
            data = serializer.data

            # Salvando os dados no Data Lake (em JSON)
            file_path = os.path.join(settings.DATA_LAKE_PATH, 'transactions', f'{store_id}_{bus_dt if bus_dt_str else "no_date"}.json')
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)

            return Response(data, status=status.HTTP_200_OK)

        except ValueError:
            return Response({"error": "Invalid busDt format, expected YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)