arrayofusers = [
    {
        "id": 30,
        "username": "Ruth.Nduta",
        "email": "ruthnduta891@gmail.com",
        "messages": [
            {
                "receipient_id": 45,
                "read": False,
                "user_id": 30
            },
            {
                "receipient_id": 3,
                "read": False,
                "user_id": 30
            },
            {
                "receipient_id": 112,
                "read": False,
                "user_id": 30
            }
        ]
    },

    {
        "id": 31,
        "username": "Pascaline.Chumba",
        "email": "pjerono56@gmail.com",
        "messages": []
    },


    {
        "id": 45,
        "username": "Josephbill",
        "email": "josephbill00@gmail.com",
        "messages": [
            {
                "msg_id": 3,
                "read": True,
                "user_id": 45
            }
        ]
    },


    {
        "id": 26,
        "username": "Simon.Thuo",
        "email": "simonthuo85@gmail.com",
        "messages": []
    },


    {
        "id": 112,
        "username": "Christine.Kiage",
        "email": "christinekiage@gmail.com",
        "messages": [
                  {
                "msg_id": 45,
                "read": False,
                "user_id": 27
            },
            {
                "msg_id": 3,
                "read": False,
                "user_id": 27
            },
            {
                "msg_id": 112,
                "read": False,
                "user_id": 27
            }
            ]
    }]
def is_unread_message(message):

    return not message.get('read', True)


def has_unread_messages(user):

    return any(is_unread_message(message) for message in user['messages'])


def tag_user(user):

    if has_unread_messages(user):
        user['Tag'] = "unread"
    else:
        user['Tag'] = "read"


def filter_users(arrayofusers, targetid):

    return [user for user in arrayofusers if user['id'] != targetid]




def sort_users(relevant_users):

    return sorted(relevant_users, key=lambda x: x['Tag'] == "unread", reverse=True)


def solution(arrayofusers, targetid):    

    relevant_users = filter_users(arrayofusers, targetid)
    
    for user in relevant_users:
        tag_user(user)
    
    return sort_users(relevant_users)





target_id=26
unread_messages=solution(arrayofusers, target_id)
print (unread_messages)