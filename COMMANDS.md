# DBZClanker AI Bot Commands & Features

## User Commands

### AI Conversation (Uses Groq Priority Fallback Hierarchy)
- **`@DBZClanker <message>`** - Mention the bot to start a conversation (uses roasting personality by default)
- **Reply + Mention** - Reply to any message while mentioning the bot for context-aware responses
- **`!ai <prompt>`** - Direct AI conversation command (uses Groq models)
- **`!oss <prompt>`** - Direct AI conversation using Groq models fallback hierarchy with reply context
- **`!invite`** - Sends a Direct Message to the user containing the bot's invite link

### Personalization
- **`!setpersonality <description>`** - Set a custom personality for your interactions (max 500 chars)
- **`!removepersonality`** - Remove your custom personality and use default

### Trivia & Games
- **`!trivia`** - Play trivia games (50 questions/day)
- **`!genshin`** - Genshin Impact trivia
- **`!leaderboard`** - Server trivia leaderboard
- **`!leaderboardglobal`** - Global trivia leaderboard

## Admin Commands

### Server Management
- **`!servers`** - List all servers the bot is connected to
- **`!status <status_text>`** - Set the bot's Discord status message
- **`!delete`** - Reply to a bot message to delete it (and remove your command message)

### AI Model Testing & Debugging
- **`!check`** - Reply to a bot message to see which model generated it
- **`!model [model_name] [question]`** - Force use a specific model or list available models
- **`!apicheck [test_prompt]`** - Test all Groq API keys with gemma2 model
- **`!checkinput <prompt>`** - Show exact message structure sent to API
- **`!test`** - Simple functionality test command

### Channel Management
- **`!setcooldown <minutes>`** - Set per-user cooldown for current channel (0 to remove)

## Available AI Models (Priority Order)

1. `openai/gpt-oss-120b` - *Reasoning enabled*
2. `deepseek-r1-distill-llama-70b` - *Thinking model*
3. `llama-3.3-70b-versatile`
4. `moonshotai/kimi-k2-instruct`
5. `qwen/qwen3-32b` - *Thinking model*
6. `meta-llama/llama-4-maverick-17b-128e-instruct`
7. `meta-llama/llama-4-scout-17b-16e-instruct`
8. `openai/gpt-oss-20b` - *Reasoning enabled*
9. `gemma2-9b-it`
10. `llama-3.1-8b-instant`

## Features

### Smart Conversation
- **Roast Personality** - Built-in unhinged and uncensored roasting personality (customizable with `!setpersonality`)
- **Context Awareness** - Handles reply-to-message conversations
- **One-Word Detection** - Asks for clarification on single-word replies
- **Thinking Models** - Shows "🤔 Thinking..." for reasoning models
- **Streaming Responses** - Real-time response updates
- **Anti-Repetition** - Encourages original responses

### Safety & Limits
- **Rate Limiting** - 10 requests per 3 minutes per user
- **Input Sanitization** - Removes harmful characters and prompt injection attempts
- **Character Limits** - 2000 char input, 1000 char responses (auto-splits longer ones)
- **Channel Cooldowns** - Admin-configurable per-channel user cooldowns

### Database Tracking
- **Usage Monitoring** - Tracks API requests and tokens per model/key
- **Message History** - Stores bot message metadata for admin review
- **Persistent Settings** - Cooldowns, personalities, and scores survive restarts

## Required Environment Variables

```env
# Discord
DISCORD_TOKEN=your_discord_bot_token
ADMIN_USER_IDS=comma_separated_user_ids

# Groq API (keys 11-17)
GROQ_API_KEY=your_primary_key  # becomes key 17
GROQ_API_KEY_11=key_11
GROQ_API_KEY_12=key_12
# ... keys 13-16
```