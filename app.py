from flask import Flask, request, jsonify
import data
import discord
import asyncio
import json

app = Flask(__name__)
client = discord.Client()

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/spotlight', methods=['POST'])
def return_spotlight():
    if request.method == 'POST':
        payload = request.json
        print('payload', payload)
        data.update_spotlight(payload)
    return jsonify({'Success': True})

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!spotlight'):
        await client.send_message(message.channel, data.post_spotlight_to_discord())


client.run('NTIyMjE3MzQ1NjE2MTgzMjk2.DvHwtQ.Nyp2j7hcZhTc2D6ZafFc-6ss6is')
