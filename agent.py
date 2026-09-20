import streamlit as st
from langchain_community.llms import Ollama

# ── LLM setup ─────────────────────────────────────────────
llm = Ollama(model="llama3")

def run_llm(prompt):
    return llm.invoke(prompt)

# ── Agents (same logic as your original script) ──────────
def planner_agent(app_idea):
    prompt = f"""
    You are a senior software architect.

    Break down the following app idea into clear development steps:
    {app_idea}

    Include:
    - Features
    - Tech stack
    - Step-by-step implementation plan
    """
    return run_llm(prompt)

def developer_agent(plan):
    prompt = f"""
    You are a Python developer.

    Based on this plan:
    {plan}

    Write clean, modular, production-ready Python code.
    """
    return run_llm(prompt)

def tester_agent(code):
    prompt = f"""
    You are a software tester.

    Analyze this code:
    {code}

    Identify:
    - Bugs
    - Edge cases
    - Improvements
    """
    return run_llm(prompt)

def reviewer_agent(code):
    prompt = f"""
    You are a senior code reviewer.

    Improve this code:
    {code}

    Focus on:
    - Readability
    - Performance
    - Best practices
    """
    return run_llm(prompt)

# ── Streamlit UI ───────────────────────────────────────────
st.set_page_config(page_title="Startup Buddy", page_icon="🚀", layout="wide")

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Space+Grotesk:wght@400;500;700&display=swap');

        :root {
            --orange: #f77d2b;
            --orange-deep: #eb6c1b;
            --cream: #f8f5f0;
            --ink: #1c1c1c;
            --pink: #f5b0d9;
            --yellow: #f6d64a;
            --green: #80c66a;
            --blue: #5cc4ef;
            --red: #ef4a3b;
            --white: #f8f8f8;
            --line: #111111;
        }

        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
            background: var(--orange);
            color: var(--ink);
            font-family: 'Space Grotesk', sans-serif;
            margin: 0;
            position: relative;
            overflow-x: hidden;
        }

        [data-testid="stApp"] {
            background-image:
                radial-gradient(circle at 10% 20%, rgba(255,255,255,0.18) 0, rgba(255,255,255,0.18) 2px, transparent 3px),
                radial-gradient(circle at 75% 30%, rgba(0,0,0,0.08) 0, rgba(0,0,0,0.08) 2px, transparent 3px),
                radial-gradient(circle at 55% 75%, rgba(255,255,255,0.18) 0, rgba(255,255,255,0.18) 2px, transparent 3px),
                linear-gradient(120deg, transparent 0 45%, rgba(255,255,255,0.08) 45% 47%, transparent 47% 100%);
            background-size: 180px 180px, 180px 180px, 180px 180px, 100% 100%;
            background-repeat: repeat, repeat, repeat, no-repeat;
        }

        .block-container {
            position: relative;
            z-index: 1;
            padding-top: 0;
            padding-bottom: 3rem;
            max-width: 1300px;
            margin-top: 0;
        }

        .block-container::before,
        .block-container::after,
        .block-container .extra-bubble,
        .block-container .extra-bubble-two,
        .block-container .extra-bubble-three,
        .block-container .extra-bubble-four,
        .block-container .extra-bubble-five,
        .block-container .extra-bubble-six,
        .block-container .extra-bubble-seven,
        .block-container .extra-bubble-eight,
        .block-container .extra-bubble-nine {
            content: "";
            position: absolute;
            pointer-events: none;
            z-index: -1;
        }

        .block-container::before {
            left: 3%;
            top: 150px;
            width: 140px;
            height: 140px;
            border: 6px solid rgba(255,255,255,0.22);
            border-radius: 28px;
            transform: rotate(-18deg);
        }

        .block-container::after {
            right: 5%;
            bottom: 70px;
            width: 200px;
            height: 200px;
            background: rgba(255,255,255,0.08);
            border: 5px solid rgba(17,17,17,0.12);
            border-radius: 50%;
            transform: rotate(12deg);
        }

        .extra-bubble,
        .extra-bubble-two,
        .extra-bubble-three,
        .extra-bubble-four,
        .extra-bubble-five,
        .extra-bubble-six,
        .extra-bubble-seven,
        .extra-bubble-eight,
        .extra-bubble-nine {
            display: block;
            border: 4px solid rgba(17,17,17,0.1);
            background: rgba(255,255,255,0.04);
        }

        .extra-bubble { left: 11%; top: 320px; width: 72px; height: 72px; border-radius: 50%; }
        .extra-bubble-two { left: 20%; top: 70px; width: 42px; height: 42px; border-radius: 50%; }
        .extra-bubble-three { right: 18%; top: 220px; width: 54px; height: 54px; border-radius: 50%; }
        .extra-bubble-four { right: 32%; top: 140px; width: 36px; height: 36px; border-radius: 50%; }
        .extra-bubble-five { left: 58%; bottom: 140px; width: 66px; height: 66px; border-radius: 50%; }
        .extra-bubble-six { left: 72%; top: 320px; width: 48px; height: 48px; border-radius: 50%; }
        .extra-bubble-seven { left: 42%; top: 280px; width: 28px; height: 28px; border-radius: 50%; }
        .extra-bubble-eight { right: 14%; bottom: 180px; width: 32px; height: 32px; border-radius: 50%; }
        .extra-bubble-nine { left: 26%; bottom: 120px; width: 26px; height: 26px; border-radius: 50%; }

        [data-testid="stSidebar"] > div {
            background: rgba(255, 255, 255, 0.08);
            border-right: 1px solid rgba(0, 0, 0, 0.15);
        }

        .block-container {
            position: relative;
            z-index: 1;
            padding-top: 0;
            padding-bottom: 3rem;
            max-width: 1300px;
            margin-top: 0;
        }

        header[data-testid="stHeader"],
        [data-testid="stDecoration"],
        [data-testid="stToolbar"],
        .stAppHeader {
            display: none !important;
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            height: 0 !important;
        }

        .hero-box {
            position: relative;
            padding: 0.15rem 0 0.1rem 0;
            margin: 0 0 0.3rem 0;
            text-align: center;
            overflow: visible;
        }

        .hero-box::before,
        .hero-box::after {
            content: "";
            position: absolute;
            width: 28%;
            height: 110px;
            border: 8px solid var(--line);
            border-color: var(--line) transparent transparent transparent;
            border-radius: 55% 45% 0 0 / 100% 100% 0 0;
            top: 0;
            pointer-events: none;
            opacity: 0.95;
        }

        .hero-box::before {
            left: 3%;
            transform: rotate(-12deg);
            border-color: #f6d246 transparent transparent transparent;
        }

        .hero-box::after {
            right: 3%;
            transform: rotate(12deg);
            border-color: #f2f2f2 transparent transparent transparent;
        }

        .hero-text {
            font-family: 'Archivo Black', sans-serif;
            font-size: clamp(3.2rem, 7vw, 8.4rem);
            line-height: 0.89;
            letter-spacing: -0.06em;
            margin: 0;
            color: rgba(19, 19, 19, 0.94);
            text-transform: none;
            text-shadow: 0 0 0 rgba(0,0,0,0);
            display: block;
            white-space: normal;
            padding-top: 0.2rem;
        }

        .subtitle {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 700;
            font-size: clamp(1rem, 1.5vw, 1.6rem);
            letter-spacing: 0.04em;
            text-transform: uppercase;
            color: var(--ink);
            margin-top: 0.7rem;
        }

        .hero-illustration {
            width: min(1100px, 92vw);
            margin: 0 auto 1.4rem auto;
            display: block;
        }

        .hero-illustration svg {
            display: block;
            width: 100%;
            height: auto;
        }

        .agent-row {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 0.8rem 1rem;
            width: min(1100px, 92vw);
            margin: 0 auto 1.4rem auto;
        }

        .agent-tag {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 124px;
            padding: 0.55rem 1rem;
            border: 3px solid rgba(17, 17, 17, 0.95);
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.94);
            color: #111111;
            font-family: 'Archivo Black', sans-serif;
            font-size: 0.7rem;
            letter-spacing: 0.08em;
            text-transform: lowercase;
            box-shadow: 3px 3px 0 rgba(17, 17, 17, 0.9);
            line-height: 1;
        }

        .mega-wrap {
            background: rgba(255,255,255,0.02);
            border-radius: 26px;
            padding: 1rem 0.5rem 0.8rem;
            border: 1px solid rgba(0,0,0,0.08);
        }

        .stTextArea {
            margin-top: 0.5rem;
        }

        .stTextArea textarea {
            background: rgba(255,255,255,0.18);
            color: var(--ink);
            border: 3px solid var(--line);
            border-radius: 20px;
            font-size: 1rem;
            font-weight: 500;
            box-shadow: inset 0 0 0 2px rgba(255,255,255,0.2);
        }

        .stTextArea label {
            font-family: 'Archivo Black', sans-serif;
            font-size: 1.3rem;
            letter-spacing: -0.03em;
            text-transform: uppercase;
            color: var(--ink);
        }

        .stButton > button {
            border: 3px solid var(--line);
            border-radius: 16px;
            background: var(--yellow);
            color: #000000 !important;
            font-family: 'Archivo Black', sans-serif;
            font-size: 1.05rem;
            letter-spacing: 0.04em;
            text-transform: uppercase;
            padding: 0.8rem 1.4rem;
            box-shadow: 5px 5px 0 rgba(0,0,0,0.9);
            transition: transform 0.12s ease, box-shadow 0.12s ease;
        }

        .stButton > button > span,
        .stButton > button p,
        .stButton > button div {
            color: #000000 !important;
        }

        .stButton > button:hover {
            transform: translate(-2px, -2px);
            box-shadow: 7px 7px 0 rgba(0,0,0,0.9);
        }

        .stStatusWidget {
            border: 2px solid rgba(0,0,0,0.18);
            border-radius: 18px;
            background: rgba(255,255,255,0.12);
        }

        div[data-testid="stCodeBlock"] {
            border-radius: 18px;
            border: 2px solid rgba(0,0,0,0.18);
            background: rgba(255,255,255,0.06);
        }

        h1, h2, h3, h4 {
            font-family: 'Archivo Black', sans-serif;
            color: var(--ink);
            letter-spacing: -0.04em;
            text-transform: uppercase;
        }

        .stTabs [role="tablist"] {
            gap: 0.75rem;
        }

        .stTabs [role="tab"] {
            border: 2px solid rgba(0,0,0,0.18);
            background: rgba(255,255,255,0.06);
            border-radius: 12px 12px 0 0;
            color: var(--ink);
            font-weight: 700;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-box">
        <div class="hero-text">BrainDump.exe</div>
        <div class="subtitle">Your AI startup studio</div>
    </div>

    <span class="extra-bubble"></span>
    <span class="extra-bubble-two"></span>
    <span class="extra-bubble-three"></span>
    <span class="extra-bubble-four"></span>
    <span class="extra-bubble-five"></span>
    <span class="extra-bubble-six"></span>
    <span class="extra-bubble-seven"></span>
    <span class="extra-bubble-eight"></span>
    <span class="extra-bubble-nine"></span>

    <div class="agent-row">
        <div class="agent-tag">planner</div>
        <div class="agent-tag">developer</div>
        <div class="agent-tag">tester</div>
        <div class="agent-tag">reviewer</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Keep results across reruns so expanders don't reset when you interact with them
if "results" not in st.session_state:
    st.session_state.results = None

app_idea = st.text_area(
    "What are we building today?",
    placeholder="I want to build a pet dating app",
    height=120,
)

if st.button("Launch build", type="primary", disabled=not app_idea.strip()):
    results = {}

    with st.status("Planning...", expanded=True) as status:
        results["plan"] = planner_agent(app_idea)
        st.write(results["plan"])
        status.update(label="Planning complete", state="complete")

    with st.status("Developing...", expanded=True) as status:
        results["code"] = developer_agent(results["plan"])
        st.code(results["code"], language="python")
        status.update(label="Development complete", state="complete")

    with st.status("Testing...", expanded=True) as status:
        results["test_report"] = tester_agent(results["code"])
        st.write(results["test_report"])
        status.update(label="Testing complete", state="complete")

    with st.status("Reviewing...", expanded=True) as status:
        results["final_code"] = reviewer_agent(results["code"])
        st.code(results["final_code"], language="python")
        status.update(label="Review complete", state="complete")

    st.session_state.results = results

# ── Display persisted results (so tabs/downloads survive reruns) ──
if st.session_state.results:
    r = st.session_state.results
    st.divider()
    st.subheader("Full Results")

    tab1, tab2, tab3, tab4 = st.tabs(["Plan", "Initial Code", "Test Report", "Final Code"])
    with tab1:
        st.write(r["plan"])
    with tab2:
        st.code(r["code"], language="python")
    with tab3:
        st.write(r["test_report"])
    with tab4:
        st.code(r["final_code"], language="python")
        st.download_button(
            "⬇Download final code",
            data=r["final_code"],
            file_name="generated_app.py",
            mime="text/x-python",
        )

