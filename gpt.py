import openai
openai.api_key = "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"

def answer(prompt="write compliment for person who has not glasses and looks happy"):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "user", "content": prompt},
            ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content
    return(result)

def compliment(prompt="write compliment for person who has not glasses and looks happy"):
    eng = answer(prompt)
    ukr = answer('переклади українською: '+eng)
    return ukr


if __name__=='__main__':
    print(compliment())