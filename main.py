import discord
import os
import random
from online import online
from discord.ext import commands



#setting prefix with a list of certain string
client = commands.Bot(command_prefix=["biji ", "Biji ", "Pler ", "pler ","+"])
client.remove_command("help")


#list of bot message
pisuhan = ["JANCUK!!","GOBLOK!!","KOMUNIS!!","ASU KOE!","BADJINGAN KOE!","LONTE!!","JEMBUOTI!!",]
celukan = ["Opo su","Pie Nyuk", "Lhapo cok"]
respn = ["ndene!", "mbedhil!", "join!", "mlebu kene!", "wani ora?!"]
pisuhan2 = ["TANGANE!!", "UTEKE!!","GOBLOK!", "FAKYU!"]
emotions = ['https://www.youtube.com/watch?v=av-rLcM5AgY', 'https://www.youtube.com/watch?v=NaHNRDfJVTc','https://www.youtube.com/watch?v=mGac5cQzhII', 'https://www.youtube.com/watch?v=QojMooSYJGk', 'https://www.youtube.com/watch?v=zhf1pIl007o', 'https://www.youtube.com/watch?v=NjAN9CW_YmY', 'https://www.youtube.com/watch?v=LFOMo_vwEzc', 'https://www.youtube.com/watch?v=1jwVfvhQlng', 'https://www.youtube.com/watch?v=h-0UD2L4_fU', 'https://www.youtube.com/watch?v=zBJU9ndpH1Q', 'https://www.youtube.com/watch?v=wFWaLzZnLuk', 'https://www.youtube.com/watch?v=fKum4JmG-ew','https://www.youtube.com/watch?v=0nvR5qOG8nw']

@client.group(invoke_without_command=True)
async def tulung(ctx):
  em = discord.Embed(title= "Pertulungan", description = "tuliso biji tulung <command>  nek meh dijelaske panjang lebar.", color = ctx.author.color)

  em.add_field(name= "celukan", value = "biji ;Biji ;Pler ;pler ")
  em.add_field(name= "Jasa mengmisuh", value = "pisuhi,cangkemi")
  em.add_field(name= "Fun Stuff", value = "raine, mood")
  
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
async def cangkemi(ctx):

  em = discord.Embed(title = "Cangkemi", description = "men koe ra berdosa, koe iso ngengkon aku nyangkemi wong nggo koe.", color = ctx.author.color)
  
  em.add_field(name = "Carane", value = "celuk cangkemi <njuk ngetag member>")
  
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
async def cangkemi(ctx):
   
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





online()

client.run(os.getenv('TOKEN'))
