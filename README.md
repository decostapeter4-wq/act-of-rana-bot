# Act of Rana Bot

A terminal-based conversational AI assistant for Python 3.10+, powered by Google's
Gemini API. It uses Gemini function calling to request live DuckDuckGo search results
when current information is useful, and renders responses with Rich.

## Features

- Gemini model integration through the official `google-genai` SDK.
- Tool-calling workflow for optional DuckDuckGo web search (`ddgs`).
- Rich terminal Markdown, panels, prompts, and a thinking indicator.
- In-memory conversation history with a configurable limit.
- `/help`, `/reset`, and `/exit` commands.
- Environment-based configuration; `.env` is excluded from Git.

> Search results are third-party data and may be incomplete or inaccurate. Verify
> important claims against primary sources. API usage may incur provider charges.
> This assistant is designed for legitimate technical, educational, and defensive
> work; it is not an authorization bypass or a guarantee that every request can
> be fulfilled.

## 1. Requirements

- Kali Linux or another Linux distribution.
- Python 3.10 or newer.
- Internet connection.
- Gemini API key from [Google AI Studio](https://aistudio.google.com/).

Check Python:

```bash
python3 --version
```

## 2. Create the project

```bash
mkdir -p ~/act-of-rana-bot
cd ~/act-of-rana-bot
git init
```

Put `main.py`, `requirements.txt`, `.env.example`, and `.gitignore` in this directory.
Alternatively, extract the supplied project archive and `cd` into its folder.

## 3. Create and activate a virtual environment

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
```

If Kali reports an externally-managed-environment error, do not use `sudo pip`.
Install packages only after activating the virtual environment.

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure the API key

Copy the example file:

```bash
cp .env.example .env
nano .env
```

Set `GEMINI_API_KEY` to your own key. Keep `.env` private and never commit it.

You can also export variables for the current shell instead of using `.env`:

```bash
export GEMINI_API_KEY="your_api_key_here"
export GEMINI_MODEL="gemini-2.5-flash"
```

The `.env` file takes care of loading values automatically when the application starts.

## 6. Run

```bash
python main.py
```

Try a question that benefits from current information, for example:

```text
What changed in the latest Python 3.13 release? Search for current sources.
```

## 7. Commands

| Command | Action |
|---|---|
| `/help` | Show available commands |
| `/reset` | Clear in-memory conversation history |
| `/exit` or `/quit` | Exit the application |

## 8. Git hygiene

Before committing, check that `.env` is ignored:

```bash
git status --short
git check-ignore .env
```

Commit source files:

```bash
git add main.py requirements.txt README.md .env.example .gitignore
git commit -m "Initial Act of Rana Bot implementation"
```

Never add `.env` or paste API credentials into issues, logs, screenshots, or chat.

## Configuration

| Variable | Default | Description |
|---|---:|---|
| `GEMINI_API_KEY` | required | Gemini API key |
| `GEMINI_MODEL` | `gemini-2.5-flash` | Model identifier supported by your account |
| `MAX_SEARCH_RESULTS` | `5` | Maximum results per search (1–10) |
| `MAX_HISTORY_TURNS` | `12` | Approximate user/assistant turn pairs retained |
| `LOG_LEVEL` | `WARNING` | Python logging level |

## Troubleshooting

**`GEMINI_API_KEY is missing`** — Confirm `.env` exists in the current project
directory and contains `GEMINI_API_KEY=...`, or export the variable in the shell.

**Authentication, quota, or model errors** — Verify the key, enabled API access,
billing/quota status, and model identifier in Google AI Studio.

**Search errors** — DuckDuckGo access can be rate-limited or temporarily unavailable.
The bot reports a search error to the model; retry later or use a trusted source
directly.

**Virtual environment activation** — Run `source venv/bin/activate` from the
project directory each time you open a new terminal.

## Architecture

1. `RanaBot.ask()` appends the user message to bounded in-memory history.
2. Gemini receives the conversation and the `search_web` function declaration.
3. If Gemini requests the function, the app calls DDGS and sends results back as a
   function response.
4. Gemini produces the final answer, which Rich renders in the terminal.

## License

MIT. See `LICENSE`.
