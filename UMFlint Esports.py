import random
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.utils import get
import shelve
import asyncio
import config
intents = discord.Intents.default()
intents.members = True
intents.reactions = True

# Assigning id's and bot object
TOKEN = config.token  # os.environ['TOKEN']
GUILD = config.guild  # os.environ['GUILD']
bot = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    guild = bot.get_guild(692095297844805732)
    channel = get(guild.text_channels, name='bot-status')
    async for msg in channel.history():
        if msg.content == 'I am offline!' or msg.content == 'I am online!':
            specific = msg
    await specific.edit(content='I am online!')


# # Allows a user to join an existing game role
# @bot.command(name='game', help='Gain access to a game')
# async def add_role(ctx, game):  # pass user and role
#     member = ctx.message.author
#     game = str(game)
#     guild = ctx.guild
#     desired_role = get(guild.roles, name=game)
#     # Checking if the role exists
#     if desired_role is None:
#         await ctx.send(f'{game} does not exist')
#         return
#     if desired_role in member.roles:  # checks all roles the member has
#         await member.remove_roles(desired_role)  # removes the role
#         await ctx.send(f'You have been removed from {game}')
#     else:
#         await member.add_roles(desired_role)  # adds the role
#         await ctx.send(f'You have been added to {game}')


# Reaction code to get roles


@bot.event
async def on_raw_reaction_add(payload):
    guild = payload.member.guild
    ChID = '752241151641255986'

    if str(payload.channel_id) != ChID:
        return

    emoji = int(payload.emoji.id)
    user = guild.get_member(payload.user_id)

    if emoji == 752263285759279165:
        role = discord.utils.get(guild.roles, name='rocket-league')
        if role in user.roles:
            await user.remove_roles(role)
            return
        else:
            await user.add_roles(role)
            return
    if emoji == 752263285512077514:
        role = discord.utils.get(guild.roles, name='overwatch')
        if role in user.roles:
            await user.remove_roles(role)
            return
        else:
            await user.add_roles(role)
            return
    if emoji == 752263285545369711:
        role = discord.utils.get(guild.roles, name='rainbow-6-siege')
        if role in user.roles:
            await user.remove_roles(role)
            return
        else:
            await user.add_roles(role)
            return
    if emoji == 752263285205893224:
        role = discord.utils.get(guild.roles, name='csgo')
        if role in user.roles:
            await user.remove_roles(role)
            return
        else:
            await user.add_roles(role)
            return
    if emoji == 752263285478522890:
        role = discord.utils.get(guild.roles, name='cod-mw')
        if role in user.roles:
            await user.remove_roles(role)
            return
        else:
            await user.add_roles(role)
            return
    if emoji == 752263268596187317:
        role = discord.utils.get(guild.roles, name='super-smash-bros')
        if role in user.roles:
            await user.remove_roles(role)
            return
        else:
            await user.add_roles(role)
            return
    if emoji == 752263260367093820:
        role = discord.utils.get(guild.roles, name='league-of-legends')
        if role in user.roles:
            await user.remove_roles(role)
            return
        else:
            await user.add_roles(role)
            return
    if emoji == 752263246979006515:
        role = discord.utils.get(guild.roles, name='valorant')
        if role in user.roles:
            await user.remove_roles(role)
            return
        else:
            await user.add_roles(role)
            return
    if emoji == 890997219250024458:
        role = discord.utils.get(guild.roles, name='fortnight')
        if role in user.roles:
            await user.remove_roles(role)
            return
        else:
            await user.add_roles(role)
            return


