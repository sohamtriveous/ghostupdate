__author__ = 'sohammondal'

import commands
import sys
import os

'''
24-08-2014
'''

def exec_cmd(cmd):
    '''
    execute the given command
    :param cmd: the command to be execute
    :return:
    '''
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        print 'Could not execute', cmd, sys.stderr
        return False
    return True

def update_ghost():
    '''
    update ghost
    source: http://goo.gl/bG4oXG
    :return:
    '''
    print 'Stopping ghost'
    exec_cmd('service ghost stop')
    os.chdir('/var/www/')
    print 'Downloading the latest ghost'
    exec_cmd('wget '+ ghost_url)
    print 'Download complete, unzipping'
    exec_cmd('unzip -uo ghost*.zip -d ghost')
    exec_cmd('chown -R ghost:ghost ghost/*')
    os.chdir('/var/www/ghost')
    print 'Installing/Upgrading...'
    exec_cmd('npm install')
    print 'Successful, starting ghost'
    exec_cmd('service ghost start')
    print 'Great, ghost started, you are good to go!'
    return

#this is the url for the latest ghost
ghost_url = 'http://ghost.org/zip/ghost-latest.zip'

update_ghost()
