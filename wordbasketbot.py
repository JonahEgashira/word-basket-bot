# インストールした discord.py を読み込む
import discord
import random
import copy

from serviceKey import serviceKey
from format import format_word

TOKEN = serviceKey["TOKEN"]
client = discord.Client()

GeneralId = serviceKey["GeneralId"]
RandomId = serviceKey["RandomId"]


@client.event
async def on_ready():
    channel = client.get_channel(RandomId)
    await channel.send('レムレム？')
    await channel.send('遊び方がわからないときは .help と送信してね')
    print('ログインしました')

dakuon = [
    'が',
    'ぎ',
    'ぐ',
    'げ',
    'ご',
    'ざ',
    'じ',
    'ず',
    'ぜ',
    'ぞ',
    'だ',
    'ぢ',
    'づ',
    'で',
    'ど',
    'ば',
    'び',
    'ぶ',
    'べ',
    'ぼ',
    'ぱ',
    'ぴ',
    'ぷ',
    'ぺ',
    'ぽ',
]

hiragana = [
    'あ',
    'い',
    'う',
    'え',
    'お',
    'か',
    'き',
    'く',
    'け',
    'こ',
    'が',
    'ぎ',
    'ぐ',
    'げ',
    'ご',
    'さ',
    'し',
    'す',
    'せ',
    'そ',
    'ざ',
    'じ',
    'ず',
    'ぜ',
    'ぞ',
    'た',
    'ち',
    'つ',
    'て',
    'と',
    'だ',
    'ぢ',
    'づ',
    'で',
    'ど',
    'な',
    'に',
    'ぬ',
    'ね',
    'の',
    'は',
    'ひ',
    'ふ',
    'へ',
    'ほ',
    'ば',
    'び',
    'ぶ',
    'べ',
    'ぼ',
    'ぱ',
    'ぴ',
    'ぷ',
    'ぺ',
    'ぽ',
    'ま',
    'み',
    'む',
    'め',
    'も',
    'や',
    'ゆ',
    'よ',
    'ら',
    'り',
    'る',
    'れ',
    'ろ',
    'わ',
]

word_list_original = [
    'あ',
    'い',
    'う',
    'え',
    'お',
    'か',
    'き',
    'く',
    'け',
    'こ',
    'さ',
    'し',
    'す',
    'せ',
    'そ',
    'た',
    'ち',
    'つ',
    'て',
    'と',
    'な',
    'に',
    'ぬ',
    'ね',
    'の',
    'は',
    'ひ',
    'ふ',
    'へ',
    'ほ',
    'ま',
    'み',
    'む',
    'め',
    'も',
    'や',
    'ゆ',
    'よ',
    'ら',
    'り',
    'る',
    'れ',
    'ろ',
    'わ',
    '5', '5', '5', '5', '5',
    '6', '6', '6', '6', '6',
    '7+', '7+', '7+', '7+', '7+',
]

word_list = []
user_list = []
user_id_list = {}
user_hands = []
user_num = 0
is_game_started = False
current_char = ""


def init():
    global user_num
    global user_id_list
    global user_list
    global word_list
    global user_hands
    global is_game_started
    global current_char

    user_num = 0
    user_id = {}
    user_hands = []
    user_list = []
    word_list = []
    is_game_started = False
    current_char = ""

# ラムが返信


async def reply(message):
    reply = f'{message.author.mention} 話しかけないでくれる？'  # 返信メッセージの作成
    await message.channel.send(reply)  # 返信メッセージを送信


def is_not_number(word):
    if word == '5' or word == '6' or word == '7+':
        return False
    else:
        return True


help = '''ルール: 次の文字で表示された文字で始まり、自分の手札の文字で終わる3文字以上の言葉を送信しましょう。
 一番早く送信すると手札が消費され、手札がなくなると勝利です。
 5や7+などの数字の手札は、次の文字で始まって、5,6であればちょうど5,6文字、7+は7文字以上の言葉を送信してください。
 この時に終わりの文字はなんでも構いません(「ん」以外）。
 
 コマンド一覧
 .start @ユーザー名1 @ユーザー名2 @ユーザー名3 で、指定されたユーザーでゲームを始めます
 .reset でゲームをリセットします
 .show で現在場に出ている文字を表示します
 .draw または 「ひく」でカードを一枚引きます'''

# メッセージ受信時に動作する処理