# Reaction code to remove roles
@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(payload.guild_id)
    user = guild.get_member(payload.user_id)
    ChID = '752241151641255986'

    if str(payload.channel_id) != ChID:
        return

    emoji = int(payload.emoji.id)

    if emoji == 752263285759279165:
        role = discord.utils.get(guild.roles, name='rocket-league')
        if role in user.roles:
            await user.remove_roles(role)
            return
    if emoji == 752263285512077514:
        role = discord.utils.get(guild.roles, name='overwatch')
        if role in user.roles:
            await user.remove_roles(role)
            return
    if emoji == 752263285545369711:
        role = discord.utils.get(guild.roles, name='rainbow-6-siege')
        if role in user.roles:
            await user.remove_roles(role)
            return
    if emoji == 752263285205893224:
        role = discord.utils.get(guild.roles, name='csgo')
        if role in user.roles:
            await user.remove_roles(role)
            return
    if emoji == 752263285478522890:
        role = discord.utils.get(guild.roles, name='cod-mw')
        if role in user.roles:
            await user.remove_roles(role)
            return
    if emoji == 752263268596187317:
        role = discord.utils.get(guild.roles, name='super-smash-bros')
        if role in user.roles:
            await user.remove_roles(role)
            return
    if emoji == 752263260367093820:
        role = discord.utils.get(guild.roles, name='league-of-legends')
        if role in user.roles:
            await user.remove_roles(role)
            return
    if emoji == 752263246979006515:
        role = discord.utils.get(guild.roles, name='valorant')
        if role in user.roles:
            await user.remove_roles(role)
            return
    if emoji == 890997219250024458:
        role = discord.utils.get(guild.roles, name='fortnight')
        if role in user.roles:
            await user.remove_roles(role)
            return


# Allows an admin to create new game areas
@bot.command(name='create', help='Creates a new game role and channel')
@commands.has_role('MAIZE')
async def create_role(ctx, game):
    # Setting up important reference variables
    guild = ctx.guild
    new_role = str(game)
    category = discord.utils.get(guild.categories, name='Games')
    print(get(guild.roles, name=game))

    # Checking if the role already exists
    if get(guild.roles, name=game) is not None:
        await ctx.send(f'{game} already exists')
        return

    # Creating the role
    await guild.create_role(name=new_role)
    desired_role = get(guild.roles, name=game)
    await desired_role.edit(mentionable=True, hoist=True)

    # Creating the channel so only those with the role can see
    await guild.create_text_channel(new_role, category=category)
    channel = discord.utils.get(guild.text_channels, name=game)
    await channel.edit(sync_permissions=True)
    await channel.set_permissions(desired_role, read_messages=True, send_messages=True)
    await ctx.send(f'A channel and role has been made for {game}')
    await channel.send(f'Welcome, this is the beginning of {game}')

    # Creating the voice channel so only those with the role can see
    await guild.create_voice_channel(new_role, category=category)
    voice = discord.utils.get(guild.voice_channels, name=game)
    await voice.edit(sync_permissions=True)
    await voice.set_permissions(desired_role, read_messages=True, send_messages=True)


# Allows an admin to delete game areas
@bot.command(name='delete', help='Deletes a game role and channel')
@commands.has_permissions(administrator=True)
async def delete_role(ctx, game):
    guild = ctx.guild
    game = str(game)
    role = get(guild.roles, name=game)
    channel = get(guild.text_channels, name=game)
    voice = discord.utils.get(guild.voice_channels, name=game)
    await role.delete()
    await channel.delete()
    await voice.delete()


# Allows the user to check who plays a specific game
@bot.command(name='players', help='Shows the players of a game')
async def members_of_game(ctx, game):
    guild = ctx.guild
    role = get(guild.roles, name=game)
    playing = shelve.open('playing.txt', flag='r')

    if role is None:
        await ctx.send('That is not a role, try using the exact name of the channel')
        return

    members = role.members

    output = 'These are the members who play {} (Bold names are looking to play!):\n'.format(game)
    for member in members:
        if str(member.id) in playing.keys():
            if game in playing[str(member.id)]:
                output += "**" + str(member) + "**" + '\n'
            else:
                output += str(member) + '\n'
        else:
            output += str(member)+'\n'
    await ctx.send(output)


# Allows the user to check who plays a specific game
@bot.command(name='select', help='Randomly selects one player')
async def random_select(ctx, game):
    guild = ctx.guild
    role = get(guild.roles, name=game)
    members = role.members
    selection = str(random.choice(members))
    await ctx.send(f'This user was chosen:\n'+selection)


# # Allows the user to check who plays a specific game
# @bot.command(name='setup', help='f')
# async def fff(ctx):
#     channel = bot.get_channel(752241151641255986)
#     await channel.send('''Welcome to UMFlint Esports, the official University of Michigan-Flint
# competitive gaming organization.To access specific game channels, and receive a role,
# please click the reaction emoji for the corresponding category from the following list.
# If you no longer wish to be included in a category,
# re-click on the same reaction emoji to remove the role.
# Thank you for joining our community!''')
#     await channel.send('**Rocket League**')
#     await channel.send('**Overwatch**')
#     await channel.send('**Rainbow 6 Siege**')
#     await channel.send('**CS-GO**')
#     await channel.send('**COD-MW**')
#     await channel.send('**Super Smash Bros.**')
#     await channel.send('**League of Legends**')
#     await channel.send('**Valorant**')


