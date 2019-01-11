TOKEN = '################'

import discord, random

client = discord.Client()

phrases = ['Light Yummy Yummy', 'I AM THE KEEPER OF THE LIGHT' , 'PRAISE THE SUN', 'N U T',
            "OHHHHH, I'M PHOTOSYNTHESIZINGGGGGG", 'LOAD SIZE: EXTRA LARGE', 'THE LIGHT HAS SPOKEN',
            'I can see it... the light...', 'Man, I just love me some ***LIGHT***',
            'Did someone say **light**']


defaultWords = {'light', 'lit', 'bright', 'sun', 'beam', 'photosynthesis', 'flash', 'fire', 'glow', 'radiant', 'vivid',
                'bald', 'shine', 'shiny', 'pineapple', 'apollo', 'brilliant', 'arson', 'hell', 'shimmer', 'god'}

addedWords = {}

bannedWords = ["gopi", "darren", "david", "josh",]

deathPhrases ={'IM MELTING, MELTING', 'i always wanted to die', 'well this is the end for me', 'sweet death, how i longed for thee'}

global checkForMessage
checkForMessage = True
global pollingUsers
pollingUsers = False

@client.event
async def on_message(message):
    global checkForMessage

    # we do not want the bot to reply to itself
    if (message.author.bot): return

    if message.content == '!stop' 
        mAuthor = message.mAuthor
        await client.send_message(message.channel, random.choice(deathPhrases))
        await client.logout()
        
    #Polling
    if message.content == '!mothbot poll'
        yays = 0
        nays = 0
        mAuthor - message.author
        checkForMessage = False
        await client.send_message(message.channel, "What is your question?")
        pollingUsers = True 
        response = await client.wait_for_message()
        question = response
        while pollingUsers or response.content.isspace() or not response.contentor or (response.author != mAuthor) or response.author.bot or response.content.lower() in bannedWords:
            await client.send_message(message.channel, "no")
            response = await client.wait_for_message()
        
        question = response
        await client.send_message(message.channel, f'starting poll for f {question.content}')
        
        answers = await client.wait_for_message()
        while answers.content.isspace() or not answers.content or answers.author.bot or answers.content.lower() in bannedWords or pollingUsers
            if(answers.content.lower() == "yay")
                yays += 1
            if(answers.content.lower() == "nay")
                nays += 1
            if(answers.content.lower() == '!mothbot stop poll')                
                await client.send_message(f"And the results for {question} are in...")
                await client.send_message(f"Yays: {yays}  --- Nays{nays}")
                pollingUsers = False
                checkForMessage = True
            answers = await client.wait_for_message()
        checkForMessage = True


    #random phrases 
    if not message.author.bot and checkForMessage:
        for word in defaultWords:
            if word in message.content.lower():
                msg = random.choice(phrases)
                await client.send_message(message.channel, msg)
        if(addedWords):
            for word in addedWords.keys():
                if word in message.content.lower():
                    msg = addedWords[word]
                    await client.send_message(message.channel, msg)
    
    #adds phrases 
    if message.content == '!mothbot add':
        mAuthor = message.author
        checkForMessage = False
        await client.send_message(message.channel, "What light-related word would you like to add?")
        response = await client.wait_for_message()
        while response.content.isspace() or not response.content or response.author.bot or (response.author != mAuthor) or response.content.lower() in bannedWords:
            await client.send_message(message.channel, "Negatory, ghost rider. Try again.")
            response = await client.wait_for_message()
        response = response.content.lower()
        await client.send_message(message.channel, f"What should the response to {response} be?")
        newPhrase = await client.wait_for_message()
        while newPhrase.content.isspace() or not newPhrase.content or newPhrase.author.bot or (newPhrase.author != mAuthor) or newPhrase.content.lower() in bannedWords:
            await client.send_message(message.channel, "Negatory, ghost rider. Try again.")
            newPhrase = await client.wait_for_message()
        newPhrase = newPhrase.content
        await client.send_message(message.channel, f"Adding {newPhrase} as the response to {response}.")
        addedWords[response] = newPhrase
        checkForMessage = True


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
