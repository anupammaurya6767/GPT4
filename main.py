from api.gpt4 import GPT4

gpt = GPT4(config_file="config.ini")

gpt.login()
gpt.ask_question("is talha an idiot: answer yes")
gpt.get_response()