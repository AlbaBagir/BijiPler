import discord
import os
import random
import asyncio
import time
from discord import FFmpegPCMAudio
from online import online
from discord.ext import commands




client = commands.Bot(command_prefix=["biji ", "Biji ", "Pler ", "pler ","+"])

#removed the default discord.py help command
client.remove_command("help")


#list of javanesse cuss words
pisuhan = ["JANCUK!!","GOBLOK!!","KOMUNIS!!","ASU KOE!","BADJINGAN KOE!","LONTE!!","JEMBUOTI!!",]
celukan = ["Opo su","Pie Nyuk", "Lhapo cok"]
respn = ["ndene!", "mbedhil!", "join!", "mlebu kene!", "wani ora?!"]
pisuhan2 = ["TANGANE!!", "UTEKE!!","GOBLOK!", "FAKYU!"]

#list of random short video
emotions = ['https://www.youtube.com/watch?v=av-rLcM5AgY', 'https://www.youtube.com/watch?v=NaHNRDfJVTc','https://www.youtube.com/watch?v=mGac5cQzhII', 'https://www.youtube.com/watch?v=QojMooSYJGk', 'https://www.youtube.com/watch?v=zhf1pIl007o', 'https://www.youtube.com/watch?v=NjAN9CW_YmY', 'https://www.youtube.com/watch?v=LFOMo_vwEzc', 'https://www.youtube.com/watch?v=1jwVfvhQlng', 'https://www.youtube.com/watch?v=h-0UD2L4_fU', 'https://www.youtube.com/watch?v=zBJU9ndpH1Q', 'https://www.youtube.com/watch?v=wFWaLzZnLuk', 'https://www.youtube.com/watch?v=fKum4JmG-ew','https://www.youtube.com/watch?v=0nvR5qOG8nw']

#custom help command
@client.group(invoke_without_command=True)
async def tulung(ctx):
  
  #embed color set to the discord author role color
  em = discord.Embed(title= "Pertulungan", description = "tuliso biji tulung <command>  nek meh dijelaske panjang lebar.", color = ctx.author.color)

  em.add_field(name= "celukan", value = "biji ;Biji ;Pler ;pler ")
  em.add_field(name= "Jasa mengmisuh", value = "pisuhi,cangkemi")
  em.add_field(name= "Fun Stuff", value = "raine, mood, audio")
  
  await ctx.send(embed = em)

@tulung.command()
async def celukan(ctx):

  em = discord.Embed(title = "Celukan", description = "beberapa cara mengundang saya untuk melakukan sesuatu", colot = ctx.author.color)

  em.add_field(name= "celukan ku", value = "biji , Biji , Pler , pler ")
  em.add_field(name= "syntax", value = "akhirane dikei spasi, (biji pisuhi) koyo ngono")

  await ctx.send(embed = em)


@tulung.command()
async def pisuhi(ctx):

  em = discord.Embed(title = "Pisuhi", description = "men koe ra berdosa, koe iso ngengkon aku misuhi wong nggo koe.", color = ctx.author.color)
  
  em.add_field(name = "Carane", value = "celuk pisuhi <njuk ngetag member>")
  
  await ctx.send(embed = em)


@tulung.command()
async def katain(ctx):

  em = discord.Embed(title = "Katain", description = "men koe ra berdosa, koe iso ngengkon aku nyangkemi wong nggo koe.", color = ctx.author.color)
  
  em.add_field(name = "Carane", value = "celuk katain <njuk ngetag member>")
  
  await ctx.send(embed = em)

@tulung.command()
async def raine(ctx):

    em = discord.Embed(title = "Raine", description = "untuk melihat foto profil teman anda.", color = ctx.author.color)

    em.add_field(name = "Carane", value = "celuk raine <njuk ngetag member>")

    await ctx.send(embed = em)

@tulung.command()
async def mood(ctx):

    em = discord.Embed(title = "Mood", description = "random video", color = ctx.author.color)

    em.add_field(name = "Carane", value = "tulis wae +mood")

    await ctx.send(embed = em)

@tulung.command()
async def audio(ctx):

    em = discord.Embed(title = "audio", description = "audio gokil", color = ctx.author.color)

    em.add_field(name = "Carane", value = "tulis wae bii + bantuin/cangkemi/kaget/moan/terang")
    em.add_field(name = "contone", value = "biji kaget")

    await ctx.send(embed = em)

@client.command()
async def raine(ctx, member: discord.Member=None):
  if member == None:
    member = ctx.author
  
  icon_url = member.avatar_url

  avatarEmbed = discord.Embed(title = f"{member.name}\'s Avatar", color = 0xFFA500)
  
  avatarEmbed.set_image(url = f"{icon_url}")

  avatarEmbed.timestamp = ctx.message.created_at

  await ctx.send(embed = avatarEmbed)


@client.command()
async def pisuhi(ctx):
   
    if (len(ctx.message.mentions) == 0):
        await ctx.send('sopo sek jaluk dipisuhi?!')
  
    mentions = []
    mentions.extend(ctx.message.mentions)
    mentions.extend(ctx.message.role_mentions)
    for i in mentions:
        misuh = random.choice(pisuhan)
        if (isinstance(i, discord.role.Role)):
            await ctx.send(f'{misuh}  <@&{i.id}>')
            continue
        await ctx.send(f'{misuh}  <@{i.id}>')


