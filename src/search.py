'''search function to return a collection of messages that contain a certain string'''
from src.utils import check_token
from src.channels import channels_list


def search(token, query_str):
    '''given a string, it returns all messages sent containing that string'''
    search_results = []
    check_token(token) # checking it's a valid user
    user_channels = channels_list(token)

    for id_channel in user_channels['channel_id']:
        messages = user_channels[id_channel]['messages']
        for id_message in messages['message_id']:
            message = messages[id_message]['message']
            if query_str in message:
                search_results.append(message)

    return search_results
