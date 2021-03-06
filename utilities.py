import settings


def check_maps(destination_location, gmaps):
    '''
    calculates distance and duration using google maps api
    '''

    source_location = 'Deutsche Boerse, Praha'
    result = gmaps.distance_matrix(source_location, destination_location, mode='driving')
    distance = result['rows'][0]['elements'][0]['distance']['text']
    duration = result['rows'][0]['elements'][0]['duration']['text']

    return distance, duration


def send_to_slack(sc, result, train):
    '''
    sends results to slack
    '''

    if train == 'no_trains':

        sc.api_call(
            "chat.postMessage", channel=settings.SLACK_CHANNEL, text=result,
            username='pybot', icon_emoji=':robot_face:'
        )
    elif train == 'trains':

        sc.api_call(
            "chat.postMessage", channel=settings.SLACK_CHANNEL_TRAINS, text=result,
            username='pybot', icon_emoji=':robot_face:'
        )

    else:

        sc.api_call(
            "chat.postMessage", channel=settings.SLACK_CHANNEL_LANDS, text=result,
            username='pybot', icon_emoji=':robot_face:'
        )


