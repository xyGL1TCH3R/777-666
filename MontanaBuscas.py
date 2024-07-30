import telebot, requests, requests_html, json, re, urllib3, os
from os import system, name
from telebot import TeleBot, types

bot = telebot.TeleBot("7229451684:AAF3uRXiU81aMRx4eaD-d9whwRiUSfVSW4c", parse_mode=None)

PRIVADO = [5810047270]

###################################

GRUPO = []

###################################

EXCEPT = []

###############################################
###############################################
#                     START
###############################################

@bot.message_handler(commands=['start'])
def START(message1):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Iniciar')
    ide = message1.chat.id
    liste = PRIVADO + GRUPO + EXCEPT
    markup.add(item1)

    if ide in liste:
        #bot.send_message(message.chat.id, 'teste, {0.first_name}!'.format(message.from_user), reply_markup = markup)
        bot.reply_to(message1, '<b>' 'Bem-vindo Chefe 🌎💰' '</b>', parse_mode='HTML')
        bot.send_message(ide, '✅ ' '<b>' 'use ' '</b>''<code>' '/menu' '</code>''<b>' ' veja os comandos' '</b>' ' ✅', parse_mode='HTML')
        #bot.send_message(message.chat.id, 'teste, {0.first_name}!'.format(message.from_user), reply_markup = markup)
    
    else:
        bot.reply_to(message1, '<b>' + '🚫 ' + '@'+message1.chat.username + ' VOCÊ NÃO TEM ACESSO 🚫' '</b>', parse_mode='HTML')
        bot.send_message(ide, '<b>' 'Você não tem autorização para ultilizar esse comando!' '</b>', parse_mode='HTML')
                		
################################################

session = requests_html.HTMLSession()

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):

    if call.data == 'deletar':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


################################################
###############################################
               # MENU DO BOT #
###############################################
###############################################

