import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random



banner = '''
  _____  _   _ _____  ______ ______ ______
 |  __ \| \ | |  __ \|  ____|  ____|___  /
 | |  | |  \| | |  | | |__  | |__     / / 
 | |  | | . ` | |  | |  __| |  __|   / /  
 | |__| | |\  | |__| | |____| |____ / /__ 
 |_____/|_| \_|_____/|______|______/_____|    
                                          

'''

client = discord.Client()
client = commands.Bot(command_prefix = ["~"])  #command prefix, but is not used in this
bot_token = 'OTc2MDI1OTM2MDQ4ODM2NjM4.GE5ygR.tt6r61OKGKOf9bYdds-ybiybohpci6yPF9Os94' #bot token

print(banner)
print()
print('made by xGrqnd')
print()

chatlog = open("./logs/message_log.txt", "a") # opening chat log before loops to advoid large RAM usage
errorlog = open("./logs/exception_log.txt", "a")


@client.event
async def on_ready():
print("Bot is ready!")
print("Logged in as: " + client.user.name)
print("Bot ID: " + str(client.user.id))
for guild in client.guilds:
    print ("Connected to server: {}".format(guild))
    print("---------------------------------------")
    print()
    print("INVITES TO ALL SERVERS:")
    print()
    invites = []
    for guild in client.guilds:
        for c in guild.text_channels:
            if c.permissions_for(guild.me).create_instant_invite:
                invite = await c.create_invite()
                invites.append(invite)
                print(guild)
                print(invite)
                print()
                game = discord.Game("dndeez with xGrqnd") #what the bot is playing
                await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    guild = str(message.guild)    #setting variables
    content = str(message.content)
    author = str(message.author)
    time = str(message.created_at)
    channel = str(message.channel)
    link = str(message.jump_url)


    chatlog.write(time + " " + guild + " " + channel + " " author + ": " + content)
    
    x = content.split()     #splitting the message content into the different words and putting it into a list
    command = x[0]      #extracting the first string from the list
    commandcontent = x[1] #extracing the content from after the command
    
    if command = '~roll': #checking if the commad is equal to ~roll
        split = int(commandcontent.find('d'))  #finding the location of the 'd' in the content. e.g.3d4, which means we can support multiple digits
        
        try:
            split2 = int(commandcontent.find('+'))
        except:
            await message.channel.send("Bozo needs to add a '+', even if it's a +0")
            errorlog.write("Failed to execute a dice roll for " + author + " fail id = FAIL:+NOTFOUND " + link + "\n")


        if split == 2:
            numofrolls = commandcontent[0]

            
            if split2 - split == 2: # a one digit dice number
                dice = commandcontent[split + 1]
                
            if split2 - split == 3: # a two digit dice number
                dice = (commandcontent[split + 1] + commandcontent[split + 2])

            else: # catch exception
                await channel.send("Bozo stop being greedy, you don't need to roll a number bigger than 100")
                errorlog.write("Failed to execute a dice roll for " + author + " failid = FAIL:GREEDYSHITTER " + link + "\n")
                

        if split == 3:
            numofrolls = (commandcontent[0] + commandcontent[1])

            if split2 - split == 2: # a one digit dice number
                dice = commandcontent[split + 1]
                
            if split2 - split == 3: # a two digit dice number
                dice = (commandcontent[split + 1] + commandcontent[split + 2])

            else: #catch exception
                await channel.send("Bozo stop being greedy, you don't need to roll a number bigger than 100")
                errorlog.write("Failed to execute a dice roll for " + author + " failid = FAIL:GREEDYSHITTER " + link + "\n")
                

        if split == 4:
            numofrolls = (commandcontent[0] + commandcontent[1] + commandcontent[2])
            
            if split2 - split == 2: # a one digit dice number
                dice = commandcontent[split + 1]
                
            if split2 - split == 3: # a two digit dice number
                dice = (commandcontent[split + 1] + commandcontent[split + 2])

            else: #catch exception
                await channel.send("Bozo stop being greedy, you don't need to roll a number bigger than 100")
                errorlog.write("Failed to execute a dice roll for " + author + " failid = FAIL:GREEDYSHITTER " + link + "\n")
        else:
            await message.channel.send("Bozo got too chunky of a nuber or can't spell ^-^")
            errorlog.write("Failed to execute a dice roll for " + author + " failid = FAIL:CATCHEXCEPTION " + link + "\n")

        #rolling the dice
        await channel.send("Rolling " + numofrolls + "d" + dice + " dice")
                           
        diceloop = 1
        output = 1
        while diceloop < numofrolls:
            output = output + random.randint(1, int(dice))
            diceloop = diceloop + 1
            
        await channel.send(output)











client.run(bot_token) #loggin in to the bot MUST BE AT THE END
