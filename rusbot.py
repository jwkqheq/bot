import amino
import random
import os

token1 = os.getenv("TOKEN1")
token2 = os.getenv("TOKEN2")

crra = '224443378'
cgdar = '11143881'
cra = '71893015'
cadm = '93021778'
crrar = '62818812'
cstr = '18823866'

client = amino.Client()
client.login(email=token1, password=token2)
sub_client = amino.SubClient(comId=crra, profile=client.profile)
chat5 = '13406d9c-d221-4581-9bbf-209e50133035' # gdar
chat2 = 'bd096200-18cb-45fc-a40e-63dd3c22019e' # rra
chat3 = '5fdfa6e0-7add-4e49-aca2-51f5028b8191' # ra
chat4 = '65cda157-ca6c-4f75-8d9f-5539262bbdb9' # Главный чат (AdM)
chat6 = '5a182e04-f9eb-405c-9a8b-32e65fdeda30' # Главный чат (РРАР)
chat1 = '5bb3b52c-1e1e-45ee-9361-ab8df83b6993' # Флуд чат (Strategion)
lis = ['Думаю да','Думаю нет', 'Конечно же.', 'Нет, ты что?', '50/50', 'С этим вопросом лучше обратитесь к Гуглу.', 'К вам спешит дурка!', 'ор', 'помоги сделать заказ в яндекс еде пжпж', 'Удали', 'Забанен, чекай.', ]
listt = ['0', '1', '2', '3', '5', '8', '11', '13', '15', '17', '18', '21', '24', '25', '27', '31', '35', '41', '47', '54', '61', '65', '72', '78', '82', '85', '88', '91', '99', '100']
listtt = ['AK47', 'AWP', 'GLOCK18', 'Desert Eagle', 'пальчика', 'FAMAS', 'GALIL', 'Dual Barrettas', 'Байдена', 'Германии', 'Путина', 'Ковида19', 'Луны', 'GLOCK17', 'M4A1-S', 'Джаста', 'TEC9']
print("успешно вошел в аккаунт")

bl1 = '42356022-cefa-4ef9-9da0-904a4dcd5ab0' # геймстровая бошка (флуд даже через пред)
bl2 = 'a5e817b3-2f72-4062-9c91-fc7c3b564675' # неон (флуд)
bl3 = '75fa5344-367b-4d96-aa76-9a1a447beb96' # светлана (провокации)
bl4 = '8a5bdbbe-9f39-4b4a-a407-78da465a6bb0' # скаер
bl5 = '67bc5e58-6da1-4425-a303-2923aaa4c8d0' # cvetlanna 2
bl6 = '9d33d501-580c-4d98-8e4f-e36e660acd29' # svetlanna 3
bl7 = 's'                                    #
bl8 = 's'                                    #
bl9 = 's'                                    #
bl10 = 's'                                    #
bl11 = 's'                                    #
bl12 = 's'                                    #
bl13 = 's'                                    #

wl11 = 'b5fc41cd-aade-43ab-bf5d-33c46404f68f'
wl12 = '713d32e0-af17-47e1-a518-0092f6dc0690'
wl13 = '3327b018-8cb6-436f-b3b5-5967f04f051d'
wl14 = 'edcbf03f-7953-4d24-8525-8b4a00f4fb33'
wl15 = 'f5b2c278-2bc8-4a65-b4c4-604989275504'
wl16 = '3216ac0a-8db5-4499-9dd0-43f41de11618'
split = 'dd46a9fa-ea4b-486a-b9d6-b37343366de6'



# slamezzz = b5fc41cd-aade-43ab-bf5d-33c46404f68fб
# slmzbot = 713d32e0-af17-47e1-a518-0092f6dc0690
# tenzen = ae6a373c-c809-44fd-a56b-403c954094a1
# mamba = 3327b018-8cb6-436f-b3b5-5967f04
# just - f5b2c278-2bc8-4a65-b4c4-f051d
# vadim = edcbf03f-7953-4d24-8525-8b4a00f4fb33604989275504
# kermit - 3216ac0a-8db5-4499-9dd0-43f41de11618
# henryriver - 2ff0c6b4-5b75-4cf7-bbc7-fac999e60c03