# Allows the user to flip a coin
@bot.command(name='flip', help='flip a coin')
async def fff(ctx):
    coin = ['Heads', 'Tails']
    output = random.choice(coin)
    await ctx.send(output)


# Allows the user to check who plays a specific game
@bot.command(name='schedule', help='allows you to store your schedule to be viewed by others')
async def scheduling(ctx):
    auth = str(ctx.message.author.id)
    con = str(ctx.message.content)
    temp_add = []

    # Opening the master schedule
    master = shelve.open('master.txt', flag='c', writeback=True)

    def said_yes(response):
        return 'yes' in response.content.lower() and response.author.id == ctx.message.author.id

    if auth in master:
        await ctx.send('You already have a schedule. If you want to replace it, type yes. This will cancel in 20s.')
        try:
            await bot.wait_for("message", check=said_yes, timeout=20)
        except asyncio.exceptions.TimeoutError:
            await ctx.send('You ran out of time, exiting the scheduler!')
            return

    await ctx.send("Welcome to the scheduler! We will walk through each day and you will enter your availability.")

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days:
        await ctx.send(f"What is your availability for {day}?")
        temp_m = await bot.wait_for("message", check=(lambda s: s.author == ctx.message.author))
        temp_add.append((day, temp_m.content))

    master[auth] = temp_add
    master.close()
    await ctx.send('You have created your schedule!')


# Allows the user to check who plays a specific game
@bot.command(name='check', help='check the schedule of a user. !check @user')
async def scheduling_check(ctx, user=None):
    if user is None:
        user = str(ctx.message.author.id)
    elif not user.startswith("<@"):
        await ctx.send("You have to mention someone!")
        return
    else:
        user = user.strip("<@!{>")

    user_output = bot.get_user(int(user))
    con = str(ctx.message.content)
    temp_add = []
    output = ''

    # Opening the master schedule
    master = shelve.open('master.txt', flag='r')

    for schedule in master:
        if schedule == user:
            output += f'This is the schedule of **{user_output}**\n\n'
            for day in master[schedule]:
                output += f'{day[0]}: {day[1]}\n\n'
            await ctx.send(output)
            master.close()
            return
    await ctx.send('They do not have a schedule!')
    master.close()
    return


# Allows the user to say they are looking to play a particular game
@bot.command(name='play', help='register that you are looking to play. !play game remove to stop')
async def looking_to_play(ctx, game, remove=None):
    guild = ctx.guild
    auth = str(ctx.message.author.id)
    if game.startswith("<@"):
        game = int(game.strip("<@&>"))
        role = get(guild.roles, id=game)
        game = role.name
    else:
        role = get(guild.roles, name=game)

    if role is None:
        await ctx.send('That is not a role, try using the exact name of the channel/role')
        return

    playing = shelve.open('playing.txt', flag='c', writeback=True)

    if auth not in playing.keys():
        playing[auth] = []

    temp = playing[auth]

    if remove == 'remove':
        for stored_game in temp:
            if stored_game == game:
                temp.remove(game)
                await ctx.send(f'You have been removed from looking to play {game}')
                playing.close()
                return
        await ctx.send(f'You were not looking to play {game}')
        playing.close()
        return

    if game in temp:
        await ctx.send('You are already playing that game! To remove yourself use !play GameName remove.')
        playing.close()
        return

    else:
        temp.append(game)
        playing[auth] = temp
        playing.close()
        await ctx.send(f'You are now looking to play {game}!')
        return


# Allows picture saving to your account
@bot.command(name='imgs', help='save an img link to your account. !imgs name url. Names must not have spaces')
async def saving_image(ctx, name, url):
    guild = ctx.guild
    auth = str(ctx.message.author.id)

    if name is None or url is None:
        await ctx.send('Please include both a name and url. !img Name Url')
        return

    img_log = shelve.open('img_log.txt', flag='c', writeback=True)

    if auth not in img_log.keys():
        img_log[auth] = []

    temp = img_log[auth]

    temp.append((name, url))
    img_log[auth] = temp
    img_log.close()
    await ctx.send(f'You have saved the image as {name}!')
    return


