import k_amino as amino, time, concurrent.futures, pyfiglet, colorama,random

client = amino.Client()
email = "enviousMacaw41cea@gmail.com"  # Correo de cuenta
password = "LsuaaIsGay1234%"  # Contraseña de la cuenta
nicknames = ["🍯⠀̥ ᜒ𝀛  𝑮𔘓᜔𔘓ᜒd ̷̸ 𝑮͟ɩr͟l ᪶  ᜓ˙𝀛",
             "𔘓 ܸ   ໍ ⠀⠀𝑪ᥙtə ♰̷̸ 𝑮ɩrl  𓂃   𔓕  ໍ ͙˙",
             "  ֪  ࣪  𝐏ᦅ̶͟ᦅ͟pə࣪r  ⌗ ۫ ܸ"]  # Apodos del perfil
msg = "[C]𝗗⃪࣮𝗔̷̸𝗟𝚺̸  𝗖͠𝗟𝗜𝗖͠𝗞  𝗔̷̸  𝗟𝗔̷̸  𝗙̸̷ۣۜ𝝝𝗧⵿ۜ𝝝🔥"  # Mensaje del spam jiji
link = "https://aminoapps.com/invite/U5LVEV42VI"  # Link de la comunidad
archi = "hola1.png"  # Nombre de la imagen, debe de ser .png
title = "UNETE PERRA🔥"  # Título del chat
anuncio = "❤⃝➵「¿QUIERES 𝐂𝐔𝐌PLIR TUS FANTASIAS?」❤️  ˹𝐄ntra˼ 𝐀mor, ☆⇉ 𝐓e 𝐀seguro 𝐐ue 𝐋o 𝐃isfrutaras...͢ ͜🎫=͡💞 [🔥ENTRA🔥|https://aminoapps.com/invite/U5LVEV42VI]]"  # Anuncio fijado

selected_nickname = random.choice(nicknames)
client.login(email=email, password=password)
client.edit_profile(selected_nickname)

n_comus = 30


def eu():
    global chat
    ch = client.get_chat_threads(0, 30)
    for x, title in enumerate(ch.title, 1):
        print(f" - {x}.{title}")
    chat = ch.chatId[int(input(" - Selecciona el chat: ")) - 1]
    print(chat)


def pre():
    try:
        client.edit_chat(chatId=chat, title=title, announcement=anuncio)
    except Exception as e:
        print(e)
        client.edit_chat(chatId=chat, title=title, announcement=anuncio)
    global imagen
    imagen = open(archi, "rb")
    try:
        client.send_message(chatId=chat, snippetImage=imagen, message=msg, snippetLink=link)
    except Exception as e:
        print(e)
        client.send_message(chatId=chat, snippetImage=imagen, message=msg, snippetLink=link)


num = 300
num1 = 0

lista = []


def colec_Co():
    global n_comus
    com = client.get_my_communities(0, n_comus).comId
    for comId in com:
        sub = amino.SubClient(comId=comId, client=client)
        for x in range(0, 500, 100):
            try:
                lista.extend(sub.get_all_users("recent", x, x + 100).userId)
            except:
                continue
        time.sleep(45)
        print(" - Se han sacado los usuarios de ", comId)


def recolec():
    global num
    global num1
    global lista
    if num <= 1200:
        num -= 900
        num1 -= 900
    else:
        pass
    for x in range(num1, num, 100):
        try:
            time.sleep(5)
            lista.extend(client.get_all_users("online", x, +100).userId)
        except Exception as e:
            print(e)
            continue
        num += 300
        num1 += 300
    sab = len(lista)
    if sab <= 100:
        for x in range(num1, num, 100):
            try:
                time.sleep(15)
                lista.extend(client.get_all_users("recent", x, x + 100).userId)
            except Exception as e:
                print(e)
                continue
    else:
        print(" - Continue")
    print(f" - Se cargaron {sab}")
    time.sleep(3)


def reen():
    img = open(archi, "rb")
    try:
        client.send_message(chatId=chat, snippetImage=img, message=msg, snippetLink=link)
    except Exception as e:
        pass


def main():
    a = 500
    i = 0
    counter = 0
    with concurrent.futures.ThreadPoolExecutor(10000) as executor:
        for userId in lista:
            if i <= a:
                try:
                    executor.submit(client.invite_to_chat, chat, userId)
                    time.sleep(0.2)
                    counter += 1
                    i += 1
                except Exception as e:
                    print(e)
                    time.sleep(1)
                    continue
            elif i > a:
                time.sleep(1150)
                a += 300
                time.sleep(15)
                reen()

            if counter == 300:
                print("lista terminada")
                counter = 0
                i = 0
                break
        lista.clear()


print(colorama.Fore.LIGHTCYAN_EX)
print("SPAM LOCO GLOBAL__TAKUMIᯥ")
print("1-Escribe el numero 1, para empezar. jiji")
el = int(input("\n - Selecciona la opcion: "))


def inc():
    while True:
        recolec()
        time.sleep(5)
        main()
        time.sleep(5)
        try:
            reen()
        except:
            pass


if el == 1:
    eu()
    reen()
    inc()
