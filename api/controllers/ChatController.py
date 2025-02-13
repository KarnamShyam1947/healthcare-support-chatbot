from flask_restx import Resource, Namespace, reqparse
from werkzeug.datastructures import FileStorage
import asyncio

from utils.LLMUtils import analyze_image_with_query, analyze_with_query
from utils.FileUtils import encode_bytes
from utils.AudioUtils import get_text_from_audio_bytes, convert_to_english, translate_to_lang

chat_controller = Namespace(
    name="Chat Controller",
    description="This description about the chat completion",
    path="/chat",
    validate=True
)

chat_args = reqparse.RequestParser()
chat_args.add_argument(
    location="files",
    type=FileStorage,
    name="image",
)
chat_args.add_argument(
    location="files",
    name="audio",
    type=FileStorage
)
chat_args.add_argument(
    name="audio_language_code",
    location="form",
    type=str
)
chat_args.add_argument(
    location="form",
    name="query",
    type=str
)

@chat_controller.route("/completion")
class ChatCompletionResource(Resource):
    def get(self):
        return {
            "hello" : "world"
        }
    
    @chat_controller.expect(chat_args)
    def post(self):
        request = chat_args.parse_args()
        print(request)
        
        if not request.get("image") and not request.get("audio"):
            query_req = request.get("query")
            resp = analyze_with_query(query_req)

        if request.get("query") and request.get("image"):
            query_req = request.get("query")
            img_bytes = encode_bytes(request.get("image").read())
            resp = analyze_image_with_query(query=query_req,encoded_image=img_bytes)

        if request.get("image") and request.get("audio"):
            img_bytes = encode_bytes(request.get("image").read())

            audio_response = get_text_from_audio_bytes(request.get("audio").read(), request.get("audio_language_code"))
            print("native language : " , audio_response)

            translated_text = asyncio.run(convert_to_english(audio_response)) \
                                if request.get("audio_language_code") != "en" \
                                else audio_response
                                
            print("English text : ", translated_text)
            
            resp = analyze_image_with_query(query=translated_text,encoded_image=img_bytes)

            actul_resp = asyncio.run(translate_to_lang(resp, request.get("audio_language_code")))
            resp = actul_resp
            print("main ", actul_resp)

        response = {
            "response" : resp
        }

        return response
    
