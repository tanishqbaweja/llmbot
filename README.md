# DBZClanker AI Discord Bot

A Discord bot powered by multiple AI models through the Groq API, featuring intelligent conversation, rate limiting, and admin controls.

## Features

### 🤖 AI Conversation
- **Multiple Model Support**: Automatically tries models in priority order for best availability
- **Smart Fallback**: If one model fails, automatically tries the next available model
- **Streaming Responses**: Real-time response updates as the AI generates text
- **Context Awareness**: Handles reply-to-message conversations with context

### 🛡️ Safety & Security
- **Input Sanitization**: Removes harmful characters and prevents prompt injection
- **Rate Limiting**: Per-user request limits to prevent spam
- **Secure Database**: Encrypted API key storage and usage tracking
- **Admin Controls**: Restricted access to sensitive commands

### 📊 Usage Tracking
- **API Usage Monitoring**: Tracks requests and tokens per model and API key
- **Rate Limit Compliance**: Respects Groq API limits automatically
- **Message History**: Stores bot message metadata for admin review

### 🎯 Smart Features
- **One-Word Reply Detection**: Asks for clarification on single-word replies to bot messages
- **Thinking Models Support**: Shows "🤔 Thinking..." for reasoning models, then streams actual response
- **Emoji Filtering**: Removes Discord custom emojis from input
- **Character Limits**: Enforces response length limits for better readability
- **Anti-Repetition**: Encourages original responses instead of echoing user input
- **Dynamic Status**: Admin can set custom bot status messages

### 🎤 Voice Chat
- **Native Audio Support**: Uses Gemini 2.5 Flash Native Audio for natural voice conversations
- **Real-time Processing**: Streams audio input/output with minimal latency
- **Auto-disconnect**: Leaves voice channel after 3 minutes of inactivity
- **Memory Retention**: Maintains conversation context throughout voice session
- **Audio Format Conversion**: Automatically converts Discord audio to Gemini-compatible format

## Commands

### User Commands
- **`@DBZClanker <message>`** - Mention the bot to start a conversation
- **Reply + Mention** - Reply to any message while mentioning the bot for context-aware responses
- **`!voice`** - Join your voice channel and start a voice conversation
- **`!leave`** - Leave the current voice channel

### Admin Commands
- **`!servers`** - List all servers the bot is connected to
- **`!check`** - Reply to a bot message to see which model generated it
- **`!model [model_name] [question]`** - Force use a specific model or list available models
- **`!status <status_text>`** - Set the bot's Discord status (e.g., "Now using GPT-5 Mini...")
- **`!setcooldown <minutes>`** - Set per-user cooldown for the current channel (0 to remove)
- **`!checkinput <prompt>`** - Show the exact final message structure sent to the API (for debugging)
- **`!apicheck [test_prompt]`** - Test all API keys with gemma2 model and show which ones work/fail

## Available Models

1. `openai/gpt-oss-120b` (Primary) - *Reasoning enabled*
2. `deepseek-r1-distill-llama-70b` - *Thinking model with 1000 token limit*
3. `llama-3.3-70b-versatile`
4. `moonshotai/kimi-k2-instruct`
5. `qwen/qwen3-32b` - *Thinking model with 1000 token limit*
6. `meta-llama/llama-4-maverick-17b-128e-instruct`
7. `meta-llama/llama-4-scout-17b-16e-instruct`
8. `openai/gpt-oss-20b` - *Reasoning enabled*
9. `gemma2-9b-it` - *Used for API testing*
10. `llama-3.1-8b-instant`

## Setup Instructions

### 1. Discord Bot Setup

