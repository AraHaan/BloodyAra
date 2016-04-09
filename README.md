# BloodyAra

![BloodyAra](https://i.gyazo.com/87a5b318e3ddc447d8008292ac44f835.png)

 * This Repo is basically Dead and so is the bot (account was reused for DecoraterBotBeta and is now a official discord bot).

Uses [discord.py](https://github.com/Rapptz/discord.py) to communicate with the Discord API and [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) to scrape Elwiki.

# Requirements
*  python 3.4 or higher
*  heroku toolbelt
*  git
*  pip

# Installation

*  Clone the repo or download it into a folder and command line to it
*  run `pip install -r requirements.txt`
*  setup a virtual environment using `virtualenv venv` and start it with `venv\scripts\Activate.bat`
*  make your app in heroku
*  add the git remote in using `heroku git:remote -a your-app-name`
*  add `DISCORD_USER` and `DISCORD_PASS` config vars to your heroku app using `heroku config:set` (this is the account the bot will use)
*  just to make sure everything is working fine, try running the bot locally with `heroku local` and testing
*  deploy it with `git add .` `git commit` `git push heroku master`
*  go to your heroku dashboard, open your app's resources tab, assign it a dyno and click on save. it should sign in and start responding to commands.
*  you can check the logs of your app by running `heroku logs --tail`

# Troubleshoot

If you get a problem in step 2 it's probably because lxml couldn't install itself on Windows. You'll have to download the unofficial lxml binaries for Windows corresponding to your python version and system arch from [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml) and run

    pip install wheel
    pip install <filename here>

and retry step 2.

# TODO

* make this thing modular
* user permissions for certain commands
* hook up server join and leave commands so i don't have to sign into the bot manually to make it join servers
* ?????