# Allows showing peoples pictures
@bot.command(name='imgl', help='Load an image linked to an account. !imgl @user name')
async def load_image(ctx, user, name=None):
    guild = ctx.guild
    user = user.strip("<@!>")

    user_output = bot.get_user(int(user))

    img_log = shelve.open('img_log.txt', flag='r')

    if user not in img_log.keys():
        await ctx.send('They do not have any saved images!')
        return

    temp = img_log[user]

    if name is None:
        output = 'These are the image names they have saved:\n\n'
        for temp_name in temp:
            output += f'{temp_name[0]}\n'
        await ctx.send(output)
        img_log.close()
        return

    for temp_name in temp:
        if temp_name[0] == name:
            output = 'This is the image url:\n'
            output += f'{temp_name[1]}'
            await ctx.send(output)
            img_log.close()
            return
    await ctx.send(f"They don't have an image saved as {name}, try the command without a name for a list")
    img_log.close()
    return


# Allows the user to choose an identity
@bot.command(name='identity', help='Give yourself tags for gender and pronouns')
async def identity(ctx):
    output = ''
    auth = ctx.message.author
    rep = True
    guild = auth.guild
    member = auth

    await ctx.send(f'Welcome, type the letter of the option you want from each list that shows up, '
                   f'if you already have the role, it will be removed.\n')
    output += f'Select a gender:\n\n'
    output += f'A: Male\nB: Female\nC: Non-binary\nD: Other'
    await ctx.send(output)

    while rep is True:
        gender = await bot.wait_for("message", check=(lambda s: s.author == auth))
        gender = gender.content.lower()
        if gender == 'cancel' or gender == 'stop':
            await ctx.send("Ending script.")
            return
        if gender not in ['a', 'b', 'c', 'd']:
            await ctx.send("Sorry, that was not an option. Try again, or type cancel to exit!")
            continue
        else:
            rep = False

    rep = True
    output = 'Select a pronoun:\n\n'
    output += 'A: He/Him\nB: He/They\nC: She/Her\nD: She/They\nE: They/Them\nF: Other'
    await ctx.send(output)

    while rep is True:
        pronoun = await bot.wait_for("message", check=(lambda s: s.author == auth))
        pronoun = pronoun.content.lower()
        if pronoun == 'cancel' or pronoun == 'stop':
            await ctx.send("Ending script.")
            return
        if pronoun not in ['a', 'b', 'c', 'd', 'e', 'f']:
            await ctx.send("Sorry, that was not an option. Try again, or type cancel to exit!")
        else:
            rep = False

    # Code block for assigning gender roles
    if gender == 'a':
        role_id = 754160909009682553
        desired_role = get(guild.roles, id = role_id)
        name = desired_role.name
        if desired_role in member.roles:  # checks all roles the member has
            await member.remove_roles(desired_role)  # removes the role
            await ctx.send(f'{name} has been removed.')
        else:
            await member.add_roles(desired_role)  # adds the role
            await ctx.send(f'You have been given {name}.')

    if gender == 'b':
        role_id = 754160946183798854
        desired_role = get(guild.roles, id = role_id)
        name = desired_role.name
        if desired_role in member.roles:  # checks all roles the member has
            await member.remove_roles(desired_role)  # removes the role
            await ctx.send(f'{name} has been removed.')
        else:
            await member.add_roles(desired_role)  # adds the role
            await ctx.send(f'You have been given {name}.')

    if gender == 'c':
        role_id = 754160970334732299
        desired_role = get(guild.roles, id = role_id)
        name = desired_role.name
        if desired_role in member.roles:  # checks all roles the member has
            await member.remove_roles(desired_role)  # removes the role
            await ctx.send(f'{name} has been removed.')
        else:
            await member.add_roles(desired_role)  # adds the role
            await ctx.send(f'You have been given {name}.')

    if gender == 'd':
        role_id = 754161030946619543
        desired_role = get(guild.roles, id = role_id)
        name = desired_role.name
        if desired_role in member.roles:  # checks all roles the member has
            await member.remove_roles(desired_role)  # removes the role
            await ctx.send(f'{name} has been removed.')
        else:
            await member.add_roles(desired_role)  # adds the role
            await ctx.send(f'You have been given {name}.')

    # Code block for assigning pronoun roles
    if pronoun == 'a':
        role_id = 754161080611242074
        desired_role = get(guild.roles, id = role_id)
        name = desired_role.name
        if desired_role in member.roles:  # checks all roles the member has
            await member.remove_roles(desired_role)  # removes the role
            await ctx.send(f'{name} has been removed.')
        else:
            await member.add_roles(desired_role)  # adds the role
            await ctx.send(f'You have been given {name}.')

    if pronoun == 'b':
        role_id = 754161340997959701
        desired_role = get(guild.roles, id = role_id)
        name = desired_role.name
        if desired_role in member.roles:  # checks all roles the member has
            await member.remove_roles(desired_role)  # removes the role
            await ctx.send(f'{name} has been removed.')
        else:
            await member.add_roles(desired_role)  # adds the role
            await ctx.send(f'You have been given {name}.')

    if pronoun == 'c':
        role_id = 754161378402762803
        desired_role = get(guild.roles, id = role_id)
        name = desired_role.name
        if desired_role in member.roles:  # checks all roles the member has
            await member.remove_roles(desired_role)  # removes the role
            await ctx.send(f'{name} has been removed.')
        else:
            await member.add_roles(desired_role)  # adds the role
            await ctx.send(f'You have been given {name}.')

    if pronoun == 'd':
        role_id = 754161410887385231
        desired_role = get(guild.roles, id = role_id)
        name = desired_role.name
        if desired_role in member.roles:  # checks all roles the member has
            await member.remove_roles(desired_role)  # removes the role
            await ctx.send(f'{name} has been removed.')
        else:
            await member.add_roles(desired_role)  # adds the role
            await ctx.send(f'You have been given {name}.')

    if pronoun == 'e':
        role_id = 754161445377409095
        desired_role = get(guild.roles, id = role_id)
        name = desired_role.name
        if desired_role in member.roles:  # checks all roles the member has
            await member.remove_roles(desired_role)  # removes the role
            await ctx.send(f'{name} has been removed.')
        else:
            await member.add_roles(desired_role)  # adds the role
            await ctx.send(f'You have been given {name}.')

    if pronoun == 'f':
        role_id = 754161499114700938
        desired_role = get(guild.roles, id = role_id)
        name = desired_role.name
        if desired_role in member.roles:  # checks all roles the member has
            await member.remove_roles(desired_role)  # removes the role
            await ctx.send(f'{name} has been removed.')
        else:
            await member.add_roles(desired_role)  # adds the role
            await ctx.send(f'You have been given {name}.')


