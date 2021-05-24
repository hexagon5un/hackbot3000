## Hackbot3000

This is tutorial code for writing super-simplistic IRC chat bots.  

* `hello_world.py` contains a bare scaffolding demo, everything in one script.  Run it, tweak it, play around with it interactively.

* `hackbot3000` is a bit more feature-rich, and imports the nitty-gritty from `irc.py` and the IRC class within.  

Work in progress!  

Come play with us in _#hackaday-bots_ on _irc.libera.chat_.

## On IRC Bots

There are really only a couple of things you _need_ to do to make a bot. 

* Connect a plain-old socket

* Authenticate to the server: NICK and USER will suffice for simple stuff, but you might want to register the bot's name, in which case you'll need to set a password.

* Join a channel

* Respond to keepalive PINGs

* And the rest is up to you.  `hello_world.py` has some too-basic scaffolding to give you ideas.

* If you want to get serious, you probably want to look around:
  [`Phenny`](http://inamidst.com/phenny/) is a good baseline for functionality.

