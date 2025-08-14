# AutoPost AI — Multi-Agent Social Content Generator
**Streamlit app that plans, drafts, critiques, and packages platform-optimized posts (text + images) in one run.**

> **Why**: Ship consistent, on-brand posts faster.  
> **How**: A 7-agent pipeline (Autogen) with a prompt-critic feedback loop tuned per platform.

---

## ✨ Features
- **One-click pipeline**: Brief → ideas → copy → image → critique → revision → publish-ready assets.
- **Platform profiles**: Style, length, and metadata tailored for X, LinkedIn, Instagram, and Reddit.
- **Critic-in-the-loop**: Automatic quality checks (clarity, tone, length, hooks, CTAs, hashtags, alt-text).
- **Modular agents**: 7 scripts you can swap or extend (Writer, Vision, Critic, Hashtag/SEO, etc.).
- **Streamlit UI**: Simple front-end for briefs, iterations, previews, and export.
- **Stateless/Stateful**: Run single-shot or keep conversation state per session.

---

## 🧱 Architecture (High-Level)
User Brief ──▶ PlannerAgent ──▶ CopywriterAgent ──▶ ImageAgent
              ▲           │
              │           ▼
        CriticAgent ◀── HashtagAgent
              │
              └──▶ FormatterAgent ──▶ PublisherAgent (or export)

Roles:
- PlannerAgent: expand brief, pick angles/platforms/constraints
- CopywriterAgent: platform-specific copy + alt text
- ImageAgent: generate/edit visuals from prompts
- CriticAgent: rubric-based review (clarity, hook, tone, length, accessibility)
- HashtagAgent: hashtags/SEO/metadata per platform
- FormatterAgent: final layout, emojis, line breaks, UTM links
- PublisherAgent: API publish or export (JSON/MD/PNG)


**Agent roles**
1. **PlannerAgent** – expands brief, defines angle, platforms, and constraints  
2. **CopywriterAgent** – drafts platform-specific copy & alt-text  
3. **ImageAgent** – generates/edits visuals from prompts  
4. **CriticAgent** – scores against rubric; suggests rewrites  
5. **HashtagAgent** – suggests hashtags/SEO snippets per platform  
6. **FormatterAgent** – final layout, emojis, line-break rules, UTM links  
7. **PublisherAgent** – pushes to APIs or exports to `/exports`

---

## 🧰 Tech Stack
- **Python 3.10+**, **Streamlit**
- **Autogen** (multi-agent orchestration)
- **LLM providers** (OpenAI/Anthropic/etc.) via pluggable adapters
- **Image generation** (DALL·E/Stable Diffusion—adapter based)
- **dotenv / pydantic** for config

---

## 📁 Project Structure

autopost-ai/
├─ app.py                          # Streamlit entry point
├─ agents/
│  ├─ planner_agent.py
│  ├─ copywriter_agent.py
│  ├─ image_agent.py
│  ├─ critic_agent.py
│  ├─ hashtag_agent.py
│  ├─ formatter_agent.py
│  └─ publisher_agent.py
├─ core/
│  ├─ pipeline.py                  # Orchestrates the 7-agent flow
│  ├─ prompts.py                   # System prompts & critic rubrics
│  ├─ providers.py                 # LLM/image provider adapters
│  └─ utils.py                     # Logging, IO, tracing, helpers
├─ configs/
│  ├─ platforms.yaml               # Per-platform rules (length, tone, hashtags)
│  └─ settings.yaml                # Models, temps, seeds, critic rounds
├─ exports/                        # Generated assets (JSON/MD/PNG)
├─ requirements.txt
├─ .env.example
└─ README.md


---

## ⚙️ Setup

```bash
git clone https://github.com/yourname/autopost-ai.git
cd autopost-ai
python -m venv .venv && source .venv/bin/activate   # (Windows) .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env


# LLMs (use what you have)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=
STABILITY_API_KEY=

# Optional: publisher tokens (leave blank to export only)
TWITTER_BEARER_TOKEN=
LINKEDIN_CLIENT_ID=
LINKEDIN_CLIENT_SECRET=
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=


streamlit run app.py