@bot.message_handler(commands=['menu'])
def MENU(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/menuu':
        bot.reply_to(men, '<b>' + '⚠ KKK COMANDO ERRADO ⚠' + '</b>', parse_mode='HTML')
    else:
        try:
        	bot.reply_to(men, '<b>' '🔍 MENU BOT 🔎' '</b>' + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + '<b>' 
            '[+] CEP:</b><code> /cep 89233013' '</code>' + '\n' + '<b>' 
            '[+] COVID19:</b><code> /covid19 SP' '</code>' + '\n' + '<b>'
            '[+] BIN:</b><code> /bin 552289' + '</code>' '\n' + '<b>' 
            '[+] NOME:</b><code> /nome Jacinto leite Aquino rego' + '</code>' '\n' + '<b>' 
            '[+] CNPJ:</b><code> /cnpj 27865757000102' + '</code>' '\n' + '<b>' 
            '[+] CPF SIMPLES: ' '</b>''<code>' '/cpf_simples 29993559806' '</code>' + '\n' + '<b>'  
            '[+] CPF CADSUS: ' '</b>''<code>' '/cpf_cadsus 29993559806' '</code>' + '\n' + '<b>'
            '[+] CPF RECEITA: ' '</b>''<code>' '/cpf_receita 34288575850' '</code>' + '\n' + '<b>'
            '[+] IP: ' '</b>' '<code>' + '/ip 204.152.203.157' + '</code>' + '\n' + '<b>' 
            '[+] PLACA: ' '</b>' + '<code>' '/placa GTJ6699' '</code>' + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + 
            '<b>🥋 CHEFE: @isTony_Montana \n</b>' , parse_mode='HTML')
        except:
                    bot.reply_to(men, '<b>' + '.' + '</b>', parse_mode='HTML')

################################################
###############################################
            # CONSULTA DE CEP #
###############################################
###############################################

@bot.message_handler(commands=['cep'])
def cep(message):
    dell = types.InlineKeyboardButton(text='🚮  APAGAR  🚮', callback_data='deletar')
    keyboardmain = types.InlineKeyboardMarkup(row_width=3)
    keyboardmain.add(dell)
    cep = message.text.replace('/cep ', '')
    if message.text == '/cep':
        return 'Insira o CEP após o comando!'

    else:
        try:
            r = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()
            cep = r['cep']
            uf = r['uf']
            cidade = r['localidade']
            bairro = r['bairro']
            ddd = r['ddd']

            ui = f'''
🔍 CONSULTA DE CEP 🔎
▱▱▱▱▱▱▱▱▱▱▱▱▱
• CEP: {cep} 
• UF: {uf} 
• CIDADE: {cidade} 
• BAIRRO: {bairro} 
• DDD: {ddd} 
▱▱▱▱▱▱▱▱▱▱▱▱▱
• DONO DO BOT: @isTony_Montana
'''
            bot.reply_to(message,reply_markup=keyboardmain,text=ui)

        except:
            nu = '⚠️ CEP NÂO ENCONTRADO ⚠️'
            bot.reply_to(message,reply_markup=keyboardmain,text=nu)


################################################
###############################################
            # CONSULTA DE BIN #
###############################################
###############################################

@bot.message_handler(commands=['bin'] + ['BIN'])
def BIN(men):
            notbin = []
            bid = men.chat.id
            cp = men.text
            if bid in notbin:
                bot.reply_to(men, '⚠ 𝙘𝙤𝙣𝙨𝙪𝙡𝙩𝙖 𝙙𝙚 𝙗𝙞𝙣 𝙙𝙚𝙨𝙖𝙩𝙞𝙫𝙖𝙙𝙖 ⚠')
            else:
                try:
                    bn = re.sub('[^0-9]', '', cp)
                    response = requests.get('https://binlist.io/lookup/{}'.format(bn))
                    res = response.content
                    r = json.loads(res)
                    if str(r['success']) == str('True'):

                        bot.reply_to(men, '\n         ㅤ   ㅤ<b>🔍 DADOS BIN 🔎</b>\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n<b>• BIN</b>: ' + '<code>' + str(
                            r['number']['iin']) + '</code>' + '\n' +
                                     '<b>• BANDEIRA</b>: ' + '<code>' + str(r['scheme']) + '</code>' + '\n' +
                                     '<b>• TIPO</b>: ' + '<code>' + str(r['type']) + '</code>' + '\n' +
                                     '<b>• NÍVEL</b>: ' + '<code>' + str(r['category']) + '</code>' + '\n' +
                                     '<b>• BANCO</b>: ' + '<code>' + str(r['bank']['name']) + '</code>' + '\n' +
                                     '<b>• TEL BANCO</b>: ' + '<code>' + str(r['bank']['phone']) + '</code>' + '\n' +
                                     '<b>• URL</b>: ' + str(r['bank']['url']) + '\n' +
                                     '<b>• PAÍS</b>: ' + '<code>' + str(r['country']['name']) + '</code>' + '\n' +
                                     '<b>• ID</b>: ' + '<code>' + str(r['country']['alpha3']) + '</code>' + '\n' +
                                     '<b>• SIGLA</b>: ' + '<code>' + str(r['country']['alpha2']) + '</code>' + '\n' +  
                                     '▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '<b> '• CRIADOR: @isTony_Montana' + '\n' + '</b>', parse_mode='HTML')
                    else:
                        bot.reply_to(men, '<b>VEJA O EXEMPLO</b>: "' + '<code>' + '/bin 651652' + '</code>' + '"', parse_mode='HTML')
                except:
                    bot.reply_to(men, '<b>⚠ DIGITE UMA BIN PORRA ⚠</b>', parse_mode='HTML')

################################################
###############################################
           # CONSULTA DE CNPJ #
###############################################
###############################################

@bot.message_handler(commands=['cnpj', 'CNPJ'])
def CNPJ(men):
            liberadocnpj = PRIVADO + GRUPO + EXCEPT
            bid = men.chat.id
            if bid in liberadocnpj:
                mensagem = men.text
                if men.text == '/cnpj':
                    bot.reply_to(men, '<b>' '⚠ 𝘿𝙄𝙂𝙄𝙏𝙀 𝙐𝙈 𝘾𝙉𝙋𝙅 ⚠' '</b>', parse_mode='HTML')
                elif men.text == '/CNPJ':
                    bot.reply_to(men, '<b>' '⚠ 𝘿𝙄𝙂𝙄𝙏𝙀 𝙐𝙈 𝘾𝙉𝙋𝙅, 𝙄𝘿𝙄𝙊𝙏𝘼 ⚠' '</b>', parse_mode='HTML')
                else:
                    try:
                        cnpj = re.sub('[^0-9.]', '', mensagem)
                        url = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj))
                        req = json.loads(url.text)
                        bot.reply_to(men,'ㅤㅤㅤㅤ🔍 𝘿𝘼𝘿𝙊𝙎 𝘾𝙉𝙋𝙅 🔎' +
'▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n𝘾𝙉𝙋𝙅: ' '<code>' + str(req['cnpj']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙏𝙄𝙋𝙊: ' '<code>' + str(req['tipo']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙉𝙊𝙈𝙀: ' '<code>' + str(req['nome']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙏𝙀𝙇𝙀𝙁𝙊𝙉𝙀𝙎: ' '<code>' + str(req['telefone']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙀𝙈𝘼𝙄𝙇: ' '<code>' + str(req['email']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙎𝙄𝙏𝙐𝘼𝘾̧𝘼̃𝙊: ' '<code>' + str(req['situacao']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙇𝙊𝙂𝙍𝘼𝘿𝙊𝙐𝙍𝙊: ' '<code>' + str(req['logradouro']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝘽𝘼𝙄𝙍𝙍𝙊: ' '<code>' + str(req['bairro']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙉𝙐́𝙈𝙀𝙍𝙊: ' '<code>' + str(req['numero']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + 
                     '𝘾𝙀𝙋: ' '<code>' + str(req['cep']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + 
                     '𝙈𝙐𝙉𝙄𝘾𝙄́𝙋𝙄𝙊: ' '<code>' + str(req['municipio']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n'
                     '𝙋𝙊𝙍𝙏𝙀: ' '<code>' + str(req['porte']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝘼𝘽𝙀𝙍𝙏𝙐𝙍𝘼: ' '<code>' + str(req['abertura']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙁𝘼𝙉𝙏𝘼𝙎𝙄𝘼: ' '<code>' + str(req['fantasia']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙎𝙏𝘼𝙏𝙐𝙎: ' '<code>' + str(req['status']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝘾𝘼𝙋𝙄𝙏𝘼𝙇: ' '<code>' + str(req['capital_social']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n'
                     #'𝘼𝙏𝙄𝙑𝙄𝘿𝘼𝘿𝙀 𝙋𝙍𝙄𝙉𝘾𝙄𝙋𝘼𝙇: ' '<code>' + str(req['atividade_principal']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     #'𝘼𝙏𝙄𝙑𝙄𝘿𝘼𝘿𝙀 𝙎𝙀𝘾𝙐𝙉𝘿𝘼́𝙍𝙄𝘼: ' '<code>' + str(req['atividades_secundarias']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝘿𝘼𝙏𝘼 𝙎𝙄𝙏𝙐𝘼𝘾̧𝘼̃𝙊: ' '<code>' + str(req['data_situacao']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + 
                     '𝙐𝙁: ' '<code>' + str(req['uf']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + 
                     '𝘿𝙊𝙉𝙊𝙎: ' '<code>' + str(req['qsa']) + '</code>'  '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝘾𝘼𝙉𝘼𝙇:  @isTony_Montana', parse_mode='HTML')

                    except:
                        bot.reply_to(men, '<b>𝙊𝙋𝙎, 𝘾𝙉𝙋𝙅 𝙉Â𝙊 𝙀𝙉𝘾𝙊𝙉𝙏𝙍𝘼𝘿𝙊 𝙂𝘼𝘿𝙊 🐂</b>', parse_mode='HTML')
            else:
                bot.reply_to(men, '<b>Você não tem autorização para ultilizar esse comando!</b>', parse_mode='HTML')

################################################
###############################################
              # CPF SIMPLES #
###############################################
###############################################

@bot.message_handler(commands=['cpf_simples', 'CPF_SIMPLES'])
def CPF_SIMPLES(men):
            liberadocpfsimples = PRIVADO + GRUPO + EXCEPT
            bid = men.chat.id
            if bid in liberadocpfsimples:
                mensagem = men.text
                if men.text == '/cpf_simples':
                    bot.reply_to(men, '<b>' 'DIGITE UM CPF VALIDO!' '</b>', parse_mode='HTML')
                elif men.text == '/CPF_SIMPLES':
                    bot.reply_to(men, '<b>' 'DIGITE UM CPF VALIDO!' '</b>', parse_mode='HTML')
                else:
                    try:
                        cpfsimples = re.sub('[^0-9.]', '', mensagem)
                        url = requests.get('https://nettinn.000webhostapp.com/Consulta.php?cpf={}'.format(cpfsimples))
                        req = json.loads(url.text)
                        bot.reply_to(men, '\n         ㅤ   <b>🔍 DADOS DO NOME 🔎</b>\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '<b>• NOME</b>: ' + '<code>' + str(req['nome']) + '</code>' + '\n' +
                                     '<b>• CPF</b>: ' + '<code>' + str(req['cpf']) + '</code>' + '\n' +
                                     '<b>• SEXO</b>: ' + '<code>' + str(req['sexo']) + '</code>' + '\n' +
                                     '<b>• NASCIMENTO</b>: ' + '<code>' + str(req['anoNasc']) + '</code>' + '\n' +
                                     '▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '<b>• VIZINHOS</b>: ' + '<code>' + str(req['vizinhos']) + '</code>' + '\n' +
                                     '▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '• BOT: @Imperiosearchbot' + '\n' + 
                                     '• DONOS: @isTony_Montana ' + '</b>', parse_mode='HTML')
                    except:
                        bot.reply_to(men, '<b>CPF NÃO ENCONTRADO</b>', parse_mode='HTML')
            else:
                bot.reply_to(men, '<b>Você não tem autorização para ultilizar esse comando!</b>', parse_mode='HTML')

################################################
###############################################
              # CONSULTA DE IP #
###############################################
###############################################

@bot.message_handler(commands=['ip', 'IP'])
def IP(men):
            liberadoip = PRIVADO + GRUPO + EXCEPT
            bid = men.chat.id
            if bid in liberadoip:
                mensagem = men.text
                if men.text == '/ip':
                    bot.reply_to(men, '<b>' 'DIGITE UM IP!' '</b>', parse_mode='HTML')
                elif men.text == '/IP':
                    bot.reply_to(men, '<b>' 'DIGITE UM IP, ANIMAL!' '</b>', parse_mode='HTML')
                else:
                    try:
                        ip = re.sub('[^0-9.]', '', mensagem)
                        url = requests.get('http://ip-api.com/json/{}'.format(ip))
                        req = json.loads(url.text)
                        bot.reply_to(men,
                                     '▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '𝙄𝙋: ' + req['query'] + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '𝙋𝘼𝙄́𝙎: ' + req['country'] + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '𝙎𝙄𝙂𝙇𝘼 𝙋𝘼𝙄́𝙎: ' + str(req['countryCode']) + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '𝙍𝙀𝙂𝙄𝘼̃𝙊: ' + str(req['region']) + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '𝙍𝙀𝙂𝙄𝘼̃𝙊 𝙉𝘼𝙈𝙀: ' + str(req['regionName']) + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '𝘾𝙄𝘿𝘼𝘿𝙀: ' + str(req['city']) + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '𝘾𝙀𝙋: ' + str(req['zip']) + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '𝙇𝘼𝙏𝙄𝙏𝙐𝘿𝙀: ' + str(req['lat']) + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '𝙇𝙊𝙉𝙂𝙄𝙏𝙐𝘿𝙀: ' + str(req['lon']) + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '𝙋𝙍𝙊𝙑𝙀𝘿𝙊𝙍: ' + str(req['org']) + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                    except:
                        bot.reply_to(men, '<b>IP NÃO ENCONTRADO</b>', parse_mode='HTML')
            else:
                bot.reply_to(men, '<b>Você não tem autorização para ultilizar esse comando! </b>', parse_mode='HTML')

################################################
###############################################
                  #COVID 19
###############################################
###############################################

@bot.message_handler(commands=['covid19'])
def COVID19(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + EXCEPT
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split('/covid19')
                    ipp = re.sub('[^A-Z]', '', msg)
                    #ip = re.sub('[^0-9]', '', msg)
                    url = requests.get("https://covid19-brazil-api.vercel.app/api/report/v1/brazil/uf/" + ipp)
                    req = url.json()
                    response = f'🔍<b>ESTATÍSTICAS ENCONTRADAS</b>🔍\n\n<b>• UF</b>: <code>{req["uf"]}</code>\n<b>• ESTADO</b>: <code>{req["state"]}</code>\n<b>• CASOS</b>: <code>{req["cases"]}</code>\n<b>• MORTES</b>: <code>{req["deaths"]}</code>\n<b>• SUSPEITAS</b>: <code>{req["suspects"]}</code>\n<b>• RECUSADOS</b>: <code>{req["refuses"]}</code>\n\n<b> • By</b>: @DKZINBR'
                    bot.reply_to(nome, response, parse_mode="html")
                except:
                 bot.reply_to(nome, '<b>ESTADO NÃO FOI ENCONTRADA</b>', parse_mode='html')
            else:
                  bot.reply_to(nome, '''VOCÊ NÃO TEM AUTORIZAÇÃO

<SEM PERMISSÃO
━━━━━━━━━━━━━━━━━''', parse_mode='html')

###############################################
###############################################
              # PLACA SIMPLES
###############################################
###############################################

@bot.message_handler(commands=['placa','placa3','veiculo','placa4'])
def PLACA_SIMPLES(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + EXCEPT
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split('/placa')
                    ipp = re.sub('[^A-Z]', '', msg)
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get("https://apicarros.com/v2/consultas/" + ipp + ip + "/f63e1e63dd231083d38ce929984aac7d", verify=False)
                    req = url.json()
                    response = f'🔍<b>PLACA ENCONTRADA</b>🔍\n\n<b>• PLACA</b>: <code>{req["placa"]}</code>\n<b>• ANO</b>: <code>{req["ano"]}</code>\n<b>• CHASSI</b>: <code>{req["chassi"]}</code>\n<b>• COR</b>: <code>{req["cor"]}</code>\n<b>• DATA</b>: <code>{req["data"]}</code>\n<b>• ALERME</b>: <code>{req["dataAtualizacaoAlarme"]}</code>\n<b>• VEICULO</b>: <code>{req["dataAtualizacaoCaracteristicasVeiculo"]}</code>\n<b>• ROUBO/FURTO</b>: <code>{req["dataAtualizacaoRouboFurto"]}</code>\n<b>• MARCA</b>: <code>{req["marca"]}</code>\n<b>• MODELO</b>: <code>{req["modelo"]}</code>\n<b>• MUNICÍPIO</b>: <code>{req["municipio"]}</code>\n<b>• UF</b>: <code>{req["uf"]}</code>\n<b>• SITUAÇÃO</b>: <code>{req["situacao"]}</code>\n\n<b>• By</b>: @DKZINBR'
                    bot.reply_to(nome, response, parse_mode="html")
                except:
                 bot.reply_to(nome, '<b>⚠️NÃO ECONTRADO</b>', parse_mode='html')
            else:
                  bot.reply_to(nome, '''VOCÊ NÃO TEM AUTORIZAÇÃO

<SEM PERMISSÃO
━━━━━━━━━━━━━━━━━''', parse_mode='html')

###############################################
###############################################
             #Consulta Cadsus
###############################################
###############################################

@bot.message_handler(commands=['cpf_cadsus', 'CPF_CADSUS'])
def CPF_CADSUS(men):
            liberadocpfcadsus = PRIVADO + GRUPO + EXCEPT
            bid = men.chat.id
            if bid in liberadocpfcadsus:
                mensagem = men.text
                if men.text == '/cpf_cadsus':
                    bot.reply_to(men, '<b>' 'DIGITE UM CPF !!!' '</b>', parse_mode='HTML')
                elif men.text == '/CPF_CADSUS':
                    bot.reply_to(men, '<b>' 'DIGITE UM CPF, KRL !!!' '</b>', parse_mode='HTML')
                else:
                    try:
                        cpfcadsus = re.sub('[^0-9.]', '', mensagem)
                        url = requests.get('https://api.i-find.dev/?token=110558cd-281a-4244-aabc-228a24a8c0f3&cpf={}'.format(cpfcadsus))
                        req = json.loads(url.text)
                        bot.reply_to(men,'<b>' 
                                     'ㅤ🔍 CONSULTA CPF CADSUS 🔎' '</b>' + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n\n' + '<b>'
                                     '• 📃 DOCUMENTOS: ' '</b>' '<code>' + '</code>' '\n' + '<b>'  
                                     '• NOME: ' '</b>' '<code>' + req['nome'] + '</code>' '\n' + '<b>' 
                                     '• SEXO: ' '</b>' '<code>' + req['sexo'] + '</code>' '\n' + '<b>'
                                     '• CNS: ' '</b>' '<code>' + req['numeroCns'] + '</code>' '\n' + '<b>' 
                                     '• CPF: ' '</b>' '<code>' + req['cpf'] + '</code>' '\n' + '<b>'
                                     '• DATA DE NASCIMENTO: ' '</b>' '<code>' + req['dataNascimento'] + '</code>' '\n\n' + '<b>'

                                     '• 🌡 CARACTERISTICAS: ' '</b>' '<code>' + '</code>' '\n' + '<b>'
                                     '• SEXO: ' '</b>' '<code>' + req['sexo'] + '</code>' '\n' + '<b>'
                                     '• COR: ' '</b>' '<code>' + req['racaCorDescricao'] + '</code>' '\n\n' + '<b>'

                                     '• 👨‍👩‍👦 FILIAÇÃO: ' '</b>' '<code>' + '</code>' '\n' + '<b>' 
                                     '• MÃE: ' '</b>' '<code>' + req['nomeMae'] + '</code>' '\n' + '<b>'
                                     '• PAI: ' '</b>' '<code>' + req['nomePai'] + '</code>' '\n\n' + '<b>'

                                     '• 🏠 MEIOS DE CONTATO: ' '</b>' '<code>' + '</code>' '\n' + '<b>'
                                     '• CIDADE: ' '</b>' '<code>' + req['enderecoMunicipio'] + '</code>' '\n' + '<b>'
                                     '• RUA: ' '</b>' '<code>' + req['enderecoLogradouro'] + '</code>' '\n' + '<b>'
                                     '• BAIRRO: ' '</b>' '<code>' + req['enderecoBairro'] + '</code>' '\n' + '<b>'
                                     '• CEP: ' '</b>' '<code>' + req['enderecoCep'] + '</code>' '\n' + '<b>'
                                     '• NUMERO: ' '</b>' '<code>' + req['enderecoNumero'] + '</code>' '\n\n' + '<b>'
                                     ' • DONO BOT: @isTony_Montana  ' + '</b>', parse_mode='HTML')
                    except:
                        bot.reply_to(men, '<b>CPF NÃO ENCONTRADO</b>', parse_mode='HTML')

###############################################
###############################################
             #Consulta Nome
###############################################
###############################################

@bot.message_handler(commands=['nome'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + EXCEPT
            if id1 in ltnome:

                bot.reply_to(nome, '<code>CONSULTANDO...</code>', parse_mode='HTML')
                msg = nome.text
                fl = msg.split('/nome')
                ip = re.sub('[^0-9]', '', msg)
                
                msg2 = msg.replace("/nome ","")

                try:
                    url = requests.get(f'http://hardzera.ml/api/nome.php?token=FS38XUJ1XBIDY3W9_POZE&nome={msg2}').json()

                    if url['status'] != "200":
                        bot.reply_to(nome, "NOME NAO ENCONTRADO")
                        return

                    text = "🔎 CONSULTA DE NOME 🔎\n"

                    for v in url['pessoas']:
                        text += (f"▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱")
                        text += (f"\n•📄NOME: {v['nome']}")
                        text += (f"\n•📂CPF: {v['cpf']}")
                        text += (f"\n•👫SEXO: {v['sexo']}")
                        text += (f"\n•📅NASCIMENTO: {v['nascimento']}\n")
                        text += (f"▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱")

                    bot.reply_to(nome, text)
                except Exception:
                    bot.reply_to(nome, "NOME NAO ENCONTRADO")

###############################################
###############################################
        #Consulta CPF Receita Federal
###############################################
###############################################

@bot.message_handler(commands=['cpf_receita', 'CPF_RECEITA'])
def CPF_RECEITA(men):
            liberadocpfreceita = PRIVADO + GRUPO + EXCEPT
            bid = men.chat.id
            if bid in liberadocpfreceita:
                mensagem = men.text
                if men.text == '/cpf_receita':
                    bot.reply_to(men, '<b>' 'DIGITE UM CPF !!!' '</b>', parse_mode='HTML')
                elif men.text == '/CPF_RECEITA':
                    bot.reply_to(men, '<b>' 'DIGITE UM CPF !!!' '</b>', parse_mode='HTML')
                else:
                    try:
                        cpfreceita = re.sub('[^0-9.]', '', mensagem)
                        url = requests.get('https://api.i-find.dev/?token=110558cd-281a-4244-aabc-228a24a8c0f3&receitaCpf={}'.format(cpfreceita))
                        req = json.loads(url.text)
                        bot.reply_to(men,'<b>' 
                                     'ㅤ🔍 CONSULTA CPF RECEITA 🔎' '</b>' + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + '<b>'
                                     '• 📄 DOCUMENTOS: ' '</b>' '<code>' + '</code>' '\n' + '<b>'  
                                     '• NOME: ' '</b>' '<code>' + req['pessoa']['nome'] + '</code>' '\n' + '<b>' 
                                     '• DATA DE NASCIMENTO: ' '</b>' '<code>' + req['dataNascimento'] + '</code>' '\n' + '<b>' 
                                     '• SEXO: ' '</b>' '<code>' + req['sexo'] + '</code>' '\n' + '<b>' 
                                     '• NOME DA MÃE: ' '</b>' '<code>' + req['nomeMae'] + '</code>' '\n\n' + '<b>' 

                                     '• 🏠 ENDEREÇO: ' '</b>' '<code>' + '</code>' '\n' + '<b>' 
                                     '• ESTADO: ' '</b>' '<code>' + req['pessoa']['siglaUf'] + '</code>' '\n' + '<b>' 
                                     '• CIDADE: ' '</b>' '<code>' + req['pessoa']['nomeMunicipio'] + '</code>' '\n' + '<b>' 
                                     '• BAIRRO: ' '</b>' '<code>' + req['pessoa']['nomeBairro'] + '</code>' '\n' + '<b>' 
                                     '• RUA: ' '</b>' '<code>' + req['pessoa']['nomeLogradouro'] + '</code>' '\n' + '<b>' 
                                     '• CEP: ' '</b>' '<code>' + req['pessoa']['numeroCep'] + '</code>' '\n' + '<b>'
                                     '• NUMERO: ' '</b>' '<code>' + req['pessoa']['numeroLogradouro'] + '</code>' '\n' + '<b>'
                                     '• COMPLEMENTO: ' '</b>' '<code>' + req['pessoa']['descricaoComplemento'] + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + '<b>'

                                     '• DONO BOT: @isTony_Montana ' + '</b>', parse_mode='HTML')
                    except:
                        bot.reply_to(men, '<b>CPF NÃO ENCONTRADO</b>', parse_mode='HTML')


#####################################################################

print('BOT ONLINE @isTony_Montana ✅!!!')

bot.polling(none_stop = True)