@client.event
async def on_message(message):
    global user_num
    global user_id_list
    global user_list
    global word_list
    global user_hands
    global is_game_started
    global current_char

    if message.content == '.8':
        await message.channel.send("8888888888888")
        return

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # ゲームプレイ中にエスケープしたい場合
    if message.content.startswith('/'):
        return

    # ゲームのリセット
    if message.content == '.reset':
        await message.channel.send("やり直すわ")
        init()
        return

    if message.content == '.help':
        await message.channel.send(help)

    # ゲームが進行中だと、自分の手札を教えてくれる
    if client.user in message.mentions or message.content == 'ラム':
        if is_game_started == True:
            idx = user_id_list[message.author.name]
            hand = ' , '.join(user_hands[idx])
            await message.channel.send(f"{message.author.mention}の残り手札は、「{hand}」よ")
            return

        else:
            await reply(message)
            return

    # ゲーム開始
    if message.content.startswith('.start'):
        # 既にゲームが始まっているとき
        if is_game_started == True:
            await message.channel.send("ゲームが始まってるわよ")
            return

        # プレイ人数が足りないとき
        if len(message.mentions) == 0:
            await message.channel.send("プレイ人数が足りないわ")
            return

        # リストからコピー
        word_list = copy.copy(word_list_original)
        is_game_started = True

        # ワードのリストの長さ
        word_num = len(word_list)

        # メンバーの名前とidを辞書に登録する
        for member in message.mentions:
            user_list.append(member.name)
            user_id_list[member.name] = user_num
            user_num += 1

        # ユーザーの手札を二次元配列で管理する
        user_hands = [[] for i in range(user_num)]

        # ランダムでユーザに手札を配る
        hand_num = 5
        for i in range(user_num):
            for j in range(hand_num):
                idx = random.randint(0, len(word_list) - 1)
                user_hands[i].append(word_list.pop(idx))

        # ユーザーの手札を知らせる
        for member in message.mentions:
            user_id = user_id_list[member.name]
            hand = ' , '.join(user_hands[user_id])
            await message.channel.send(f"{member.mention}の手札は、「{hand}」よ")

        # 最初に表示される文字をランダム抽出(数字だった場合はひらがなが出るまでやる)
        while True:
            idx = random.randint(0, len(word_list) - 1)
            if is_not_number(word_list[idx]):
                current_char = (word_list.pop(idx))
                break

        # ゲーム開始時に、いまの文字を表示
        await message.channel.send("ゲームが始まるわ")
        await message.channel.send(f"次のもじは「    {current_char}    」よ")

    # メッセージから得られる情報
    user = message.author.name
    user_id = user_id_list[user]
    word = message.content
    word_len = len(word)
    word_formatted = format_word(word)

    # いまの文字がわからないときに教えてくれる
    if message.content == '.show' and is_game_started == True:
        await message.channel.send(f"次のもじは「    {current_char}    」よ")
        return

    # 自分の手札にあらたな文字を追加する
    if (message.content == '.draw' or message.content == 'ひく') and is_game_started == True:
        if len(word_list) == 0:
            await message.channel.send("山札が空よ")
            return

        idx = random.randint(0, len(word_list) - 1)
        add_word = word_list.pop(idx)
        user_hands[user_id].append(add_word)
        hand = ' , '.join(user_hands[user_id])
        await message.channel.send(f"「{add_word}」を追加したわ\n{message.author.mention}の手札は、「{hand}」よ")
        return

    if is_game_started == True and message.author.name in user_list:

        # スタートの文字列で反応しないようにする
        if message.content.startswith('.start'):
            return

        # 3文字以上の言葉でないとだめ
        if word_len < 3:
            await message.channel.send(f"{message.author.mention}言葉が短すぎるわ")
            return

        # 最後の言葉がひらがなじゃない場合、だめ
        last_char = word_formatted[-1]
        if last_char not in hiragana:
            await message.channel.send(f"{message.author.mention}なによその言葉は")
            return

        # 投げられた言葉から、マッチするものを探す、なかったら「無い」と返す
        length = len(user_hands[user_id])
        del_idx = -1

        # ひらがなマッチ
        for i in range(length):
            if word_formatted[0] == current_char and word_formatted[-1] == user_hands[user_id][i]:
                del_idx = i

        # 数字マッチ（数字マッチを優先して消す)
        for i in range(length):
            if is_not_number(user_hands[user_id][i]):
                continue

            # '7+'のときは別で処理
            word_digit = 0
            if user_hands[user_id][i] != '7+':
                word_digit = int(user_hands[user_id][i])

            if user_hands[user_id][i] == '7+':
                if word_len >= 7:
                    del_idx = i
            elif word_len == word_digit:
                del_idx = i

        # マッチする手札がある
        if del_idx != -1:
            # 対応する文字を消す
            user_hands[user_id].pop(del_idx)

            # 単語のリピート
            await message.channel.send(f"{word}！")

            # もう手札がなかったら勝ち
            if not user_hands[user_id]:
                await message.channel.send(f"{message.author.mention}の勝ちね")
                # 初期化
                init()
                return

            current_char = word_formatted[-1]
            await message.channel.send(f"次のもじは「     {current_char}     」よ")

            # 残りの手札を知らせる
            hand = ' , '.join(user_hands[user_id])
            await message.channel.send(f"{message.author.mention}の残り手札は、「{hand}」よ")

        else:
            await message.channel.send(f"{message.author.mention}出せる手札がないわ、よく考えなさい")


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
