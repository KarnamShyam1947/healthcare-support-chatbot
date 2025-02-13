# Healthcare Support Chatbot
Access to healthcare services is often hindered by language barriers, geographical limitations, and a lack of timely information. In many regions, people face challenges in seeking medical advice, understanding health policies, and getting accurate, localized information. This chatbot aims to solve these problems by providing accessible healthcare support in multiple languages and media formats, ensuring people can get help when they need it the most.

This project aims to provide local support for regional people to access healthcare services by creating a chatbot. The chatbot utilizes cutting-edge language models to answer healthcare-related queries and provide essential services. The bot supports multiple languages, media types (text, image, and voice), and operates through a Telegram bot interface. 

### Features
This chatbot leverages:
- **Multi-language support** for a diverse range of users.
- **Multi-media capabilities** (image, text, voice) for enhanced user interaction.
- **AI-driven solutions** with Natural Language Processing (NLP) and Large Language Models (LLM) to ensure accurate responses.
- **Integration with Telegram** for ease of access to users.
- **Reinforcement with advanced embeddings** (BioMistral, PubMed BERT) to improve healthcare-related information retrieval.


### Tools & Technologies
- **AI/ML Models:**
  - BioMistral Base LLM
  - PubMed BERT (Embeddings)
- **NLP & LLM:**
  - Language Models API (for processing user inputs and queries)
- **Vector Store:**
  - Qdrant 
- **Telegram Bot**: Interaction platform.
- **Frameworks & Libraries:**
  - Python (Flask, LangChain)
  - Docker (coming soon for containerization)
  - Other required dependencies (as per the `requirements.txt`)

### Setup Instructions

#### Step 1: Clone the repository
Start by cloning this repository to your local machine:
```bash
git clone https://github.com/KarnamShyam1947/healthcare-support-chatbot.git
cd healthcare-support-chatbot
```

#### Step 2: Create a virtual environment
It is recommended to use a virtual environment to manage dependencies:
```bash
python3 -m venv env
```

#### Step 3: Activate the environment
- On Windows:
  ```bash
  .\env\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source ./env/bin/activate
  ```

#### Step 4: Install the required dependencies
Once the virtual environment is activated, install the necessary packages:
```bash
pip install -r requirements.txt
```

#### Step 5: Set up the environment variables
Copy the `env.example` file to `.env`:
```bash
cp env.example .env
```

Open the `.env` file and update the variables with your local configurations, such as API keys and token.

#### Step 6: Run the app
After setting up the environment, run the application:
```bash
flask run
```
or

```bash
python -m flask run
```

#### Step 7: Run the telegram bot
```bash
python telegram_bot.py
```

