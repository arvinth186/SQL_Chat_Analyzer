import streamlit as st
from pathlib import Path

from langchain_classic.agents import create_sql_agent
from langchain_classic.sql_database import SQLDatabase
from langchain_classic.agents import AgentType
from langchain_classic.callbacks import StreamlitCallbackHandler
from langchain_classic.agents.agent_toolkits import SQLDatabaseToolkit
from langchain_groq import ChatGroq
from sqlalchemy import create_engine
import sqlite3

st.set_page_config(page_title="SQL Chat Analyzer", page_icon="🐔", layout="wide")
st.title("SQL Chat Analyzer 🐔")




LOCALDB = "USE+LOCALDB"
MYSQL = "USE_MYSQL" # mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname> [uded for SQLDatabase.from_uri]

radio_opt = ["USe Sql3 Database- Student.db","Connect to MySQL Database"]
with st.sidebar:
    selected_opt = st.radio("Select Database Option", radio_opt)

if radio_opt.index(selected_opt)==1:
    db_uri = MYSQL
    mysql_host = st.sidebar.text_input("Please enter MySQL Host")
    mysql_user = st.sidebar.text_input("Please enter MySQL User")
    mysql_password = st.sidebar.text_input("Please enter MySQL Password", type="password")
    mysql_db = st.sidebar.text_input("Please enter MySQL Database Name")

else:
    db_uri = LOCALDB

api_key = st.sidebar.text_input("Please enter Groq API Key", type="password")

if not db_uri:
    st.warning("Please select a database option to proceed.")
    st.stop()
if not api_key:
    st.warning("Please enter Groq API Key to proceed.")
    st.stop()

## LLM Model
model =  ChatGroq(model="llama-3.1-8b-instant", groq_api_key=api_key, streaming=True)

# Configure Database Connection

@st.cache_resource(ttl="2h") # cache the database connection for 2 hours
def configure_db(db_uri,mysql_host=None, mysql_user=None, mysql_password=None, mysql_db=None):
    if db_uri == LOCALDB:

        dbfilepath = (Path(__file__).parent/"sqlchat.db").absolute()
        print(f"SQLite DB Path: {dbfilepath}")
        # creator = lambda: sqlite3.connect(f"file:{dbfilepath}?mode=ro",uri=True)
        # creator = lambda: sqlite3.connect(dbfilepath)
        engine = create_engine(f"sqlite:///{dbfilepath}")
        return SQLDatabase(engine=engine)

    elif db_uri == MYSQL:
        if not mysql_host or not mysql_user or not mysql_password or not mysql_db:
            st.warning("Please enter all MySQL connection details in the sidebar to proceed.")
            st.stop()
        
        return SQLDatabase.from_uri(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}")

if db_uri == MYSQL:
    db=configure_db(db_uri, mysql_host, mysql_user, mysql_password, mysql_db)
else:
    db=configure_db(db_uri)


# Create SQL Agent with Streamlit Callbacks

toolkit = SQLDatabaseToolkit(db=db, llm=model)
agent = create_sql_agent(
    llm=model,
    toolkit=toolkit,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
    # max_iterations=20,        # default is 5
    # max_execution_time=60     # in seconds
)

if "messages" not in st.session_state or st.sidebar.button("Clear Conversation"):
    st.session_state.messages = [{"role": "assistant", "content": "How can I help you with your SQL database?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


user_query = st.chat_input("Ask SQL related questions here...")
if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query) # display user message in chat

    with st.chat_message("assistant"):
        streamlit_callback = StreamlitCallbackHandler(st.container()) # responsible for showu==ing the chain of thoughts
        response = agent.run(user_query, callbacks=[streamlit_callback])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)  # display final answer
        





