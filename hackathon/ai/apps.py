from django.apps import AppConfig
import os
import cohere
import openai


class AiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ai'
    co_api_key = os.getenv('COHERE_API_KEY')
    oai_api_key = os.getenv("OPENAI_API_KEY")
    openai = openai
    openai.api_key = oai_api_key
    co = cohere.Client(api_key=co_api_key)