# Allows the user to pin a message in the game chats if they have the role
@bot.command(name='pin', help='Pin the message that contains the command')
async def pin(ctx):
    msg = ctx.message
    guild = ctx.message.author.guild
    channel_name = ctx.message.channel.name
    member = ctx.message.author
    role = get(guild.roles, name=channel_name)
    if role is None:
        await ctx.send('You can not pin outside of the game channels')
        return
    await msg.pin()


# Allows user to save their ign's for various games to be seen as a list later
@bot.command(name='igns', help='Save your ign for various games. !igns game [ign]')
async def igns_command(ctx, game=None, ign=None):
    guild = ctx.guild
    auth = str(ctx.message.author.id)

    if game is None or ign is None:
        await ctx.send('Please include both a game and ign. !igns game [ign]')
        return

    ign_log = shelve.open('ign_log.txt', flag='c', writeback=True)

    if auth not in ign_log.keys():
        ign_log[auth] = []

    temp = ign_log[auth]

    for x in temp:
        if x[0] == game:
            await ctx.send(f'Would you like to change your ign from {x[0]} for {game}?')
            temp_m = await bot.wait_for("message", check=(lambda s: s.author == ctx.message.author))
            if temp_m.lower() == 'yes':
                temp.append((game, ign))
                ign_log[auth] = temp
                ign_log.close()
                await ctx.send(f'You have saved your ign for {game} as {ign}!')
                return
            else:
                return

    temp.append((game, ign))
    ign_log[auth] = temp
    ign_log.close()
    await ctx.send(f'You have saved your ign for {game} as {ign}!')
    return


