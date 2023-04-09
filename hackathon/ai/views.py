from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from ai.apps import AiConfig


class AiView(TemplateView):
    def get(self, request, prompt='Nothing...', *args, **kwargs):
        prompt = prompt
        response = AiConfig.co.generate(
            model='command-xlarge-nightly',
            prompt=prompt,
            max_tokens=40,
            temperature=0.6,
            stop_sequences=["--"]
        )
        return HttpResponse(response)
# Create your views here.
