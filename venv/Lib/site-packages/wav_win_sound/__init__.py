# Pixelsuft WAV Sound Player.
# Copyright Pixelsuft, 2021.
from os import name as os_type


if __name__ == '__main__':
    print('This is module, not file!')
    exit()
if not os_type=='nt':
    print('This module is only for windows!')
    exit()


play_sound_path = __path__[0].replace('/', '\\')
if not play_sound_path[-1] == '\\':
    play_sound_path += '\\'


from subprocess import check_output as run_sync_cmd
from subprocess import Popen as run_async_cmd
from parse_args import set as set_args
from threading import Thread as thread
from os import access as file_exists
from os import F_OK as file_exists_param
from urllib.request import urlretrieve as download


class Mixer():
    def __init__(self, **kwargs):
        self.sound_list = []
        self.cmd_line = ''
        self.is_playing = False
    
    
    def check_player(self):
        if not file_exists(play_sound_path + 'play_sound.exe', file_exists_param):
            try:
                download('https://github.com/Pixelsuft/wav_win_sound/raw/main/wav_win_sound/play_sound.exe', play_sound_path + 'play_sound.exe')
                return True
            except:
                return False
        else:
            return True
    
    
    def load(self, filenames):
        if self.check_player() == True:
            self.sound_list = [play_sound_path + 'play_sound.exe']
            if type(filenames) == list:
                self.sound_list += filenames
            else:
                self.sound_list.append(str(filenames))
            self.cmd_line = set_args(self.sound_list)
    
    
    def sync_play(self):
        if self.check_player() == True:
            try:
                self.is_playing = True
                run_sync_cmd(self.cmd_line, shell = True)
                self.is_playing = False
                return True
            except:
                self.is_playing = False
                return False
    
    
    def async_play(self):
        if self.check_player() == True:
            thread(target=self.sync_play).start()
    
    
    def async_play_old(self):
        if self.check_player() == True:
            try:
                run_async_cmd(self.cmd_line, shell = True)
                return True
            except:
                return False
    
    
    def stop(self):
        try:
            run_sync_cmd('taskkill /f /im play_sound.exe', shell = True)
            self.is_playing = False
            return True
        except:
            return False
