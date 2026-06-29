import streamlit as st
from chatbot_agent import build_agent, chat

# ── PAGE CONFIG ─────────────────────────────────────────────
st.set_page_config(
    page_title="LLaMA 3 Agent",
    page_icon="🦙",
    layout="centered"
)

# ── SIDEBAR ─────────────────────────────────────────────────
with st.sidebar:
    st.title("🦙 LLaMA 3 Agent")
    st.caption("Powered by Ollama + LangChain + LangGraph")

    st.divider()

    st.markdown("### 🛠️ Tools Available")
    st.markdown("""
    - 🔍 **Web Search** — DuckDuckGo
    - 📖 **Wikipedia** — Factual queries
    - 🕐 **Date & Time** — Current datetime
    - 🧮 **Calculator** — Math expressions
    """)

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.history = []
        st.session_state.pending_input = None
        st.rerun()

    st.divider()

    st.markdown("### 💡 Try asking:")
    st.markdown("""
    - What is today's date?
    - What is 23% of 85000?
    - Who is APJ Abdul Kalam?
    - Latest news about AI?
    """)

# ── SESSION STATE INIT ───────────────────────────────────────
if "agent" not in st.session_state:
    with st.spinner("⏳ Loading LLaMA 3 agent..."):
        st.session_state.agent = build_agent()

if "history" not in st.session_state:
    st.session_state.history = []

if "is_thinking" not in st.session_state:
    st.session_state.is_thinking = False

if "pending_input" not in st.session_state:
    st.session_state.pending_input = None

# ── MAIN AREA ────────────────────────────────────────────────
st.title("💬 Chat")

# ── WELCOME MESSAGE ──────────────────────────────────────────
if len(st.session_state.history) == 0 and not st.session_state.is_thinking:
    with st.chat_message("assistant"):
        st.write("Hey! I'm your LLaMA 3 powered assistant 🦙 I can search the web, do math, look up Wikipedia, and tell you the time. What would you like to know?")

# ── DISPLAY CHAT HISTORY ─────────────────────────────────────
for human, ai in st.session_state.history:
    with st.chat_message("user"):
        st.write(human)
    with st.chat_message("assistant"):
        st.write(ai)

# ── SHOW THINKING STATE ──────────────────────────────────────
if st.session_state.is_thinking:
    with st.chat_message("user"):
        st.write(st.session_state.pending_input)
    with st.chat_message("assistant"):
        with st.spinner("🦙 Thinking..."):
            try:
                response = chat(
                    agent=st.session_state.agent,
                    user_input=st.session_state.pending_input,
                    history=st.session_state.history
                )
                # Save and reset
                st.session_state.history.append(
                    (st.session_state.pending_input, response)
                )
                st.session_state.pending_input = None
                st.session_state.is_thinking = False
                st.rerun()

            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")
                st.session_state.is_thinking = False
                st.session_state.pending_input = None
                st.rerun()

# ── INPUT — only shown when NOT thinking ─────────────────────
else:
    if user_input := st.chat_input("Ask me anything..."):
        # Store input and set thinking flag BEFORE rerun
        st.session_state.pending_input = user_input
        st.session_state.is_thinking = True
        st.rerun()  # rerun immediately to lock the UI

# ── AUTO SCROLL ──────────────────────────────────────────────
st.write(
    '<script>window.parent.document.querySelector("section.main").scrollTop = 999999</script>',
    unsafe_allow_html=True
)