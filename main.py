from api.gpt4 import GPT4

gpt = GPT4(config_file="config.ini")

gpt.login()
print(gpt.design("a cow"))

gpt.ask_question("hi")
print(gpt.get_response())