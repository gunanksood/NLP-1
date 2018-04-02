lookup_dict = {'hlo': 'hello', 'awsm': 'Awesome', 'asap': 'As soon as possible', 'msg': 'message'}


def object_standardization(text):
    words = text.split()
    new_words = []
    new_text = ""
    for word in words:
        if word in lookup_dict:
            word = lookup_dict[word]
            new_words.append(word)
        new_text = new_text + " " + word
    print new_words
    return new_text


text = raw_input("please enter some text ")
print object_standardization(text)
