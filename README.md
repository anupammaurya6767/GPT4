<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/anupammaurya6767/GPT4">
    <img src="https://github.com/anupammaurya6767/GPT4/raw/main/assets/gpt4.png" alt="Logo" width="230" height="230">
  </a>

  <h3 align="center">GPT4</h3>

  <p align="center">
     GPT4-API
    <br />
    ·
    <a href="https://github.com/anupammaurya6767/GPT4/issues">Report Bug</a>
    ·
    <a href="https://github.com/anupammaurya6767/GPT4/issues">Request Feature</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

[![GPT4][product-screenshot]](https://github.com/anupammaurya6767/GPT4/raw/main/assets/x%20vfdzv.png)

[![Watch the video](https://img.youtube.com/vi/Km1RiNiwxqs/0.jpg)](https://www.youtube.com/watch?v=Km1RiNiwxqs)


The **GPT-4 API** is an interface for interacting with the powerful GPT-4 language model. It allows you to generate natural language text, perform question-answering tasks, and more. Whether you're building chatbots, content generators, or creative writing tools, GPT-4 has got you covered!

Here's why:
* Free access to GPT-4.😀
* Seamless integration into your code.😋
* Generate text and images effortlessly.😮
* Explore the GPT-4 API on GitHub.🌟
* Don't forget to give it a star, fork, and contribute. 😎


<p align="right">(<a href="#top">back to top</a>)</p>


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
    pip install -r requirements.txt
    ```

    #### Or
```
pip install api-gpt4
```

4. Set up your GPT-4 credentials (Microsoft account username, password, etc.) in `config.ini`.

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
    ap.ask_question(question)
    response = ap.get_response()
    ```

4. Image Generation:

    ```python
    prompt = 'A man on bike'
    response = ap.design(prompt)
    ```

5. Close the API connection when done:

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

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/anupammaurya6767/GPT4.svg?style=for-the-badge
[contributors-url]: https://github.com/anupammaurya6767/GPT4/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/anupammaurya6767/GPT4.svg?style=for-the-badge
[forks-url]: https://github.com/anupammaurya6767/GPT4/network/members
[stars-shield]: https://img.shields.io/github/stars/anupammaurya6767/GPT4.svg?style=for-the-badge
[stars-url]: https://github.com/anupammaurya6767/GPT4/stargazers
[issues-shield]: https://img.shields.io/github/issues/anupammaurya6767/GPT4.svg?style=for-the-badge
[issues-url]: https://github.com/anupammaurya6767/GPT4/issues
[license-shield]: https://img.shields.io/github/license/anupammaurya6767/GPT4.svg?style=for-the-badge
[license-url]: https://github.com/anupammaurya6767/GPT4/blob/main/LICENSE
[product-screenshot]: https://github.com/anupammaurya6767/GPT4/raw/main/assets/x%20vfdzv.png
