from flask import Flask, request, jsonify
import requests
import os
import json

app = Flask(__name__)

SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
LANGDOCK_API_KEY = os.environ.get('LANGDOCK_API_KEY')
LANGDOCK_ASSISTANT_ID = os.environ.get('LANGDOCK_ASSISTANT_ID')

def handler(event, context):
    """Vercel serverless handler"""
    if event['httpMethod'] == 'POST':
        # Parse form data from Slack
        form_data = parse_form_data(event['body'])
        channel_id = form_data.get('channel_id', 'unknown')
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                "response_type": "in_channel",
                "text": f"✅ Bot working! Processing channel: {channel_id}"
            })
        }
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/plain'},
        'body': 'Incident Summary Bot is running!'
    }

def parse_form_data(body):
    """Parse URL-encoded form data from Slack"""
    pairs = body.split('&')
    data = {}
    for pair in pairs:
        if '=' in pair:
            key, value = pair.split('=', 1)
            data[key] = value.replace('+', ' ')
    return data
