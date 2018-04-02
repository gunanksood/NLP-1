import re
noise_list = ['is', 'am', 'are', 'in', 'the', 'this', 'of', '@*', 'http*', '#*']

def noise_removal(input_text):
    tokens = input_text.split()
    noise_free_words = [word for word in tokens if word not in noise_list]
    noise_free = " ".join(noise_free_words)
    print noise_free
    mentions = re.finditer('@\w*', noise_free)
    for i in mentions:
        print i.group().strip()
        noise_free = re.sub(i.group(), '', noise_free)
    return noise_free


text = raw_input('Hey! please enter some text ')
noise_free_text = noise_removal(text)
print noise_free_text
