# DBZClanker AI Bot Commands & Features

## User Commands

### AI Conversation (Uses OpenRouter Mistral → Groq Fallback)
- **`@DBZClanker <message>`** - Mention the bot to start a conversation
- **Reply + Mention** - Reply to any message while mentioning the bot for context-aware responses
- **`!ai <prompt>`** - Direct AI conversation command

### Personalization
- **`!setpersonality <description>`** - Set a custom personality for your interactions (max 500 chars)
- **`!removepersonality`** - Remove your custom personality and use default

## Admin Commands

### Server Management
- **`!servers`** - List all servers the bot is connected to
- **`!status <status_text>`** - Set the bot's Discord status message

### AI Model Testing
- **`!check`** - Reply to a bot message to see which model generated it
- **`!model [model_name] [question]`** - Force use a specific model or list available models
- **`!apicheck [test_prompt]`** - Test all Groq API keys with gemma2 model
- **`!geminicheck`** - Test all Gemini API keys
- **`!mistralapicheck [test_prompt]`** - Test all OpenRouter API keys

### Alternative AI Services
- **`!gemini <prompt>`** - Use Google Gemini with web search (1min cooldown, reply context supported)
- **`!mistral <prompt>`** - Use Mistral via OpenRouter API
- **`!image <prompt>`** - Generate images with Gemini (3min cooldown, supports input images)

### Channel Management
- **`!setcooldown <minutes>`** - Set per-user cooldown for current channel (0 to remove)

### Debugging
- **`!checkinput <prompt>`** - Show exact message structure sent to API

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

### Special Cooldowns
- **Gemini** - 1 minute global cooldown (admins exempt)
- **Image Generation** - 3 minutes global cooldown (admins exempt)
- **Channel-Specific** - Configurable per-channel cooldowns

### Database Tracking
- **Usage Monitoring** - Tracks API requests and tokens per model/key
- **Message History** - Stores bot message metadata for admin review
- **Persistent Settings** - Cooldowns and user data survive restarts

## Primary AI Service Priority

1. **OpenRouter Mistral** (Primary) - Uses `cognitivecomputations/dolphin-mistral-24b-venice-edition:free`
2. **Groq Models** (Fallback) - Uses model hierarchy if OpenRouter fails

## Required Environment Variables

```env
# Discord
DISCORD_TOKEN=your_discord_bot_token
ADMIN_USER_IDS=comma_separated_user_ids

# OpenRouter API (keys 1-15, PRIMARY for main AI features)
OPENROUTER_API_KEY_1=key_1
OPENROUTER_API_KEY_2=key_2
# ... keys 3-15

# Groq API (keys 11-17, FALLBACK)
GROQ_API_KEY=your_primary_key  # becomes key 17
GROQ_API_KEY_11=key_11
GROQ_API_KEY_12=key_12
# ... keys 13-16

# Gemini API (keys 1-13, for !gemini and !image commands)
GEMINI_API_KEY=main_gemini_key
GEMINI_API_KEY_1=key_1
# ... keys 2-13
```

## Notes
- **Primary AI Service**: OpenRouter Mistral is tried first for main conversation features
- **Fallback System**: If all OpenRouter keys fail, automatically falls back to Groq model hierarchy
- **Error Handling**: All errors are logged to console, users see generic error messages
- Admin commands require your Discord user ID in `ADMIN_USER_IDS`
- Thinking models show reasoning process before final response
- Image generation supports both text prompts and input images
- All responses respect Discord's 2000 character limit with auto-splitting