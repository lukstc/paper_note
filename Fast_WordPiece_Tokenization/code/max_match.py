def max_match(language:str, text:str, vocabulary:list):


    n = len(text)
    if text == '':
        return []

    for i in range(n):
        first_token = text[:n-i]
        remainder = text[n-i:]
        if first_token in vocabulary:
            return [first_token] + max_match(language,text = remainder,vocabulary=vocabulary)

    # if no match
    # English - return whole text
    # Chinese - return one-char
    if language == "zh":
        first_token = text[0]
        remainder = text[1:]
    elif language == "en":
        first_token = text
        remainder = ""
    else:
        raise ValueError

    return [first_token]+max_match(language, remainder, vocabulary)


if __name__ == "__main__":

    text_zh = "今天的的天气很好"
    # text_zh = "你好呀"
    vocabulary_zh = ["今天","天气","很好"]

    text_en = "supercalifragilisticexpialidocious"
    # text_en = "tokenization"
    # text_en = "superfast"
    vocabulary_en = ["super","cali","fra","gil","istic","ex","pia","lido","cious"]


    print("#"*20, "run - zh","#"*20)
    print("text_zh:",text_zh)
    print("vocabulary_zh:",vocabulary_zh)
    result_zh = max_match('zh',text_zh,vocabulary_zh)
    print(result_zh)

    print("#"*20, "run - en","#"*20)
    print("text_en:",text_en)
    print("vocabulary_en:",vocabulary_en)
    result_en = max_match('en',text_en,vocabulary_en)
    print(result_en)
