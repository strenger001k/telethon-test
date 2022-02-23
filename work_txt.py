def get_list_id():
    with open('chat_list.txt', 'r') as file:
        id_list = [int(line[:-1]) for line in file]
    return id_list
