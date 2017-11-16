import asyncio
import discord
from discord.ext import commands
import re
import random
import os
import time
from random import shuffle
#from mutagen.mp3 import MP3
bot = commands.Bot(command_prefix=['µsic ','music ','Music '], description='Nico Nico Nii~')
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
@asyncio.coroutine
def playing():
	global current
	yield from bot.say(current)

@bot.command()
@asyncio.coroutine
def sleep(*,sleepytime):
	global voice
	global sleep
	sleep=int(sleepytime)
	yield from bot.say("Nico is going to take a quick nap, the #1 Idol in the Universe will be back in {} seconds!".format(sleep))
	#time.sleep(30)
	#play()
	
	#ch=bot.get_channel('254596398853521409')
	#voice2 = yield from bot.join_voice_channel(ch)
	#voice=voice2
	#play (voice2,shuff())

# @bot.command()
# @asyncio.coroutine
# def wake():
	# yield from bot.say("Why did you wake Nico up from her nap? Nico still loves you!")
	# global sleep
	# sleep=0
@asyncio.coroutine
def play():
	yield from bot.wait_until_ready()
	global voice
	global sleep
	sleep = 0
	ch=bot.get_channel('254596398853521409')
	voice = yield from bot.join_voice_channel(ch)
	songs=shuff()
	current=songs.pop(0)
	player=voice.create_ffmpeg_player("./music/"+current,options="-q:a 9")
	yield from bot.change_presence(game=discord.Game(type=2,name=current))
	player.start()
	while True:
		
		if sleep!=0:
			print ("about to sleep\n")
			player.stop()
			yield from voice.disconnect()
			yield from asyncio.sleep (sleep)
			sleep = 0
			voice=yield from bot.join_voice_channel(ch)
			if len(songs)<1:
				songs=shuff()
			current=songs.pop(0)
			yield from bot.change_presence(game=discord.Game(type=2,name=current))
			player=voice.create_ffmpeg_player("./music/"+current,options="-q:a 9")
			player.start()
		elif player.is_playing():
			yield from asyncio.sleep(5)
		else:
			if len(songs)<1:
				songs=shuff()
			current=songs.pop(0)
			yield from bot.change_presence(game=discord.Game(type=2,name=current))
			player=voice.create_ffmpeg_player("./music/"+current,options="-q:a 9")
			player.start()
		
	


def shuff():
	songList=os.listdir("./music")
	shuffle(songList)
	return songList
	
	
	


@bot.command(pass_context=True)
@asyncio.coroutine
def start(self):
	global voice
	
	ch=bot.get_channel('254596398853521409')
	voice = yield from bot.join_voice_channel(ch)
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
	songs=shuff()
	current=songs.pop(0)
	player=voice.create_ffmpeg_player("./music/"+current,options="-q:a 9")
	yield from bot.change_presence(game=discord.Game(type=0,name=current))
	player.start()
	while True:
		
		if player.is_playing():
			time.sleep(5)
		else:
			if len(songs)<1:
				songs=shuff()
			current=songs.pop(0)
			yield from bot.change_presence(game=discord.Game(type=0,name=current))
			player=voice.create_ffmpeg_player("./music/"+current,options="-q:a 8")
			player.start()
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
		
		
bot.loop.create_task(play())
bot.run('Mzc2OTI4ODU5NDYwODYxOTUy.DOFh5g.3-2968B9V5LATvzRwn7W8tE-mBc')
