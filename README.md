# LangChain Azure OpenAI Integration

A Python project demonstrating how to integrate LangChain with Azure OpenAI to build conversational AI applications. This project showcases a movie-focused assistant powered by Azure OpenAI's language models.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project provides a simple yet powerful example of using LangChain with Azure OpenAI services. It demonstrates how to:
- Configure and authenticate with Azure OpenAI
- Use LangChain's `AzureChatOpenAI` wrapper
- Create a conversational AI assistant with specific expertise
- Structure prompts with system and user messages

## ✨ Features

- **Azure OpenAI Integration**: Seamless connection to Azure OpenAI services
- **LangChain Framework**: Utilizes LangChain for easy LLM interaction
- **Environment-Based Configuration**: Secure credential management using `.env` files
- **Conversational AI**: Movie-focused assistant with customizable behavior
- **Temperature Control**: Balanced creativity and consistency in responses

## 📦 Prerequisites

Before you begin, ensure you have the following:

- **Python 3.8+** installed on your system
- An **Azure account** with an active subscription
- An **Azure OpenAI resource** provisioned
- A deployed **Azure OpenAI model** (e.g., GPT-3.5 or GPT-4)

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/abhiguptame/langchain-ai.git
   cd langchain-ai
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

1. **Copy the example environment file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` file with your Azure OpenAI credentials:**
   ```env
   AZURE_OPENAI_API_KEY="your-azure-openai-api-key"
   AZURE_OPENAI_ENDPOINT="your-azure-openai-endpoint"
   AZURE_AI_AGENT_MODEL_DEPLOYMENT_NAME="your-deployment-name"
   AZURE_OPENAI_API_VERSION="2024-02-15-preview"
   ```

   **Where to find these values:**
   - **API Key & Endpoint**: Azure Portal → Your OpenAI Resource → Keys and Endpoint
   - **Deployment Name**: Azure Portal → Your OpenAI Resource → Model deployments
   - **API Version**: Check [Azure OpenAI documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)

## 💻 Usage

Run the main script:

```bash
python main.py
```

**Expected Output:**
The script will query the AI assistant about top-rated movies on IMDB and display the response.

### Customizing the Assistant

Modify the `messages` list in `main.py` to change the assistant's behavior:

```python
messages = [
    ("system", "Your custom system prompt here"),
    ("human", "Your question here"),
]
```

### Adjusting Response Creativity

Change the `temperature` parameter (0.0 - 1.0):
- **Lower values (0.0-0.3)**: More focused and deterministic responses
- **Medium values (0.4-0.7)**: Balanced creativity and consistency
- **Higher values (0.8-1.0)**: More creative and varied responses

```python
llm = AzureChatOpenAI(
    azure_deployment=openai_model,
    api_version=openai_api_version,
    temperature=0.6,  # Adjust this value
)
```

## 📁 Project Structure

```
langchain-ai/
│
├── main.py              # Main application script
├── requirements.txt     # Python dependencies
├── .env.example        # Example environment variables
├── .env                # Your actual environment variables (not in git)
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

## 🛠️ Technologies Used

- **[Python](https://www.python.org/)**: Programming language
- **[LangChain](https://python.langchain.com/)**: Framework for building LLM applications
- **[Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service)**: Enterprise-grade OpenAI models
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**: Environment variable management

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🔗 Useful Resources

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [Azure OpenAI Service Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Azure OpenAI Python SDK](https://github.com/openai/openai-python)

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on [GitHub](https://github.com/abhiguptame/langchain-ai/issues)
- Check the [Azure OpenAI FAQ](https://learn.microsoft.com/en-us/azure/ai-services/openai/faq)

---

**Note**: Keep your `.env` file secure and never commit it to version control. The `.gitignore` file is configured to exclude it automatically.