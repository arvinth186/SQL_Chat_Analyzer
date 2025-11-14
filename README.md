<h1 align="center">🐔 SQL Chat Analyzer</h1>
<p align="center">
  An interactive Streamlit application that allows users to query SQL databases using natural language,
  powered by LangChain, Groq LLMs, and SQL Agents.
</p>

<hr>

<h2>📌 Overview</h2>
<p>
  <strong>SQL Chat Analyzer</strong> is a Streamlit-based AI application that converts natural language queries into
  executable SQL queries. It works with both <strong>SQLite</strong> and <strong>MySQL</strong> databases and uses
  <strong>LangChain SQL Agent</strong> + <strong>Groq Llama 3.1</strong> model to interpret user questions and generate accurate SQL responses.
</p>
<p>
  The app also provides a chat-style interface with conversation history, in-depth reasoning visibility, and
  instant streaming responses.
</p>

<hr>

<h2>🚀 Features</h2>
<ul>
  <li>🔹 Connect to <strong>SQLite (sqlchat.db)</strong> or <strong>MySQL</strong> with user credentials</li>
  <li>🔹 Ask natural language questions and get SQL-generated answers</li>
  <li>🔹 Uses <strong>LangChain SQL Agent</strong> with <strong>ZERO_SHOT_REACT_DESCRIPTION</strong></li>
  <li>🔹 Real-time streaming responses using <strong>Groq LLM</strong></li>
  <li>🔹 Conversation history stored in <code>st.session_state</code></li>
  <li>🔹 Streamlit callback handler to show agent reasoning steps</li>
  <li>🔹 Caches DB connection for faster performance</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>

<pre>
├── app.py                 # Main Streamlit application
├── sqlchat.db             # SQLite database (auto-loaded if used)
├── requirements.txt       # Dependencies (optional)
</pre>

<hr>

<h2>🧠 Tech Stack</h2>
<ul>
  <li><strong>Python 3.x</strong></li>
  <li><strong>Streamlit</strong> – UI framework</li>
  <li><strong>LangChain Classic</strong> – SQL Agent + Toolkit</li>
  <li><strong>Groq LLM</strong> (Llama 3.1 – 8B Instant)</li>
  <li><strong>SQLAlchemy</strong> – DB engine</li>
  <li><strong>SQLite / MySQL</strong> – Database backends</li>
</ul>

<hr>

<h2>⚙️ Installation</h2>

<p>Clone the repository:</p>
<pre><code>git clone https://github.com/yourusername/sql-chat-analyzer.git
cd sql-chat-analyzer
</code></pre>

<p>Install dependencies:</p>
<pre><code>pip install -r requirements.txt
</code></pre>

<p>(Sample <strong>requirements.txt</strong> you can add)</p>

<pre><code>
streamlit
langchain-classic
langchain-groq
sqlalchemy
mysql-connector-python
</code></pre>

<hr>

<h2>🔌 Setting Up Databases</h2>

<h3>1️⃣ SQLite</h3>
<p>
  The app automatically loads <strong>sqlchat.db</strong> placed in the same directory.
</p>

<h3>2️⃣ MySQL</h3>
<p>Provide credentials in the sidebar:</p>

<ul>
  <li>Host</li>
  <li>User</li>
  <li>Password</li>
  <li>Database Name</li>
</ul>

<hr>

<h2>▶️ Running the App</h2>

<pre><code>streamlit run app.py
</code></pre>

<p>
  Open the URL shown in the terminal (usually <code>http://localhost:8501</code>).
</p>

<hr>

<h2>🧩 How It Works</h2>
<ol>
  <li>User selects database type (SQLite or MySQL) from sidebar.</li>
  <li>User enters Groq API key to activate the LLM.</li>
  <li>The app configures SQL database using <code>SQLDatabase</code>.</li>
  <li>LangChain's <strong>SQL Agent</strong> interprets the natural language query.</li>
  <li>Agent constructs and runs SQL queries directly on the connected DB.</li>
  <li>Results are displayed in a chat interface with history.</li>
</ol>

<hr>

<h2>💻 Key Code Highlights</h2>

<h3>🔹 Database Configuration</h3>
<p>Cached for performance:</p>
<pre><code>@st.cache_resource(ttl="2h")
def configure_db(...):
    ...
</code></pre>

<h3>🔹 Groq LLM</h3>
<pre><code>
model = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=api_key,
    streaming=True
)
</code></pre>

<h3>🔹 SQL Agent</h3>
<pre><code>
agent = create_sql_agent(
    llm=model,
    toolkit=toolkit,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
</code></pre>

<h3>🔹 Chat Interface</h3>
<pre><code>
user_query = st.chat_input("Ask SQL related questions here...")
response = agent.run(user_query)
</code></pre>

<hr>

<h2>📷 Dashboard Preview</h2>

<p align="center">
  <img src="Dashboard_preview.png" alt="SQL Chat Analyzer" width="800">
</p>

<p align="center">
  <i>Example interface of the Streamlit-based PDF Q&A Chatbot.</i>
</p>

<hr>

<h2>🛡️ Notes & Best Practices</h2>
<ul>
  <li>Never expose your Groq API key publicly.</li>
  <li>Use read-only DB users in production.</li>
  <li>SQLite DB file must exist in project root.</li>
  <li>For large MySQL DB, index your tables.</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>
<p>
  Feel free to submit issues or create pull requests. Contributions are welcome!
</p>

<hr>

<h2>📄 License</h2>
<p>
  This project is released under the <strong>MIT License</strong>.
</p>

<hr>

<h2>⭐ Support</h2>
<p>If you like this project, consider giving it a ⭐ on GitHub!</p>

