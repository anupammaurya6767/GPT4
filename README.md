# GPT-4 API
<img align='right' src="https://github.com/anupammaurya6767/GPT4/blob/main/assets/Designer.png" width="230">
The GPT4 API project aims to provide an automated interface for interacting with the GPT-4 (Generative Pre-trained Transformer 4) model developed by OpenAI. GPT-4 is a state-of-the-art natural language processing model capable of generating human-like text based on input prompts.


## Description

The **GPT-4 API** is an interface for interacting with the powerful GPT-4 language model. It allows you to generate natural language text, perform question-answering tasks, and more. Whether you're building chatbots, content generators, or creative writing tools, GPT-4 has got you covered!

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Make sure you have the following installed-

- Python: You'll need Python installed on your system.
- Selenium: We'll be using Selenium for web automation.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/anupammaurya6767/GPT4.git
    ```

2. Install dependencies:

    ```bash
    pip install selenium
    ```

3. Set up your GPT-4 credentials (Microsoft account username, password, etc.) in `config.ini`.

## Usage

1. Initialize the GPT-4 API:

    ```python
    from api.gpt4 import GPT4

    ap = GPT4(config_file='config.ini')
    ```

2. Log in to the GPT-4 service:

    ```python
    ap.login()
    ```

3. Ask questions or generate text:

    ```python
    question = 'What is the meaning of life?'
    ap.ask_question(question, max_t=10)
    response = ap.get_response()
    ```

4. Close the API connection when done:

    ```python
    ap.close()
    ```

## Features

- **Natural Language Generation**: Create human-like text.
- **Question-Answering**: Get accurate answers to queries.
- **Customizable**: Fine-tune GPT-4 for specific tasks.
- **Scalable**: Handle large volumes of requests.

## Contributing

Contributions are welcome! If you find a bug or have an enhancement idea, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
