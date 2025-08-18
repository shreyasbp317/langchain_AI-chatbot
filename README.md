💬 Chat with Skippy
Chat with Skippy is an AI-powered conversational assistant built with LangChain, Google Generative AI (Gemini), and Gradio.
Skippy isn’t just a chatbot – it engages in reasoning inspired by Einstein’s questioning style, while also adding personal anecdotes to make conversations more human-like.

🚀 Features
🤖 Conversational AI powered by Gemini 2.5 Flash via LangChain

🧠 Context-aware responses with memory of previous messages

🎭 Unique personality: Skippy responds with reasoning and personal insights

🌐 Web-based UI built with Gradio

🧹 Clear chat option to reset conversations

⚡ Lightweight & easy to run locally

📂 Project Structure
bash
Copy
Edit
.
├── main.py         # Main application file
├── .env            # Environment variables (Gemini API key)
├── requirements.txt # Dependencies
└── README.md       # Project documentation
⚙️ Setup & Installation
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/<your-username>/chat-with-skippy.git
cd chat-with-skippy
2. Create a virtual environment (recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Configure environment variables
Create a .env file in the project root and add your Gemini API key:

ini
Copy
Edit
GEMINI_API_KEY=your_api_key_here
▶️ Running the Application
bash
Copy
Edit
python main.py
The Gradio app will launch, and you’ll see a link in your terminal.
Open it in your browser to start chatting with Skippy.

🛠️ Tech Stack
Python 3.9+

LangChain

Google Generative AI (Gemini)

Gradio

python-dotenv

📸 Screenshots
(Add screenshots or GIFs of your chatbot UI here)

📌 Roadmap
 Add persistent database-backed chat history

 Allow multiple personalities (e.g., Einstein, Tesla, Newton)

 Deploy to Hugging Face Spaces or Streamlit Cloud

 Enhance UI with custom styling and themes

🤝 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to check the issues page.

📄 License
Distributed under the MIT License. See LICENSE for more information.
