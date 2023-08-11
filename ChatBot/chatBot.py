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
    "Tudo bem, vamos falar de chatbot","Não envia",
    "Manda foto pelada",
    "Fofinhas",
    "Bom dia morzinho",
    "Bom dia bb",
    "Tudo bonzinho?",
    "Tudo sim vida",
    "Dormiu gostoso hoje né",
    "Dormi vida hshshsj",
    "Aiai cansei amor",
    "Hsjsjssjsj",
    "De vim apê amor",
    "Não foram te buscar?",
    "Pq?",
    "Pai tava lavando o carro",
    "Hshdhdsh",
    "Cuidado",
    "Ah mas isso é fácil pra se tornar realidade",
    "Hshshsshs",
    "QQ achou amor?",
    "Parece meio masculino",
    "Parece",
    "Acho que é unissex né",
    "Acho que sim amor",
    "Mas não gostei muito",
    "Então não compre",
    "Sim só tinha perguntado amor hshshd",
    "Se tinha gostado",
    "Ta em casa já?",
    "Não amor",
    "Tô fazendo a unha aqui hauah",
    "Aah, pensei que era em casa",
    "parecia o potinho azul la de casa",
    "A toalha é parecida né",
    "Sim",
    "Amor, quero ir pra casa",
    "Eu imagino vida🥹",
    "Te amo tanto bebe",
    "Te amo tm meu bb",
    "O café tava bom amor?",
    "Essa mão não ficou bonita né hshshs",
    "As duas ficou bonita amor",
    "Meee amor",
    "Que ruim",
    "Só quando baixar o sol agora",
    "Uma bosta",
    "Por isso fico tão estressado",
    "Eu sei vida",

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