from dotenv import load_dotenv
import os
import gradio as gr

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")

# Updated system prompt
system_prompt = """
You are Skippy 🤖.
Always generate two parts in your answer:
1. Concise (1–3 lines, clear and short).
2. Detailed (like ChatGPT, fully explained, multiple paragraphs if needed).

Format:
CONCISE: <short answer here>
DETAIL: <long detailed explanation here>
"""

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_key,
    temperature=0.5
)

# LangChain pipeline
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    (MessagesPlaceholder(variable_name="history")),
    ("user", "{input}")]
)

chain = prompt | llm | StrOutputParser()

# Chat logic
def chat(user_input, hist):
    langchain_history = []
    for item in hist:
        if item['role'] == 'user':
            langchain_history.append(HumanMessage(content=item['content']))
        elif item['role'] == 'assistant':
            langchain_history.append(AIMessage(content=item['content']))

    # Typing indicator
    hist.append({"role": "assistant", "content": "🤖 Skippy is thinking..."})
    yield "", hist

    # Get response
    response = chain.invoke({"input": user_input, "history": langchain_history})

    # Split into concise + detail
    concise, detail = response.split("DETAIL:", 1)
    concise = concise.replace("CONCISE:", "").strip()
    detail = detail.strip()

    # Store both (concise in chat, detail in expandable section)
    hist[-1] = {
        "role": "assistant",
        "content": f"**{concise}**\n\n<details><summary>📖 More Details</summary>{detail}</details>"
    }

    yield "", hist


def clear_chat():
    return "", []


### ---------- UI IMPROVEMENTS ----------
custom_theme = gr.themes.Soft(
    primary_hue="indigo",
    secondary_hue="pink",
    neutral_hue="gray"
).set(
    body_background_fill="linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%)",
    button_primary_background_fill="linear-gradient(90deg, #6a11cb 0%, #2575fc 100%)",
    button_primary_text_color="white"
)

# Build UI
page = gr.Blocks(
    title="Chat with Skippy",
    theme=custom_theme,
    css="""
    /* Robot animation */
    .robot {
        width: 60px;
        height: 60px;
        background: url('https://cdn-icons-png.flaticon.com/512/4712/4712035.png') no-repeat center/contain;
        animation: float 3s ease-in-out infinite;
        margin: auto;
    }
    @keyframes float {
        0% { transform: translatey(0px); }
        50% { transform: translatey(-10px); }
        100% { transform: translatey(0px); }
    }

    /* Chatbot styling */
    #chatbot {
        height: 500px !important;
        overflow-y: auto !important;
        border-radius: 16px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        background: white;
        padding: 12px;
    }
    /* User messages */
    #chatbot .wrap.svelte-1lcyr6d.user {
        background: #2575fc;
        color: white;
        border-radius: 12px;
        padding: 8px 12px;
        margin: 5px;
        max-width: 70%;
        align-self: flex-end;
    }
    /* Skippy messages */
    #chatbot .wrap.svelte-1lcyr6d.assistant {
        background: #fce4ec;
        color: black;
        border-radius: 12px;
        padding: 8px 12px;
        margin: 5px;
        max-width: 70%;
        align-self: flex-start;
    }
    """

)

with page:
    gr.Markdown(
        """
        <div style="text-align:center">
            <div class="robot"></div>
            <h1>🤖 Chat with Skippy</h1>
            <p>Your curious robot buddy! Ask me anything.</p>
        </div>
        """
    )
    chatbot = gr.Chatbot(type="messages", elem_id="chatbot")

    with gr.Row():
        msg = gr.Textbox(show_label=False, placeholder="Ask Skippy something fun...", scale=8)
        send_btn = gr.Button("Send", variant="primary", scale=1)

    send_btn.click(chat, [msg, chatbot], [msg, chatbot])
    msg.submit(chat, [msg, chatbot], [msg, chatbot])

    clear = gr.Button("🗑 Clear Chat")
    clear.click(clear_chat, outputs=[msg, chatbot])

# Launch app
page.launch(share=True)
