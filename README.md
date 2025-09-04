# Incident Summary Bot

A Flask webhook server for a Slack bot that processes incident summaries.

## Project Structure

```
incident-summary-bot/
├── main.py              # Flask server with Slack webhook endpoint
├── requirements.txt     # Python dependencies
├── vercel.json         # Vercel deployment configuration
└── README.md           # Project documentation
```

## Setup

### Environment Variables

Set the following environment variables:

- `SLACK_BOT_TOKEN` - Your Slack bot token
- `LANGDOCK_API_KEY` - Your LangDock API key
- `LANGDOCK_ASSISTANT_ID` - Your LangDock assistant ID

### Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set environment variables:
   ```bash
   export SLACK_BOT_TOKEN=your_slack_bot_token
   export LANGDOCK_API_KEY=your_langdock_api_key
   export LANGDOCK_ASSISTANT_ID=your_langdock_assistant_id
   ```

3. Run the server:
   ```bash
   python main.py
   ```

The server will start on `http://localhost:5000`

## Endpoints

- `GET /` - Health check endpoint
- `POST /api/slack/commands` - Handles Slack slash commands

## Deployment

This project is configured for deployment on Vercel. The `vercel.json` file contains the necessary configuration for Python serverless functions.

To deploy:
1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel`
3. Set environment variables in your Vercel dashboard
