import wikipedia

user_search = input("Enter a title or a phrase to search for: ")
wikipedia.set_lang("en")
while user_search != "":
    # try:
    #     user_search = wikipedia.summary(f"{user_search}")
    #     print(user_search)
    # except wikipedia.exceptions.DisambiguationError as e:
    #     print(e.options)
    page = wikipedia.page(user_search, autosuggest=False)
    print(page.title)
    print(page.summary)
    print(page.url)
    user_search = input("Enter a title or a phrase to search for: ")