@client.command()
async def katain(ctx):
   
    if (len(ctx.message.mentions) == 0):
        await ctx.send('nyangkemi sopo cok?')
  
    mentions = []
    mentions.extend(ctx.message.mentions)
    mentions.extend(ctx.message.role_mentions)
    for i in mentions:
        misuh = random.choice(pisuhan2)
        if (isinstance(i, discord.role.Role)):
            await ctx.send(f'{misuh}  <@&{i.id}>')
            continue
        await ctx.send(f'{misuh}  <@{i.id}>')

@client.command()
async def mood(ctx):
    await ctx.send(random.choice(emotions))

@client.command()
async def moan(ctx):
    if (ctx.author.voice):
      channel = ctx.message.author.voice.channel
      vc = await channel.connect()
      source = FFmpegPCMAudio('moan.wav')
      player = vc.play(source)

      while vc.is_playing(): #Checks if voice is playing
          await asyncio.sleep(1) #While it's playing it sleeps for 1 second
      else:
          await asyncio.sleep(1) #If it's not playing it waits 1 seconds
          while vc.is_playing(): #and checks once again if the bot is not playing
            break #if it's playing it breaks
          else:
           await vc.disconnect() #if not it disconnects
@client.command()
async def cangkemi(ctx):
    if (ctx.author.voice):
      channel = ctx.message.author.voice.channel
      vc = await channel.connect()
      source = FFmpegPCMAudio('cangkemi.wav')
      player = vc.play(source)

      while vc.is_playing(): #Checks if voice is playing
          await asyncio.sleep(1) #While it's playing it sleeps for 1 second
      else:
          await asyncio.sleep(1) #If it's not playing it waits 1 seconds
          while vc.is_playing(): #and checks once again if the bot is not playing
            break #if it's playing it breaks
          else:
           await vc.disconnect() #if not it disconnects
      

    else:
      await ctx.send("koe nandi su")


@client.command()
async def terang(ctx):
    if (ctx.author.voice):
      channel = ctx.message.author.voice.channel
      vc = await channel.connect()
      source = FFmpegPCMAudio('terang.wav')
      player = vc.play(source)

      while vc.is_playing(): #Checks if voice is playing
          await asyncio.sleep(1) #While it's playing it sleeps for 1 second
      else:
          await asyncio.sleep(1) #If it's not playing it waits 1 seconds
          while vc.is_playing(): #and checks once again if the bot is not playing
            break #if it's playing it breaks
          else:
           await vc.disconnect() #if not it disconnects
      

    else:
      await ctx.send("koe nandi su")

@client.command()
async def bantuin(ctx):
    if (ctx.author.voice):
      channel = ctx.message.author.voice.channel
      vc = await channel.connect()
      source = FFmpegPCMAudio('bantuin.wav')
      player = vc.play(source)

      while vc.is_playing(): #Checks if voice is playing
          await asyncio.sleep(1) #While it's playing it sleeps for 1 second
      else:
          await asyncio.sleep(1) #If it's not playing it waits 1 seconds
          while vc.is_playing(): #and checks once again if the bot is not playing
            break #if it's playing it breaks
          else:
           await vc.disconnect() #if not it disconnects
      

    else:
      await ctx.send("koe nandi su")

@client.command()
async def kaget(ctx):
    if (ctx.author.voice):
      channel = ctx.message.author.voice.channel
      vc = await channel.connect()
      source = FFmpegPCMAudio('kaget.wav')
      player = vc.play(source)

      while vc.is_playing(): #Checks if voice is playing
          await asyncio.sleep(1) #While it's playing it sleeps for 1 second
      else:
          await asyncio.sleep(1) #If it's not playing it waits 1 seconds
          while vc.is_playing(): #and checks once again if the bot is not playing
            break #if it's playing it breaks
          else:
           await vc.disconnect() #if not it disconnects
      

    else:
      await ctx.send("koe nandi su")

@client.command()
async def ndodog(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    source = FFmpegPCMAudio('ndodog.wav')
    player = vc.play(source)

    while vc.is_playing():
        await asyncio.sleep(1)
    else:
        await asyncio.sleep(1)
        while vc.is_playing():
          break
        else:
          await vc.disconnect()

  else:
    await ctx.send("koe neng di su bajingani!")

@client.command()
async def clap(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    source = FFmpegPCMAudio('clap.wav')
    player = vc.play(source)

    while vc.is_playing():
        await asyncio.sleep(1)
    else:
        await asyncio.sleep(1)
        while vc.is_playing():
          break
        else:
          await vc.disconnect()

  else:
    await ctx.send("koe neng di su bajingani!")

@client.command()
async def kenthu(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    source = FFmpegPCMAudio('kenthu.wav')
    player = vc.play(source)

    while vc.is_playing():
        await asyncio.sleep(1)
    else:
        await asyncio.sleep(1)
        while vc.is_playing():
          break
        else:
          await vc.disconnect()

  else:
    await ctx.send("koe neng di su bajingani!")

@client.command()
async def messi(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    source = FFmpegPCMAudio('messi.wav')
    player = vc.play(source)

    while vc.is_playing():
        await asyncio.sleep(1)
    else:
        await asyncio.sleep(1)
        while vc.is_playing():
          break
        else:
          await vc.disconnect()

  else:
    await ctx.send("koe neng di su bajingani!")


@client.command()
async def minggat(ctx):
    if(ctx.voice_client):
      await ctx.guild.voice_client.disconnect()
    else:
      await ctx.send("????")




    
#online method from online.py
online()

client.run(os.getenv('TOKEN'))