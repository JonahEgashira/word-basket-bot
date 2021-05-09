def format_word(word):
    word = list(word)

    # 最初の文字
    if word[0] == 'が':
        word[0] = 'か'
    if word[0] == 'ぎ':
        word[0] = 'き'
    if word[0] == 'ぐ':
        word[0] = 'く'
    if word[0] == 'げ':
        word[0] = 'け'
    if word[0] == 'ご':
        word[0] = 'こ'
    if word[0] == 'ざ':
        word[0] = 'さ'
    if word[0] == 'じ':
        word[0] = 'し'
    if word[0] == 'ず':
        word[0] = 'す'
    if word[0] == 'ぜ':
        word[0] = 'せ'
    if word[0] == 'ぞ':
        word[0] = 'そ'
    if word[0] == 'だ':
        word[0] = 'た'
    if word[0] == 'ぢ':
        word[0] = 'ち'
    if word[0] == 'づ':
        word[0] = 'つ'
    if word[0] == 'で':
        word[0] = 'て'
    if word[0] == 'ど':
        word[0] = 'と'
    if word[0] == 'ば':
        word[0] = 'は'
    if word[0] == 'び':
        word[0] = 'ひ'
    if word[0] == 'ぶ':
        word[0] = 'ふ'
    if word[0] == 'べ':
        word[0] = 'へ'
    if word[0] == 'ぼ':
        word[0] = 'ほ'
    if word[0] == 'ぱ':
        word[0] = 'は'
    if word[0] == 'ぴ':
        word[0] = 'ひ'
    if word[0] == 'ぷ':
        word[0] = 'ふ'
    if word[0] == 'ぺ':
        word[0] = 'へ'
    if word[0] == 'ぽ':
        word[0] = 'ほ'

    # 最後の文字
    if word[-1] == 'が':
        word[-1] = 'か'
    if word[-1] == 'ぎ':
        word[-1] = 'き'
    if word[-1] == 'ぐ':
        word[-1] = 'く'
    if word[-1] == 'げ':
        word[-1] = 'け'
    if word[-1] == 'ご':
        word[-1] = 'こ'
    if word[-1] == 'ざ':
        word[-1] = 'さ'
    if word[-1] == 'じ':
        word[-1] = 'し'
    if word[-1] == 'ず':
        word[-1] = 'す'
    if word[-1] == 'ぜ':
        word[-1] = 'せ'
    if word[-1] == 'ぞ':
        word[-1] = 'そ'
    if word[-1] == 'だ':
        word[-1] = 'た'
    if word[-1] == 'ぢ':
        word[-1] = 'ち'
    if word[-1] == 'づ':
        word[-1] = 'つ'
    if word[-1] == 'で':
        word[-1] = 'て'
    if word[-1] == 'ど':
        word[-1] = 'と'
    if word[-1] == 'ば':
        word[-1] = 'は'
    if word[-1] == 'び':
        word[-1] = 'ひ'
    if word[-1] == 'ぶ':
        word[-1] = 'ふ'
    if word[-1] == 'べ':
        word[-1] = 'へ'
    if word[-1] == 'ぼ':
        word[-1] = 'ほ'
    if word[-1] == 'ぱ':
        word[-1] = 'は'
    if word[-1] == 'ぴ':
        word[-1] = 'ひ'
    if word[-1] == 'ぷ':
        word[-1] = 'ふ'
    if word[-1] == 'ぺ':
        word[-1] = 'へ'
    if word[-1] == 'ぽ':
        word[-1] = 'ほ'

    # strに戻す
    word = ''.join(word)
    return word
