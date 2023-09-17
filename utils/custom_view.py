from dj_rest_auth.views import UserDetailsView
from utils.custom_serializer import CustomUserDetailsSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer, MultiPartRenderer

class CustomUserDetailsView(UserDetailsView):
    serializer_class = CustomUserDetailsSerializer
    parser_classes = [MultiPartParser, FormParser]
    renderer_classes = [JSONRenderer, MultiPartRenderer]