from flask_restx import Resource, Namespace

from utils.WebScrapUtils import get_all, get

schemes_controller = Namespace(
    name="schemes Controller",
    description="This description about the chat completion",
    path="/schemes",
    validate=True
)

@schemes_controller.route("/")
class SchemesCompletionResource(Resource):
    def get(self):
        return get_all()
    
@schemes_controller.route('/<string:slug>')
class SchemeByIdResource(Resource):
    def get(self, slug: str):
        return get(slug)
    