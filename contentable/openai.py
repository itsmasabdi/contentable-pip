import os
import uuid
import openai
import requests
from .utils import log_conversation

class OpenAI:
    class ChatCompletion:
        @staticmethod
        def create_stream(datasetId, conversationId, messages, *args, **kwargs):
            response = openai.ChatCompletion.create(messages=messages, *args, **kwargs)
            content = ""
            for chunk in response:
                content += chunk['choices'][0]['delta']['content'] if 'content' in chunk['choices'][0]['delta'] else ''
                yield chunk
            messages.append({
              'role': 'assistant',
              'content': content,
            })
            log_conversation(datasetId, conversationId, messages)

        @staticmethod
        def create_non_stream(datasetId, conversationId, messages, *args, **kwargs):
            response = openai.ChatCompletion.create(messages=messages, *args, **kwargs)
            if 'message' in response['choices'][0]:
              messages.append(response['choices'][0]['message'].to_dict())
            log_conversation(datasetId, conversationId, messages)
            return response

        @staticmethod
        def create(*args, **kwargs):
            messages = kwargs.pop('messages', [])
            stream = kwargs.get('stream', False)
            datasetId = kwargs.pop('datasetId', None)
            conversationId = kwargs.pop('conversationId', uuid.uuid4().hex)

            if stream:
                return OpenAI.ChatCompletion.create_stream(datasetId, conversationId, messages, *args, **kwargs)
            else:
                return OpenAI.ChatCompletion.create_non_stream(datasetId, conversationId, messages, *args, **kwargs)
