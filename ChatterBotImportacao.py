from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('bot')
#chatbot.storage.drop()
trainer = ListTrainer(chatbot)
"""
trainer.train([
    "Oi, tudo bem?",
    "ola, meu nome é BotImportações e estou para tirar suas duvidas sobre importações e compras nacionais",
    "gostaria de uma informação",
  "estou aqui para ajudar com as duvidas.",
  "como faço para buscar se minha compra internacional foi encaminhada?",
  "em caso de compras internacionais, você pode pedir para o vendedor ou utilizar o código de rastreamento para buscar nos sites da transportatora responsável, você pode também utilizar aplicaitvos como Muambator para realizar a busca de sua entregas, mas deve ficar atento as mudanças entre transportatoras nacionais e correios e sobre taxa aduaneira.",
  "como faço para buscar se minha compra foi encaminhada?",
  "em caso de compras nacionais, você pode pedir para o vendedor ou utilizar o código de rastreamento para buscar nos sites da transportatora responsável ou verificar no site dos correios.",
  "Como faço para verificar se minha compra foi taxada ou recebeu uma taxa aduaneira?",
  "pode utilizar o site dos correios, indo na aba minhas importações, onde você pode realizar o pagamento ou recusar o objeto.",
  "qual a chance da minha compra ser taxada ou receber uma taxa aduaneira?",
  "Atualmente , é realizado a cobrança de uma taxa aduaneira de 60% sobre encomendas internacionais, independente do valor, existe uma insenção de até US$50,00 entre pessoa física.",
  "oque faço se não receber o produto no prazo estipulado?",
  "você deve entrar em contato com o vendedor e solicitar providências",
  "como faço para verificar se minha compra internacional passou da fiscalização aduaneira?",
  "você pode utilizar o site dos correios, com o novo código de rastreamento informado quando sua compra chega no Brasil.",
  "como verifico a localização da minha compra?",
  "com o código de rastreamento, você pode verificar no site da transportadora responsável ou no site dos correios caso esse seja responsável pela entrega, alguns sites atualizam o comprador sobre a localização do produto.",
  "oque acontece se ninguem receber o produto?",
  "algumas transportadoras possuem politicas próprias, mas geralmente os correios retornam o produto até a agência, podendo realizar mais três tentativas, o cliente possui 7 (sete) dias uteis para retirar o produto. A entrega, não recebimento do produto e retorno do mesmo para agência são notificados no site do correio."
])
"""
while True:

    user_input = input('Usuário: ')

    if user_input.lower() == 'sair':
        break

    response = chatbot.get_response(user_input)

  
    print(f'ChatBot: {response}')