# DBZClanker AI Discord Bot

A powerful, secure, and feature-rich Discord bot powered by the Groq API. It features unhinged and uncensored conversations, multi-key rotation, interactive trivia games with server/global leaderboards, and persistent user customization.

## Features

### 🤖 Groq AI Chat
- **Primary AI Models**: Rotates through Groq models in priority order for all chat interactions.
- **Unhinged Roast Personality**: Features a built-in uncensored and unhinged roasting personality that responds directly, rudely, and uses gender-based roasts for user interactions (by default).
- **Streaming Responses**: Real-time editing of bot messages as the response generates, including separate thinking blocks (`🤔 Thinking...`) for reasoning/thinking models (e.g. DeepSeek R1, Qwen 3).
- **Reply Context**: Reply to messages and tag the bot to maintain context-aware conversations.

### 🎮 Gaming & Trivia
- **Trivia Engine**: General knowledge, anime, and Genshin Impact trivia.
- **Interactive Buttons**: Pure Discord UI buttons for selecting answers.
- **Spam Control**: 50 questions daily limit per user and 30-second answer timer.
- **Leaderboards**: Persistent database-driven local server and global cross-server leaderboards.

### 🛡️ Safety, Security, & Logging
- **Input Sanitization**: Filters out control characters, Discord custom emojis, and blocks common prompt injection patterns.
- **Access Control**: Role-based access requiring Discord User ID registration in `ADMIN_USER_IDS` for administrative tools.
- **Secure Logging**: Rotating `bot.log` up to 10MB (max 5 backups) with automatic redacting of API keys and bearer tokens.
- **File Permissions**: Automatically enforces owner-only read/write permissions on `bot.log` and the SQLite database.

### ⚙️ Persistent SQLite Database (`bot_usage.db`)
- Tracks user usage and limits (10 requests per 3 minutes).
- Saves user personalities set via command.
- Stores channel cooldown timers and last request timestamps.
- Records trivia scores and completed question IDs to prevent duplicate games.

---

## Command Reference

### Chat & AI Commands (Public)
| Command | Description |
| :--- | :--- |
| **`@DBZClanker <prompt>`** | Mentions the bot to chat with AI. Supports reply context. |
| **`!chat <prompt>`** | Chats using Groq priority models. Supports message reply context. |
| **`!invite`** | Sends a Direct Message to the user containing the bot's invite link. |

### Personalization (Public)
| Command | Description |
| :--- | :--- |
| **`!setpersonality <text>`** | Set a custom personality for your interactions (max 500 characters). |
| **`!removepersonality`** | Resets your custom personality back to default. |
| **`!checkpersonality`** | Shows the custom personality currently set by you. |

### Trivia & Games (Public)
| Command | Description |
| :--- | :--- |
| **`!trivia`** | Starts a general/anime trivia question (limit 50/day). |
| **`!genshin`** | Starts a Genshin Impact trivia question (limit 50/day). |
| **`!leaderboard`** | Displays the server's trivia leaderboard (paginated). |
| **`!leaderboardglobal`** | Displays the global trivia leaderboard (paginated). |

### Administration Commands (Admin Only)
| Command | Description |
| :--- | :--- |
| **`!servers`** | Lists all Discord servers the bot is currently connected to. |
| **`!check`** | Reply to a bot message to check which model and API key slot generated it. |
| **`!model [model_name] [prompt]`** | Force use a specific Groq model or list all available Groq priority models. |
| **`!status <text>`** | Sets the bot's Discord status (e.g. "Playing with GPT-4"). |
| **`!setcooldown <minutes>`** | Sets channel-specific user cooldown in minutes (0 to remove). |
| **`!delete`** | Reply to a bot message to delete it and remove your trigger message. |
| **`!setpersonalityadmin @user <personality>`** | Sets custom personality for another user (Owner Only). |
| **`!checkpersonalityadmin @user`** | Checks custom personality of another user (Owner Only). |

### Debugging Commands (Admin Only)
| Command | Description |
| :--- | :--- |
| **`!test`** | Checks if command processing is functioning. |
| **`!checkinput <prompt>`** | Shows the exact system prompt and message array structure sent to the API. |
| **`!apicheck [prompt]`** | Tests all Groq API keys with `gemma2-9b-it` and outputs status. |

---

## AI Model Hierarchy (Groq Models)

The bot rotates through these Groq models in priority order:

1. `openai/gpt-oss-120b` (Reasoning effort: medium)
2. `deepseek-r1-distill-llama-70b` (Thinking model)
3. `llama-3.3-70b-versatile`
4. `moonshotai/kimi-k2-instruct`
5. `qwen/qwen3-32b` (Thinking model)
6. `meta-llama/llama-4-maverick-17b-128e-instruct`
7. `meta-llama/llama-4-scout-17b-16e-instruct`
8. `openai/gpt-oss-20b` (Reasoning effort: medium)
9. `gemma2-9b-it`
10. `llama-3.1-8b-instant`

---

## Setup Instructions

### 1. Requirements & Prerequisites
Ensure you have **Python 3.8+** installed.

Install the core dependencies:
```bash
pip install -r requirements.txt
```
*(Dependencies: `discord.py`, `aiohttp`, `python-dotenv`, `google-genai`, `Pillow`, `requests`)*

### 2. Environment Configuration
Create a `.env` file in the root directory. Copy the structure from [.env.example](file:///h:/Github%20Repositories/llmbot/.env.example) and populate it with your keys:

```env
DISCORD_TOKEN=your_discord_bot_token_here
ADMIN_USER_IDS=your_discord_user_id_here,another_id_here

# Groq API Keys (1-16 slots + Main key)
GROQ_API_KEY=your_main_key
GROQ_API_KEY_1=your_key
...
```

### 3. Running the Bot
You can start the bot using the command line:
```bash
python llmbot.py
```
Or use the provided batch script on Windows:
```cmd
run.bat
```

---

## Configuration & Limits

- **Rate Limits**: Users are limited to 10 requests per 3 minutes (180 seconds) by default. Channels can have a custom cooldown set via `!setcooldown`.
- **Character Limits**: Input messages are capped at 2,000 characters. Responses are set to a 1,000-character target limit in the system prompt. If the generated text exceeds 2,000 characters, the bot automatically splits the message and replies sequentially to respect Discord's limits.
- **Trivia Limit**: Users can play up to 50 trivia/genshin questions per day. Cooldown check and scores are tracked persistently across restarts.