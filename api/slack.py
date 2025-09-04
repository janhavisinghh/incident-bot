from flask import Flask, request, jsonify
import json
import urllib.parse

def handler(req):
    """Vercel serverless handler"""
    if req.method == 'GET':
        return 'Incident Summary Bot is running!'
    
    if req.method == 'POST':
        # Parse the form data from Slack
        body = req.get_data(as_text=True)
        form_data = urllib.parse.parse_qs(body)
        
        # Extract channel_id (it comes as a list, so take first item)
        channel_id = form_data.get('channel_id', ['unknown'])[0]
        
        response = {
            "response_type": "in_channel",
            "text": f"✅ Bot working! Processing channel: {channel_id}"
        }
        
        return json.dumps(response), 200, {'Content-Type': 'application/json'}
    
    return 'Method not allowed', 405
