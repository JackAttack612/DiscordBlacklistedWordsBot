# DiscordBlacklistedWordsBot

# Making a discord bot
Go to https://discord.com/developers/applications
Click the blue "New Application" button
Enter a name for the application
Click on "bot" on the left side menu
Click "Add bot" and "Yes do it"
Under the Privileged Gateway Intents section enable "PRESENCE INTENT", "SERVER MEMBERS INTENT" and "MESSAGE CONTENT INTENT"
Go to the OAuth2 section on the left side menu
Click URL Generator under the OAuth2 section
Select "bot"
Select "Administrator"
Copy the link at the bottom of the page and paste into web browser to invite the bot to your server

# Setting up bot
Select the "bot" section in the left side menu
Copy the bot token
Put the bot token into the main.py file where instructed to
Go to discord
Go to Settings > Advanced > Enable Developer Mode
Go to your server
Right click on the channel you wish to set as your logging channel
Select copy ID
Paste the ID into the main.py file where instructed to

# Installing libraries
If on windows:
Go to windows powershell
type "pip install nextcord"

# Running the bot
If running on your own computer run the main.py file (it will have to stay open in the background)
If running on a Private Server run the main.py file 
