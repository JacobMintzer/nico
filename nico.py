import asyncio
import discord
from discord.ext import commands
import re
import random
import os
import time
from random import shuffle
#from mutagen.mp3 import MP3
bot = commands.Bot(command_prefix=['µsic ','music '], description='Nico Nico Nii~')
if not discord.opus.is_loaded():
	# the 'opus' library here is opus.dll on windows
	# or libopus.so on linux in the current directory
	# you should replace this with the location the
	# opus library is located in and with the proper filename.
	# note that on windows this DLL is automatically provided for you
	discord.opus.load_opus('opus')

#bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), description='A playlist example for discord.py')
#bot.add_cog(Music(bot))

@bot.event
@asyncio.coroutine 
def on_ready():
	print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))
	#ch=bot.get_channel('254596398853521409')
	#voice = bot.join_voice_channel(ch)
	#play(voice,shuff())

@bot.command()
async def playing():
	global current
	await bot.say(current)

@bot.command()
async def restart():
	global voice
	await voice.disconnect()
	ch=bot.get_channel('254596398853521409')
	voice2 = await bot.join_voice_channel(ch)
	voice=voice2
	play (voice2,shuff())

def play(voice,songs):
	global current
	if len(songs)<1:
		songs=shuff()
	current= songs.pop(0)
	bot.change_presence(game=discord.Game(type=0,name=current))
	player = voice.create_ffmpeg_player("./music/"+current,after=lambda:play(voice,songs))
	player.start()
	


def shuff():
	songList=os.listdir("./music")
	shuffle(songList)
	return songList

@bot.command(pass_context=True)
async def start(self):
	global voice
	ch=bot.get_channel('254596398853521409')
	voice = await bot.join_voice_channel(ch)
        #current=random.choice(os.listdir("./music/"))
        #player = voice.create_ffmpeg_player("./music/"+current)
        #bot.change_presence(game=discord.Game(type=0,name=current))
        #player.start()
        #audio=MP3('./music/'+current)
        #time.sleep(audio.info.length)
        #while True:
                #current= random.choice(os.listdir("./music"))
                #audio=MP3('./music/'+current)
	play(voice,shuff())
                #print (audio.info.length)
                #time.sleep(audio.info.length)	ch=bot.get_channel('254596398853521409')
	#current=random.choice(os.listdir("./music/"))
	#player = voice.create_ffmpeg_player("./music/"+current)
	#bot.change_presence(game=discord.Game(type=0,name=current))
	#player.start()
	#audio=MP3('./music/'+current)
	#time.sleep(audio.info.length)
	#while True:
		#current= random.choice(os.listdir("./music"))
		#audio=MP3('./music/'+current)
	#play(voice,shuff())
		#print (audio.info.length)
		#time.sleep(audio.info.length)
		
		

bot.run('Mzc2OTI4ODU5NDYwODYxOTUy.DOFh5g.3-2968B9V5LATvzRwn7W8tE-mBc')
