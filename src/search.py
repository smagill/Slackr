from src.global_variables import get_channels
from src.utils import check_token
from src.channels import channels_list


def search(token, query_str):
    search_results = []
    user_channels = channels_list(token)

    for id_channel in user_channels[channel_id]:
        messages = user_channel[id_channel]['messages']
        for id_message in messages['message_id']:
            message = messages[id_message]['message']
            if query_str in message:
                search_results.append(message)

    return search_results
