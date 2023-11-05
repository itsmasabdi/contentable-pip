import requests

def log_conversation(datasetId, conversationId, messages):
    """
    Record a conversation in the database.

    :param datasetId: The ID of the dataset to which the conversation belongs
    :param conversationId: The ID of the conversation
    :param messages: List of messages in the conversation
    :return: None
    """
    
    url = f'http://localhost:3000/api/datasets/{datasetId}'
    response = requests.post(url, json={
        'conversationId': conversationId,
        'messages': messages,
    })
