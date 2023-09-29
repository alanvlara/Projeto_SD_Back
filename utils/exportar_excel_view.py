from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import pandas as pd
import io 

from atividade.models import Atividade
from eventos.models import Evento
from usuario.models import Usuario

class ExportarDadosParaExcel(APIView):
    def get(self, request, evento_id):
        # Recupere todas as atividades relacionadas ao evento específico
        atividades = Atividade.objects.filter(evento__id=evento_id)
        
        # Inicialize um dicionário para armazenar a contagem de participantes por cidade
        contagem_cidades = {}

        # Itere pelas atividades para coletar as cidades dos usuários e contar
        for atividade in atividades:
            usuario = atividade.usuario
            if usuario and usuario.cidade:
                cidade = usuario.cidade
                contagem_cidades[cidade] = contagem_cidades.get(cidade, 0) + 1

        # Crie um DataFrame a partir do dicionário de contagem
        df = pd.DataFrame(list(contagem_cidades.items()), columns=['Cidade', 'Participantes'])

        # Crie um buffer de memória para armazenar o arquivo Excel
        excel_buffer = io.BytesIO()

        # Use o Pandas para escrever o DataFrame no buffer de memória
        df.to_excel(excel_buffer, index=False)

        # Configure a posição do cursor no início do buffer
        excel_buffer.seek(0)

        # Nome do arquivo Excel
        excel_file_name = 'dados_exportados.xlsx'

        # Retorne o arquivo Excel como resposta
        response = HttpResponse(excel_buffer.read(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = f'attachment; filename={excel_file_name}'

        # Certifique-se de fechar o buffer de memória após o envio da resposta
        excel_buffer.close()

        return response