1. **Create a Discord Application**:
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Click "New Application" and give it a name
   - Go to the "Bot" section and click "Add Bot"
   - Copy the bot token (you'll need this later)

2. **Set Bot Permissions**:
   - In the "Bot" section, enable these permissions:
     - Send Messages
     - Read Message History
     - Use Slash Commands
     - Mention Everyone
     - Connect (for voice channels)
     - Speak (for voice channels)
   - In the "OAuth2" > "URL Generator":
     - Select "bot" scope
     - Select the same permissions as above
     - Copy the generated URL

3. **Invite Bot to Server**:
   - Use the generated URL to invite the bot to your Discord server
   - Make sure you have "Manage Server" permission

### 2. Groq API Setup

1. **Get Groq API Keys**:
   - Sign up at [Groq Console](https://console.groq.com/)
   - Generate API keys (you can use multiple keys for better rate limits)
   - Copy your API key(s)

### 3. Environment Setup

1. **Clone/Download the Bot**:
   ```bash
   git clone <repository-url>
   cd llmbot
   ```

2. **Install Dependencies**:
   ```bash
   pip install discord.py aiohttp python-dotenv
   ```
   
   **For Voice Chat Feature** (optional):
   ```bash
   pip install PyNaCl websockets google-generativeai
   ```
   
   **Install FFmpeg** (required for voice):
   - **Windows**: Download from [FFmpeg website](https://ffmpeg.org/download.html) and add to PATH
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt update && sudo apt install ffmpeg`

3. **Create Environment File**:
   - Create a `.env` file in the bot directory
   - Add your credentials:
   ```env
   DISCORD_TOKEN=your_discord_bot_token_here
   ADMIN_USER_IDS=your_discord_user_id_here
   
   # Groq API Keys (keys 11-17 are used)
   GROQ_API_KEY=your_primary_groq_api_key  # This becomes key 17
   GROQ_API_KEY_11=your_additional_key_1
   GROQ_API_KEY_12=your_additional_key_2
   # ... add keys 13-16 as needed
   
   # Gemini API Keys (for voice chat and image generation)
   GEMINI_API_KEY=your_gemini_api_key
   GEMINI_API_KEY_1=your_additional_gemini_key_1
   # ... add more Gemini keys as needed
   ```

4. **Find Your Discord User ID**:
   - Enable Developer Mode in Discord (Settings > Advanced > Developer Mode)
   - Right-click your username and select "Copy ID"
   - Use this ID in the `ADMIN_USER_IDS` field

### 4. Running the Bot

1. **Start the Bot**:
   ```bash
   python llmbot.py
   ```

2. **Verify Connection**:
   - You should see "DBZClanker has connected to Discord!" in the console
   - The bot should appear online in your Discord server

### 5. Testing

1. **Mention Test**:
   - Type `@DBZClanker What's the weather like?`
   - The bot should respond to your mention

2. **Reply Test**:
   - Reply to any message while mentioning `@DBZClanker`
   - The bot should respond with context awareness

3. **Admin Test** (if you're an admin):
   - Type `!servers` to see server list
   - Type `!model` to see available models
   - Type `!status Now using advanced AI` to set bot status
   - Type `!setcooldown 3` to set a 3-minute cooldown
   - Type `!apicheck` to test all API keys

4. **Voice Chat Test**:
   - Join a voice channel in your Discord server
   - Type `!voice` to have the bot join and start voice conversation
   - Speak to the bot and it will respond with voice
   - Type `!leave` to disconnect the bot from voice
   - Bot will auto-disconnect after 3 minutes of silence

## Configuration

### Rate Limits
- **User Limit**: 10 requests per 3 minutes per user
- **API Limits**: Automatically managed per Groq's specifications
- **Input Limit**: 2000 characters maximum per message

### Response Limits
- **Character Limit**: 1000 characters (configurable in system prompt)
- **Discord Limit**: 2000 characters per message (auto-splits longer responses)

### Working API Keys
The bot is configured to use API keys 11-17. Update the key numbers in the code if you're using different key slots.

### Channel Cooldowns
- **Per-Channel Control**: Admins can set cooldowns per channel using `!setcooldown <minutes>`
- **Per-User Enforcement**: Each user has their own cooldown timer in each channel
- **Persistent Settings**: Cooldown settings and user timestamps survive bot restarts
- **Silent Ignore**: Messages sent during cooldown are silently ignored (no response, no API usage)
- **No Default Cooldown**: Channels have no cooldown unless explicitly set by an admin

### Special Model Features
- **Reasoning Models**: GPT-OSS models use `reasoning_effort: medium` parameter
- **Thinking Models**: DeepSeek R1 and Qwen models show thinking process and have 1000 token limits
- **API Testing**: Use `!apicheck` to test all API keys with gemma2 model

## Troubleshooting

### Common Issues

1. **Bot Not Responding**:
   - Check if bot has permission to read/send messages in the channel
   - Verify the bot token is correct in `.env`
   - Check console for error messages

2. **API Errors**:
   - Verify Groq API keys are valid and have credits
   - Check if you've hit rate limits
   - Ensure API keys are in the correct environment variables

3. **Permission Errors**:
   - Make sure your Discord user ID is in `ADMIN_USER_IDS`
   - Verify bot has necessary Discord permissions

4. **Database Issues**:
   - The bot creates `bot_usage.db` automatically
   - If corrupted, delete the file and restart the bot

5. **Voice Chat Issues**:
   - Ensure FFmpeg is installed and in your system PATH
   - Check that bot has "Connect" and "Speak" permissions in voice channels
   - Verify Gemini API keys are valid and have credits
   - Make sure you're in a voice channel before using `!voice`
   - If audio quality is poor, check your microphone settings

### Support

For issues or questions:
1. Check the console output for error messages
2. Verify all environment variables are set correctly
3. Ensure Discord and Groq API credentials are valid
4. Check that the bot has proper permissions in Discord

## License

This project is for educational and personal use. Please respect Groq's API terms of service and Discord's developer terms.