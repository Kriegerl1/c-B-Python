from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from numpy import True_

# # Correção do bug do Chattterbot
# from spacy.cli import download

# download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

chatbot = ChatBot("testeBotWpp", tagger_language=ENGSM)

dialog = [
    "Ola",
    "Ola, seja bem vindo!",
    "Preciso de algo",
    "Oque posso fazer por voce?",
    "Conversa comigo",
    "Claro, sobre oque gostaria?"
    "Qualquer coisa",
    "Tudo bem, vamos falar de chatbot",

]

trainer = ListTrainer(chatbot)
trainer.train(dialog)

while True:
    message = input("Digite: ")
    if message == "fim":
        break
    elif message == "limpa_Db":
        chatbot.storage.drop()
        print("O banco de dados foi limpo novamente!")
    resposta = chatbot.get_response(message)
    print(resposta)


# chatbot.storage.drop() // Limpa BD