# Allows users to view other users' igns
@bot.command(name='ign', help='Show a list of igns for a user. !ign @user')
async def ign_command(ctx, user=None):
    guild = ctx.guild
    user = user.strip("<@!>")

    user_output = bot.get_user(int(user))

    if user is None:
        await ctx.send('Please mention a user to get their IGNs using !ign @[user]')
        return

    ign_log = shelve.open('ign_log.txt', flag='r')

    if user not in ign_log.keys():
        await ctx.send('They do not have any saved IGNs!')
        return

    temp = ign_log[user]

    output = 'These are the IGNs they have saved:\n\n'
    for temp_name in temp:
        output += f'For {temp_name[0]}: Their IGN is {temp_name[1]}\n'
    await ctx.send(output)
    ign_log.close()
    return


@bot.command(name='shutdown')
@commands.has_role('MAIZE')
async def shutdown(ctx):
    guild = bot.get_guild(692095297844805732)
    channel = get(guild.text_channels, name='bot-status')
    async for msg in channel.history():
        if msg.content == 'I am online!':
            specific = msg
    await specific.edit(content='I am offline!')
    await ctx.bot.logout()


# Sends a DM to those who join the server asking for their UMID
@bot.event
async def on_member_join(member):
    msg = "Hello, welcome to the UMFlint Esports Server! Please type both your name and UMID in " \
          "the same message to be verified."

    await member.send(msg)

# # Allows the user to check who plays a specific game
# @bot.group(name='pet', help='Manage your pet!')
# async def pet_menu(ctx, opt=None, member: discord.Member = None):
#     if member is not None:
#         guild = member.guild
#         user = guild.get_member(member.strip("<@!>"))
#     auth = str(ctx.message.author.id)
#     con = ctx.message.content.lower()
#     temp_add = []
#     pets = shelve.open('pets.txt', flag='c', writeback=True)
#
#     if opt is None:
#         await ctx.send('''Welcome to pet Esports. You can manage your pet and risk it all fighting others!
# Use !pet Action to use your pet.
# The The actions are: fight, pet, and check (So far!)''')
#
#     if auth not in pets.keys():
#         await ctx.send("You don't have a pet, do you want to generate one?")
#         try:
#             await bot.wait_for("message", check=(lambda s: s.author==ctx.message.author
#                                                            and 'yes' in s.content), timeout=20)
#         except TimeoutError:
#             await ctx.send('Stopping pet generation!')
#             return
#
#         # Will be stored as Name, Health, Attack, Defense
#         temp_pet_stats = random.randrange(5, 16), random.randrange(5, 16), random.randrange(5, 16)
#         await ctx.send("What is their name?")
#         temp_name = await bot.wait_for("message", check=(lambda s: s.author == ctx.message.author))
#         temp_add.append(temp_name)
#         for value in temp_pet_stats:
#             temp_add.append(value)
#         pets[auth] = temp_add
#
#     temp_assignment = pets[auth]
#     name = temp_assignment[0]
#     health = temp_assignment[1]
#     attack = temp_assignment[2]
#     defense = temp_assignment[3]
#
#     if opt is None:
#         pets.close()
#         return
#     if member is None:
#         pets.close()
#         return
#
#     if opt == 'check':
#         output = f'Your Pets name is **{name}**, and these are their stats:\n'
#         output += f'Health: {health}\nAttack: {attack}\nDefense: {defense}'
#
#     # if opt == 'fight':


# If someone types a command that doesn't exist
@bot.event
async def on_command_error(ctx, error):
    user_message_error = open('user_error.txt', 'a')
    user_message_error.write(f'Author: {ctx.message.author}\nError: {error}\nMessage: {ctx.message.content}\n\n')
    user_message_error.close()
    if isinstance(error, CommandNotFound):
        await ctx.send('That is not a command')
        return
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('You are missing an argument')
        return
    raise error


# Examines all messages
@bot.event
async def on_message(message):
    auth = str(message.author.id)
    con = message.content
    con = con.lower()
    channel = bot.get_channel(787162590043439115)

    if message.guild is None and message.author != bot.user:
        output = str(message.author)+": "+message.content
        await channel.send(output)

    # Allows messages to eventually reach commands
    await bot.process_commands(message)


# Initializes the bot object
bot.run(TOKEN)