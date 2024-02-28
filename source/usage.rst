Usage
=====

from GPT4 import GPT4

# Initialize GPT4
gpt4 = GPT4(config_file='config.ini')

# Login to the GPT-4 API
gpt4.login()

# Ask a question
gpt4.ask_question('What is the capital of France?')

# Get the response
response = gpt4.get_response()
print(response)

# Design something
design = gpt4.design('Create a logo for my company')
print(design)

# Close the GPT4 instance
gpt4.close()