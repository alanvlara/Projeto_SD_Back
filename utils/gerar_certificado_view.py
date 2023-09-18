from django.http import FileResponse
import requests
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from atividade.models import Atividade
from django.utils import timezone  
from django.conf import settings


def gerar_certificado(request, atividade_id):
    # Obtenha os dados da atividade com base no atividade_id
    atividade = Atividade.objects.get(pk=atividade_id)

    # Crie um objeto BytesIO para armazenar o PDF
    from io import BytesIO
    buffer = BytesIO()

    # Crie o PDF usando o ReportLab
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setTitle('Certificado')

    data_formatada = atividade.evento.data.strftime('%d/%m/%Y')  # Formata a data
    
    # Use o requests para baixar a imagem do Amazon S3
    s3_url = 'https://desporpato.s3.sa-east-1.amazonaws.com/media/padroes/certificado.jpg'
    response = requests.get(s3_url)

    if response.status_code == 200:
        image_data = BytesIO(response.content)

        # Use a imagem baixada para desenhar no PDF
        p.drawImage(ImageReader(image_data), 0, 0, width=letter[0], height=letter[1])
        font_size_normal = 15
        font_size_bold = 30
        p.setFont("Helvetica-Bold", font_size_bold)

        width, height = letter

        # String 1: Certificado de Participação (centralizada)
        text1 = "Certificado de Participação"
        x_position1 = width  / 2
        y_position1 = height - 200
        p.drawCentredString(x_position1, y_position1, text1)

        # Definir estilo de fonte para strings subsequentes
        p.setFont("Helvetica", font_size_normal)

        # String 2: Certificamos que (centralizada)
        text2 = "Certificamos que"
        x_position2 = width / 2
        y_position2 = y_position1 - 100  # Ajuste conforme necessário
        p.drawCentredString(x_position2, y_position2, text2)

        # String 3: Nome do participante (centralizado, negrito e fonte aumentada)
        text3 = f'{atividade.usuario.first_name} {atividade.usuario.last_name}'
        p.setFont("Helvetica-Bold", font_size_bold)
        x_position3 = width / 2
        y_position3 = y_position2 - 40  # Ajuste conforme necessário
        p.drawCentredString(x_position3, y_position3, text3)

        # String 4: Detalhes da atividade
        text4 = f"participou do/a {atividade.evento.titulo} no dia {data_formatada}"
        p.setFont("Helvetica", font_size_normal)
        x_position4 = width / 2  # Ajuste conforme necessário
        y_position4 = y_position3 - 50  # Ajuste conforme necessário
        p.drawCentredString(x_position4, y_position4, text4)

        # Adicionar espaço de assinatura
        signature_y = 100  # Ajuste conforme necessário
        p.setFont("Helvetica", font_size_normal)
        p.drawCentredString((width/2), (y_position3 - 300), "Assinatura do Diretor do Evento")

        p.save()

    # Volte ao início do buffer e retorne o PDF
    buffer.seek(0)
    response = FileResponse(buffer, as_attachment=True, filename='certificado.pdf')
    return response
