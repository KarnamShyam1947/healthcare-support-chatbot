from flask_restx import Api

from .controllers.ChatController import chat_controller
from .controllers.SchemeController import schemes_controller

api = Api(
    title="HealthAI Connect",
    description="<replace this from the whatsapp chat>",
    validate=True,
    doc="/"
)

api.add_namespace(chat_controller)
api.add_namespace(schemes_controller)
