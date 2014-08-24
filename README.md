ghostupdate
===========

A python utility to update ghost on your digital ocean droplet. (Should work on a typical ghost setup on another VPS but this has not been tested on any other setup)

###Prerequisites
- preinstalled ghost setup on a digital ocean droplet
- root ssh access

###How to use

####Step 1: ssh into your digital ocean droplet
```bash
ssh root@a.b.c.d
```

####Step 2: download this python file
```bash
wget https://raw.githubusercontent.com/triveous/ghostupdate/master/ghostupdate.py
```

####Step 3: run this file
```bash
python ghostupdate.py
```

###Typical output
```bash
Stopping ghost
Downloading the latest ghost
Download complete, unzipping
Installing/Upgrading...
Successful, starting ghost
Great, ghost started, you are good to go!
```

###Credits
The digital ocean blog post on ghost: https://www.digitalocean.com/community/tutorials/how-to-configure-and-maintain-ghost-from-the-command-line
