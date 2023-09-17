from dj_rest_auth.registration.views import RegisterView
from utils.custom_serializer_register import CustomRegisterSerializer
# from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.renderers import JSONRenderer, MultiPartRenderer

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
    # parser_classes = [MultiPartParser, FormParser]
    # renderer_classes = [JSONRenderer, MultiPartRenderer]
