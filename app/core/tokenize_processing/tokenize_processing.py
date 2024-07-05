units = (
    "ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять",
    "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
    "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"
)
tens = (
    "", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят",
    "восемьдесят", "девяносто"
)
hundreds = (
    "", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот",
    "восемьсот", "девятьсот"
)
thousands = ("", "тысяча", "тысячи", "тысяч")
millions = ("", "миллион", "миллиона", "миллионов")
billions = ("", "миллиард", "миллиарда", "миллиардов")

def get_declension(number, forms):
    if 10 <= number % 100 <= 20:
        return forms[3]
    else:
        if number % 10 == 1:
            return forms[1]
        elif 2 <= number % 10 <= 4:
            return forms[2]
        else:
            return forms[3]

def two_digits(n, is_thousand=False):
    if 0 <= n < 20:
        if is_thousand:
            if n == 1:
                return "одна"
            elif n == 2:
                return "две"
        return units[n]
    else:
        return tens[n // 10] + ('' if n % 10 == 0 else ' ' + (("одна" if n % 10 == 1 else "две") if is_thousand and n % 10 in [1, 2] else units[n % 10]))

def three_digits(n, is_thousand=False):
    if n < 100:
        return two_digits(n, is_thousand)
    else:
        return hundreds[n // 100] + ('' if n % 100 == 0 else ' ' + two_digits(n % 100, is_thousand))

def chunk_number(n):
    chunks = []
    while n > 0:
        chunks.append(n % 1000)
        n //= 1000
    return chunks

def number_to_words(number, is_thousand=False):
    chunks = chunk_number(number)
    chunk_count = len(chunks)
    words = []
    for i in range(chunk_count):
        if chunks[i] == 0:
            continue
        if i == 1:  # тысячи
            words.append(three_digits(chunks[i], is_thousand=True) + " " + get_declension(chunks[i], thousands))
        elif i == 2:  # миллионы
            words.append(three_digits(chunks[i]) + " " + get_declension(chunks[i], millions))
        elif i == 3:  # миллиарды
            words.append(three_digits(chunks[i]) + " " + get_declension(chunks[i], billions))
        else:
            words.append(three_digits(chunks[i]))

    return ' '.join(words[::-1])

def convert_amount_to_words(amount):
    rubles = int(amount)
    kopecks = int(round((amount - rubles) * 100))
    
    rubles_word = number_to_words(rubles)
    kopecks_word = number_to_words(kopecks)
    rubles_declension = get_declension(rubles, ("", "рубль", "рубля", "рублей"))
    kopecks_declension = get_declension(kopecks, ("", "копейка", "копейки", "копеек"))
    
    if kopecks == 0:
        return f"{rubles_word} {rubles_declension}"
    else:
        return f"{rubles_word} {rubles_declension} {kopecks_word} {kopecks_declension}"


