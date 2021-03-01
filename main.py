import json
import facebook
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging
import requests

from datetime import datetime

ACCESS_TOKEN = "EAAEi4hH3af8BAIJT4FKgdTYZCVanA2h8VPPYMMZCpVfy9GTVKPdrpfvzrp5PuB88UEEVJ1HtkZAcRyP4LeV4jb4MieXwam3EwwR3AAtg3imlB7Guc1dVTHnCkay2NPCdPpDnHRzWaql7nlZBZBgwkQgfKbW3mpdg5ZAfHjoxzszQZDZD"
USER_ACCESS_TOKEN = 'EAAEi4hH3af8BANGEKJviyR7iBhAgQGhZCKpiZB1IdgwuBCOYzV9TcTNbBNTaGL4MEAtXjjuq50AwwoX36hg8aFd1DAifRqLlToMncHZCVjXqlSPZBiZAbOXf7CFFgoshGbW1fOskxoonSDfXtCIjPemd2qkD709QCTc739qc8DwZDZD'

PAGE_ID = '109481484526683'
USER_ID = "100662435385739"
HOST = "https://graph.facebook.com/"
POST_COMMENT_ID = "109481484526683_109630051178493"


def chatterbot(conversation):
    chatbot = ChatBot('Crux')
    chatbot.storage.drop()
    trainer = ListTrainer(chatbot)
    trainer.train(conversation)
    return chatbot


def get_user_name(graph):
    name = graph.get_object(USER_ID, field='name')
    return name


def get_posts(graph):
    posts = graph.get_object(PAGE_ID, fields='feed')
    return posts


def get_profile(graph, user_id):
    profile = graph.get_object(user_id, fields='first_name, location, link, email, posts, friends')
    return profile


def get_page_info(graph, page_id):
    page_info = graph.get_object(page_id, field='name ,location, link, posts, feed')
    return page_info


def get_user_friends(graph):
    friends = graph.get_object('me', fields='friends')
    return friends


def get_post_message(graph, post_id):
    # Get the message from a post.
    post = graph.get_object(PAGE_ID, id=post_id, fields='message')
    print(post['message'])
    return post['message']


def get_post_comments(graph, post_id):
    return graph.get_object(post_id, fields='comments')


def make_post(graph):
    text = input("Ingrese el texto que desea postear: ")
    post = graph.put_object(parent_object='me', connection_name='feed', message=text)
    print(json.dumps(post, indent=4))


def put_comment(graph, post_id, text):
    return graph.put_comment(object_id=post_id, message=text)


def make_comment(graph):
    post_id = enter_object_id()
    message = input('Ingrese el comentario que desea hacer: ')
    while not message:
        message = input('Ingrese el comentario que desea hacer: ')
    comment = put_comment(graph, post_id, message)
    print(json.dumps(comment, indent=4))


def put_like(graph, object_id):
    like = graph.put_like(object_id)
    print(like)


def put_photo(graph, photo_jpg, text):
    # Upload an image with a caption.
    # nombre del archivo de la foto
    photo_id = graph.put_photo(image=open(photo_jpg, 'rb'), message=text)
    return photo_id


def post_photo(graph):
    photo_jpg = input('Ingrese el nombre de la foto que desea subir: ')
    while '.jpg' not in photo_jpg:
        photo_jpg = input('Ingrese el nombre de la foto que desea subir: ')

    message = input('Ingrese el mensaje que desea postear junto a la foto: ')
    post = put_photo(graph, photo_jpg, message)
    print(json.dumps(post, indent=4))


def send_message(graph, message):
    graph.put_objet


# def update_post(graph, post_id, text):
#     valid = graph.update_post(object_id = post_id, message = text)
#     if valid:
#         print('Post actualizado!')
#     else: 
#         print('No se ha podido actualizar el post.')

def update_profile(graph, ):
    valid = graph.update_profile(parent_object='me')


def searh_users(graph, user_id):
    search = graph.searh_users(user_id)
    return search


def enter_object_id():
    object_id = input('Ingrese el id del post o comentario deseado: ')
    return int(object_id)


def liking_post(graph):
    object_id = enter_object_id()
    put_like(graph, object_id)


def read_line(file):
    line = file.readline()
    if line:
        return line.rstrip("\n").split(',')
    else:
        return '', ''


def read_file(file_name):
    conversation = []
    with open(file_name) as file:
        user_response, chatbot_response = read_line(file)
        while user_response:
            conversation.append(user_response)
            conversation.append(chatbot_response)
            user_response, chatbot_response = read_line(file)
        return conversation

def main():
    token = ACCESS_TOKEN
    graph = facebook.GraphAPI(token)
    conversation = read_file('trainer.txt')
    chatbot = chatterbot(conversation)

    peticion = input('Tú: ')
    while peticion != 'chau':
        response = chatbot.get_response(peticion)
        print(response)
        if peticion == '1':
            make_post(graph)
        elif peticion == '2':
            liking_post(graph)
        elif peticion == '3':
            make_comment(graph)
        peticion = input('Tú: ')

    profile = get_profile(graph, USER_ID)
    page_info = get_page_info(graph, PAGE_ID)
    put_like(graph, '109631641178334')

    # print('Printing profile: ')
    # print(friends)
    #print(json.dumps(profile, indent=4))
    #print(type(json.dumps(profile, indent=4)))
    #print(json.dumps(page_info, indent=4))
    print(conversation)


if __name__ == '__main__':
    main()
