from  django.urls import path
from  channels.routing import ProrocolTypeRtouter, URLRouter
from .consumers import LiveScoreConsumer
from channels.auth import AuthMiddlewarStack

# webSockets = URLRouter([
#     path(
#         "ws/live/<int:live_id>",
#         LiveScoreConsumer,
#         name="live"
#     )
# ])

application = ProtocolTypeRouter({
    # "webSockets" : URLRouter([
    #     path(
    #         "ws/live/<int:live_id>",
    #         LiveScoreConsumer,
    #         name="live"
    #     )
    # ])
    'websocket': AuthMiddlewarStack(
        URLRouter(
            learning.routing.websocket_urlpatterns
        )
    )
})