# 0bfd4ee-2f6b-4f7e-9162-ebea711ed990 f657f117-4ebc-4286-beb0-ffcd825b8c67
try:
    sub_client.send_message(message='Бот запущен. Введите ?h для просмотра команд.', chatId=chat2, messageType=10)
except:
    pass

oldMessages = []

while True:

        messageList = sub_client.get_chat_messages(chatId=chat2, size=1)
        #chatInfo = sub_client.get_chat_thread(chatId=chat2)
        for iduch, nickname, content, msgtype, id in zip(messageList.author.userId, messageList.author.nickname, messageList.content, messageList.messageType, messageList.messageId):
            if id in oldMessages: pass
            else:
                print('[',iduch,']', nickname,':',content, str(id))

                content =  str(content).split()
                if content[0][0] == "?": 
                    if content[0][1:].lower() == "h":
                        sub_client.send_message(message='Нужна помощь по боту? Лови:', chatId=chat2, replyTo=id, embedTitle='Функции бота', embedContent='нажмите сюда.', embedLink="https://rostik23347.wixsite.com/slmzzzbot")
                if content[0][0] == "?": 
                    if content[0][1:].lower() == "yt":
                        sub_client.send_message(message='Хочешь посмотреть ютуб? Лови:', chatId=chat2, replyTo=id, embedTitle='Ютуб', embedContent='нажмите сюда.', embedLink="https://www.youtube.com/")
                if content[0][0] == "?": 
                    if content[0][1:].lower() == "phonkradio":
                        sub_client.send_message(message='Любитель Фонка? Лови:', chatId=chat2, replyTo=id, embedTitle='PhonkRadio', embedContent='нажмите сюда.', embedLink="https://www.youtube.com/watch?v=HSyz0JTr82E")
                if content[0][0] == "?": 
                    if content[0][1:].lower() == "jazzradio":
                        sub_client.send_message(message='Любишь Джазз? Лови:', chatId=chat2, replyTo=id, embedTitle='JazzRadio', embedContent='нажмите сюда.', embedLink="https://www.youtube.com/watch?v=Dx5qFachd3A")
                if content[0][0] == "?": 
                    if content[0][1:].lower() == "chillradio":
                        sub_client.send_message(message='Хочешь отдохнуть? Лови:', chatId=chat2, replyTo=id, embedTitle='ChillRadio', embedContent='нажмите сюда.', embedLink="https://www.youtube.com/watch?v=5qap5aO4i9A")
                if content[0][0] == "?": 
                    if content[0][1:].lower() == "peepradio":
                        sub_client.send_message(message='Слушаешь Лил Пипа? Лови:', chatId=chat2, replyTo=id, embedTitle='LilPeepRadio', embedContent='нажмите сюда.', embedLink="https://www.youtube.com/watch?v=FgSZ46yRPss")      
                if content[0][0] == "?": 
                    if content[0][1:].lower() == "ask":
                        if not (iduch == bl1) | (iduch == bl2) | (iduch == bl3) | (iduch == bl4) | (iduch == bl5) | (iduch == bl6) | (iduch == bl6) | (iduch == bl7) | (iduch == bl8) | (iduch == bl9) | (iduch == bl10) | (iduch == bl11) | (iduch == bl2) | (iduch == bl13):
                            sub_client.send_message(message=str(random.choice(lis)), chatId=chat2, replyTo=id)
                        if (iduch == bl1) | (iduch == bl2) | (iduch == bl3) | (iduch == bl4) | (iduch == bl5) | (iduch == bl6) | (iduch == bl6) | (iduch == bl7) | (iduch == bl8) | (iduch == bl9) | (iduch == bl10) | (iduch == bl11) | (iduch == bl2) | (iduch == bl13): 
                            sub_client.send_message(message='[c] Вы находитесь в блек-листе данной команды и не имеете возможности её использовать.᠌', chatId=chat2, replyTo=id)
                if content[0][0] == "?": 
                    if content[0][1:].lower() == "getmyid":
                        sub_client.send_message(message=str(iduch), chatId=chat2, replyTo=id)
                if content[0][0] == "?": 
                    if content[0][1:].lower() == "slap":
                        if (iduch == bl1) | (iduch == bl2) | (iduch == bl3) | (iduch == bl4) | (iduch == bl5) | (iduch == bl6) | (iduch == bl6) | (iduch == bl7) | (iduch == bl8) | (iduch == bl9) | (iduch == bl10) | (iduch == bl11) | (iduch == bl2) | (iduch == bl13): 
                            sub_client.send_message(message='[c] Вы находитесь в блек-листе данной команды и не имеете возможности её использовать.᠌', chatId=chat2, replyTo=id)
                        if not (iduch == bl1) | (iduch == bl2) | (iduch == bl3) | (iduch == bl4) | (iduch == bl5) | (iduch == bl6) | (iduch == bl6) | (iduch == bl7) | (iduch == bl8) | (iduch == bl9) | (iduch == bl10) | (iduch == bl11) | (iduch == bl2) | (iduch == bl13):
                            sub_client.send_message(message='Нанесено' + ' ' + str(random.choice(listt)) + ' ' + 'урона. Сильный удар!', chatId=chat2, replyTo=id)
                if content[0][0] == "?":   
                    if content[0][1:].lower() == "heal":
                        sub_client.send_message(message='Добавлено' + ' ' + str(random.choice(listt)) + ' ' + 'здоровья.', chatId=chat2, replyTo=id)
                if content[0][0] == "?":   
                    if content[0][1:].lower() == "sleep":
                        sub_client.send_message(message='Добавлено' + ' ' + str(random.choice(listt)) + ' ' + 'энергии.', chatId=chat2, replyTo=id)                              
                if content[0][0] == "?":
                    if content[0][1:].lower() == "mine":
                        if not (iduch == bl1) | (iduch == bl2) | (iduch == bl3) | (iduch == bl4) | (iduch == bl5) | (iduch == bl6) | (iduch == bl6) | (iduch == bl7) | (iduch == bl8) | (iduch == bl9) | (iduch == bl10) | (iduch == bl11) | (iduch == bl2) | (iduch == bl13):
                            sub_client.send_message(message='Получено' + ' ' + str(random.choice(listt)) + ' ' + 'ресурсов,' + ' ' + 'потрачено' + ' ' + str(random.choice(listt)) + ' ' + 'энергии.', chatId=chat2, replyTo=id)
                        if (iduch == bl1) | (iduch == bl2) | (iduch == bl3) | (iduch == bl4) | (iduch == bl5) | (iduch == bl6) | (iduch == bl6) | (iduch == bl7) | (iduch == bl8) | (iduch == bl9) | (iduch == bl10) | (iduch == bl11) | (iduch == bl2) | (iduch == bl13): 
                            sub_client.send_message(message='[c] Вы находитесь в блек-листе данной команды и не имеете возможности её использовать.᠌', chatId=chat2, replyTo=id)        
                if content[0][0] == "?":
                    if content[0][1:].lower() == "pick":
                        if not (iduch == bl1) | (iduch == bl2) | (iduch == bl3) | (iduch == bl4) | (iduch == bl5) | (iduch == bl6) | (iduch == bl6) | (iduch == bl7) | (iduch == bl8) | (iduch == bl9) | (iduch == bl10) | (iduch == bl11) | (iduch == bl2) | (iduch == bl13):
                            sub_client.send_message(message='Подобрано.', chatId=chat2, replyTo=id) 
                        if (iduch == bl1) | (iduch == bl2) | (iduch == bl3) | (iduch == bl4) | (iduch == bl5) | (iduch == bl6) | (iduch == bl6) | (iduch == bl7) | (iduch == bl8) | (iduch == bl9) | (iduch == bl10) | (iduch == bl11) | (iduch == bl2) | (iduch == bl13): 
                            sub_client.send_message(message='[c] Вы находитесь в блек-листе данной команды и не имеете возможности её использовать.᠌', chatId=chat2, replyTo=id)               
                if content[0][0] == "?": 
                    if content[0][1:].lower() == "shoot":
                        sub_client.send_message(message='Выстрелил с' + ' ' + str(random.choice(listtt)) + '.', chatId=chat2, replyTo=id)                     
                if content[0][0] == "?":
                    if content[0][1:].lower() == "sell":
                        if not (iduch == bl1) | (iduch == bl2) | (iduch == bl3) | (iduch == bl4) | (iduch == bl5) | (iduch == bl6) | (iduch == bl6) | (iduch == bl7) | (iduch == bl8) | (iduch == bl9) | (iduch == bl10) | (iduch == bl11) | (iduch == bl2) | (iduch == bl13):
                            sub_client.send_message(message='Продано' + ' ' + str(random.choice(listt)) + ' ' + 'ресурсов,' + ' ' + 'получено' + ' ' + str(random.choice(listt)) + ' ' + 'валюты.', chatId=chat2, replyTo=id)
                        if (iduch == bl1) | (iduch == bl2) | (iduch == bl3) | (iduch == bl4) | (iduch == bl5) | (iduch == bl6) | (iduch == bl6) | (iduch == bl7) | (iduch == bl8) | (iduch == bl9) | (iduch == bl10) | (iduch == bl11) | (iduch == bl2) | (iduch == bl13):
                            sub_client.send_message(message='[c] Вы находитесь в блек-листе данной команды и не имеете возможности её использовать.᠌', chatId=chat2, replyTo=id)      
                if content[0][0] == "?":
                    if content[0][1:].lower() == "q":
                        sub_client.kick(allowRejoin=1, chatId=chat2, userId=iduch)
                        sub_client.send_message(message='Пользователь' + ' ' + nickname + ' ' + 'вышел с чата.', chatId=chat2,)      
                if content[0][0] == "?":
                    if content[0][1:].lower() == "самобан":
                        try:
                            sub_client.ban(userId=iduch, reason='Ввод команды ?самобан', banType=200)
                            sub_client.send_message(message='Пользователь' + ' ' + nickname + ' ' + 'был забанен по собственному желанию.', chatId=chat2,)
                        except:
                            sub_client.send_message(message='умный самый?', chatId=chat2, replyTo=id)       
                if content[0][0] == "?":
                    if content[0][1:].lower() == "sb":
                        try:
                            sub_client.ban(userId=iduch, reason='Ввод команды ?самобан', banType=200)
                            sub_client.send_message(message='Пользователь' + ' ' + nickname + ' ' + 'был забанен по собственному желанию.', chatId=chat2,)
                        except:
                            sub_client.send_message(message='умный самый?', chatId=chat2, replyTo=id)     
                if content[0][0] == "?":
                    if content[0][1:].lower() == "ban":
                        if (iduch == wl11) | (iduch == wl12) | (iduch == wl13) | (iduch == wl14) | (iduch == wl15) | (iduch == wl16):
                            try:
                                idmb = client.get_from_code(content[-2]).objectId
                                rs = content[-1] + ' | ' + iduch
                                sub_client.ban(userId=idmb, reason=rs, banType=200)
                                sub_client.send_message(message='Нарушитель был забанен администратором' + ' ' + nickname + '.', chatId=chat2)
                            except:
                                sub_client.send_message(message='Неправильно введён запрос. Попробуйте так: ?ban (ссылка) (причина)', chatId=chat2)
                if content[0][0] == "?":
                    if content[0][1:].lower() == "permkick":
                        if (iduch == wl11) | (iduch == wl12) | (iduch == wl13) | (iduch == wl14) | (iduch == wl15) | (iduch == wl16):
                            try:
                                idmb = client.get_from_code(content[-1]).objectId
                                sub_client.kick(userId=idmb, chatId=chat2, allowRejoin=0)
                                sub_client.send_message(message='Администратор' + ' ' + nickname + ' ' +  'навсегда исключил из чата нарушителя.', chatId=chat2)
                            except:
                                sub_client.send_message(message='Неправильно введён запрос. Попробуйте так: ?permkick (ссылка)', chatId=chat2)        
                if content[0][0] == "?":
                    if content[0][1:].lower() == "kick":
                        if (iduch == wl11) | (iduch == wl12) | (iduch == wl13) | (iduch == wl14) | (iduch == wl15) | (iduch == wl16):
                                try:
                                    idmb = client.get_from_code(content[-1]).objectId
                                    sub_client.kick(userId=idmb, chatId=chat2, allowRejoin=1)
                                    sub_client.send_message(message='Администратор' + ' ' + nickname + ' ' +  'исключил из чата нарушителя.', chatId=chat2)
                                except:
                                    sub_client.send_message(message='Неправильно введён запрос. Попробуйте так: ?kick (ссылка)', chatId=chat2)            
                if content[0][0] == "?":
                    if content[0][1:].lower() == "звание":
                        try:
                            zvanie =[content[-2]]
                            clrs = [content[-1]]
                            sub_client.edit_titles(userId=iduch, titles=zvanie, colors=clrs)
                            sub_client.send_message(message='Звание выдано.', chatId=chat2) 
                        except:
                            sub_client.send_message(message='Неправильно введён запрос. Попробуйте так: ?звание (звание) (цвет)', chatId=chat2)
                        if (iduch == bl1) | (iduch == bl2) | (iduch == bl3) | (iduch == bl4) | (iduch == bl5) | (iduch == bl6) | (iduch == bl6) | (iduch == bl7) | (iduch == bl8) | (iduch == bl9) | (iduch == bl10) | (iduch == bl11) | (iduch == bl2) | (iduch == bl13): 
                            sub_client.send_message(message='[c] Вы находитесь в блек-листе данной команды и не имеете возможности её использовать.᠌', chatId=chat2, replyTo=id)
                if content[0][0] == "?":
                    if content[0][1:].lower() == "рч":
                        if (iduch == wl11) | (iduch == wl12) | (iduch == wl13) | (iduch == wl14) | (iduch == wl15) | (iduch == wl16):
                            try:
                                idmb = client.get_from_code(content[-2]).objectId
                                rs = content[-1] + ' | ' + iduch
                                sub_client.strike(userId=idmb, reason=rs, time=4)
                                sub_client.send_message(message='Администратор' + ' ' + nickname + ' ' + 'выдал режим чтения нарушителю.', chatId=chat2)
                            except:
                                sub_client.send_message(message='Неправильно введён запрос. Попробуйте так: ?рч (ссылка) (причина)', chatId=chat2)          
                if content[0][0] == "?":
                    if content[0][1:].lower() == "unban":
                        if (iduch == wl11) | (iduch == wl12) | (iduch == wl13) | (iduch == wl14) | (iduch == wl15) | (iduch == wl16):
                            try:
                                idmb = client.get_from_code(content[-1]).objectId
                                sub_client.unban(userId=idmb, reason='Разбанен администратором - ' + iduch)
                                sub_client.send_message(message='Администратор' + ' ' + nickname + ' ' + 'убрал блокировку аккаунта нарушителя.', chatId=chat2)
                            except:
                                sub_client.send_message(message='Неправильно введён запрос. Попробуйте так: ?unban (ссылка)', chatId=chat2)            
                if content[0][0] == "?":
                    if content[0][1:].lower() == "hidepost":
                        if (iduch == wl11) | (iduch == wl12) | (iduch == wl13) | (iduch == wl14) | (iduch == wl15) | (iduch == wl16):
                            idmb = client.get_from_code(content[-2]).objectId
                            rs = content[-1] + ' | ' + iduch
                            sub_client.hide(blogId=idmb, reason=rs)
                            sub_client.send_message(message='Администратор' + ' ' + nickname + ' ' + 'скрыл пост.', chatId=chat2)            
                if content[0][0] == "?":
                    if content[0][1:].lower() == "unhidepost":
                        if (iduch == wl11) | (iduch == wl12) | (iduch == wl13) | (iduch == wl14) | (iduch == wl15) | (iduch == wl16):
                            idmb = client.get_from_code(content[-2]).objectId
                            rs = content[-1] + ' | ' + iduch
                            sub_client.unhide(blogId=idmb, reason=rs)
                            sub_client.send_message(message='Администратор' + ' ' + nickname + ' ' + 'открыл пост для просмотра.', chatId=chat2)            
                if content[0][0] == "?":
                    if content[0][1:].lower() == "hideprofile":
                        if (iduch == wl11) | (iduch == wl12) | (iduch == wl13) | (iduch == wl14) | (iduch == wl15) | (iduch == wl16):
                            idmb = client.get_from_code(content[-2]).objectId
                            rs = content[-1] + ' | ' + iduch
                            sub_client.hide(userId=idmb, reason=rs)
                            sub_client.send_message(message='Администратор' + ' ' + nickname + ' ' + 'скрыл для просмотра профиль.', chatId=chat2)            
                if content[0][0] == "?":
                    if content[0][1:].lower() == "unhideprofile":
                        if (iduch == wl11) | (iduch == wl12) | (iduch == wl13) | (iduch == wl14) | (iduch == wl15) | (iduch == wl16):
                            idmb = client.get_from_code(content[-2]).objectId
                            rs = content[-1] + ' | ' + iduch
                            sub_client.unhide(userId=idmb, reason=rs)
                            sub_client.send_message(message='Администратор' + ' ' + nickname + ' ' + 'открыл для просмотра профиль.', chatId=chat2)            
                if content[0][0] == "?":
                    if content[0][1:].lower() == "warn":
                        if (iduch== wl11) | (iduch == wl12) | (iduch == wl13) | (iduch == wl14) | (iduch == wl15) | (iduch == wl16):
                            idmb = client.get_from_code(content[-2]).objectId
                            rs = content[-1] + ' | ' + iduch
                            sub_client.warn(userId=idmb, reason=rs)
                            sub_client.send_message(message='Администратор' + ' ' + nickname + ' ' + 'выдал предупреждение нарушителю.', chatId=chat2)            
                if content[0][0] == "m":
                    if content[0][1:].lower() == "q":
                        sub_client.kick(userId=iduch, chatId=chat2, allowRejoin=1)
                        sub_client.send_message(message='братан ьыче', chatId=chat2, replyTo=id)            
                if content[0][0] == "?":
                    if content[0][1:].lower() == "whitelist":
                        sub_client.send_message(message='Список пользователей в Вайтлисте: slamezzz(2lvl), вадим(1lvl), yaicawave(1lvl), Kermit(1lvl), джаст(1lvl), Евгений Малышкин(1lvl)', chatId=chat2, replyTo=id)        
                if content[0][0] == "?":
                    if content[0][1:].lower() == "getid":
                        try:
                            idmb = client.get_from_code(content[-1]).objectId
                            sub_client.send_message(message=idmb, chatId=chat2, replyTo=id)   
                        except:
                            sub_client.send_message(message='Произошла ошибка! (Кода или ссылки не существует)', chatId=chat2, replyTo=id)
                if content[0][0] == "?":
                    if content[0][1:].lower() == "unbanid":
                        if (iduch == wl11) | (iduch == wl12) | (iduch == wl13) | (iduch == wl14) | (iduch == wl15) | (iduch == wl16):
                            try:
                                sub_client.unban(userId=content[-1], reason='Разбанен администратором - ' + iduch)
                                sub_client.send_message(message='Администратор' + ' ' + nickname + ' ' + 'убрал блокировку аккаунта нарушителя.', chatId=chat2)
                            except:
                                sub_client.send_message(message='Неправильно введён запрос. Попробуйте так: ?unbanid (юзерайди)', chatId=chat2)
                if content[0][0] == "?":
                    if content[0][1:].lower() == "banid":
                        if (iduch == wl11) | (iduch == wl12) | (iduch == wl13) | (iduch == wl14) | (iduch == wl15) | (iduch == wl16):
                            try:
                                rs = content[-1] + ' | ' + iduch
                                sub_client.ban(userId=content[-2], reason=rs, banType=200)
                                sub_client.send_message(message='Нарушитель был забанен администратором' + ' ' + nickname + '.', chatId=chat2)
                            except:
                                sub_client.send_message(message='Неправильно введён запрос. Попробуйте так: ?banid (юзерайди) (причина)', chatId=chat2)
                if content[0][0] == "?":
                    if content[0][1:].lower() == "ghost":
                        if (iduch == wl11) | (iduch == wl12) | (iduch == wl13) | (iduch == wl14) | (iduch == wl15) | (iduch == wl16):
                            try:
                                sub_client.send_message(message=' ᠌' + content[-1], chatId=chat2, messageType=109)
                            except:
                                print(iduch + ' отправил мт109')
                        if (iduch == bl1) | (iduch == bl2) | (iduch == bl3) | (iduch == bl4) | (iduch == bl5) | (iduch == bl6) | (iduch == bl6) | (iduch == bl7) | (iduch == bl8) | (iduch == bl9) | (iduch == bl10) | (iduch == bl11) | (iduch == bl2) | (iduch == bl13): 
                            sub_client.send_message(message='[c] Вы находитесь в блек-листе данной команды и не имеете возможности её использовать.᠌', chatId=chat2, replyTo=id)
                if content[0][0] == "а":
                    if content[0][1:].lower() == "уе":
                        try:
                            sub_client.send_message(message='Добрый день, ' + nickname + '. Введя эту команду, вы дали разрешение на ваш бан. Удачи!', chatId=chat2, replyTo=id)
                            sub_client.send_message(message='Запускаю бан-машину...', chatId=chat2, replyTo=id)
                            sub_client.ban(userId=iduch, reason='Ввод команды.', banType=200)
                            sub_client.send_message(message='Успешно забанен!', chatId=chat2, replyTo=id)
                            sub_client.send_message(message='Ладно это пранк КАКАШКОЙ pososee', chatId=chat2, replyTo=id)
                            sub_client.unban(userId=iduch, reason='Ввод команды.')
                            sub_client.send_message(message="я тебя разбанил не плачь", chatId=chat2, replyTo=id)
                        except:
                            sub_client.send_message(message=nickname + ', ты че умный самый?', chatId=chat2, replyTo=id)
                if content[0][0] == "a":
                    if content[0][1:].lower() == "ye":
                        try:
                            sub_client.send_message(message="[bc]" + nickname + ' ' + 'был замечен за попыткой обхода системы!\n[c] Произвожу бан...', chatId=chat2, replyTo=id)
                            sub_client.ban(userId=iduch, reason='Ввод команды.', banType=200)
                        except:
                            sub_client.send_message(message="[b] Ошибка!", chatId=chat2, replyTo=id)            
                if content[0][0] == "a":
                    if content[0][1:].lower() == "уе":
                        try:
                            sub_client.send_message(message="[bc]" + nickname + ' ' + 'был замечен за попыткой обхода системы!\n[c] Произвожу бан...', chatId=chat2, replyTo=id)
                            sub_client.ban(userId=iduch, reason='Ввод команды.', banType=200)
                        except:
                            sub_client.send_message(message="[b] Ошибка!", chatId=chat2, replyTo=id)
                if content[0][0] == "?":
                    if content[0][1:].lower() == "stop":
                        if (iduch== wl11) | (iduch == wl12) | (iduch == wl13) | (iduch == wl14) | (iduch == wl15) | (iduch == wl16):
                            print('-')
                            print('-')
                            sub_client.send_message(message="Бот отключён!\nОтключён администратором:" + ' ' + nickname + '\n' + iduch, chatId=chat2, messageType=109)
                if content[0][0] == "?":
                    if content[0][1:].lower() == "card":
                        if (iduch == wl11) | (iduch == wl12) | (iduch == wl13) | (iduch == wl14) | (iduch == wl15) | (iduch == wl16):
                            try:
                                message = content[-3]
                                embedtitle = content[-2]
                                embedcontent = content[-1]
                                sub_client.send_message(message=message, embedTitle=embedtitle, embedContent=embedcontent, chatId=chat2)
                            except:
                                sub_client.send_message(message="Произошла ошибка! [неправильно введён запрос]", chatId=chat2, replyTo=id)
                if content[0][0] == "?": 
                    if content[0][1:].lower() == "chance":
                        if (iduch == bl1) | (iduch == bl2) | (iduch == bl3) | (iduch == bl4) | (iduch == bl5) | (iduch == bl6) | (iduch == bl6) | (iduch == bl7) | (iduch == bl8) | (iduch == bl9) | (iduch == bl10) | (iduch == bl11) | (iduch == bl2) | (iduch == bl13): 
                            sub_client.send_message(message='[c] Вы находитесь в блек-листе данной команды и не имеете возможности её использовать.᠌', chatId=chat2, replyTo=id)
                        if not (iduch == bl1) | (iduch == bl2) | (iduch == bl3) | (iduch == bl4) | (iduch == bl5) | (iduch == bl6) | (iduch == bl6) | (iduch == bl7) | (iduch == bl8) | (iduch == bl9) | (iduch == bl10) | (iduch == bl11) | (iduch == bl2) | (iduch == bl13):
                            sub_client.send_message(message='Шанс:' + ' ' + str(random.choice(listt)) + '%.', chatId=chat2, replyTo=id)                
                if content[0][0] == "?":   
                    if content[0][1:].lower() == "check":
                        try:
                            sub_client.send_message(message='Бот работает исправно!', chatId=chat2, messageType=109)
                        except:
                            pass           
                        oldMessages.append(id)
                        

