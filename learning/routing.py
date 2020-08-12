from  django.urls import path, re_path
# from  channels.routing import ProrocolTypeRtouter, URLRouter
# from .consumers import LiveScoreConsumer
from . import consumers

# webSockets = URLRouter([
#     path(
#         "ws/live/<int:live_id>",
#         LiveScoreConsumer,
#         name="live"
#     )
# ])

websockets_urlpatterns = [
    re_path(r'ws/live/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]