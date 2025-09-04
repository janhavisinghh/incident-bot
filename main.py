import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK', 'message': 'Incident Summary Bot is running'})

@app.route('/api/slack/commands', methods=['POST'])
def handle_slack_command():
    try:
        slack_data = request.form.to_dict()
        channel_id = slack_data.get('channel_id')
        
        return jsonify({
            'response_type': 'in_channel',
            'text': f'Test response received! Channel ID: {channel_id}'
        })
    
    except Exception as e:
        return jsonify({
            'response_type': 'ephemeral',
            'text': f'Error processing command: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
    