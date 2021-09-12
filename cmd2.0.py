import os
import socket
import subprocess
#from pyfiglet import Figlet

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
path = 'C:/'
command_list = ['ls','ping','ip','name','quit','','create','help']
extentions = {
    'python':'.py',
    'py':'.py',
    'text':'.txt',
    'txt':'.txt',
    'java':'.java',
    'html':'.html',
    'css':'.css',
    'c':'.c'
}

def main():
    user_input = input(': ')
    word_list = user_input.split()
    print(word_list)
    print(len(word_list))

def ls():
    dir_list_c = os.listdir(path)
    return dir_list_c

def ping(target):
    ping_command = ['ping', target]
    return subprocess.call(ping_command)

def get_intial_path():
    return os.system('cd')

def get_help():
    commands = [
        'ip => to get the ip of the device',
        'name => to get the name of the device',
        'ping => to make ping tests of a server via ip addres or domain name',
        'ls => to get the list of files in the same folder OR add -a with a directory path for a specifec folder',
        'create => it take a name as an argument to make txt files or add an extention as a second argument and a directory path for a specific folder',
        'quit => to quit the terminal'
    ]
    com_list_len = len(commands)
    _all = ''

    for i in range(com_list_len):
        if i == com_list_len - 1:
            _all += commands[i]
        else:
            _all += commands[i]
            _all += '\n'
    return _all

def check_extention(arguments_list):
    if arguments_list[2] in extentions:
        return '1'
    else:
        return '0'

if __name__ == '__main__':
    #f = Figlet(font='slant')
    #print(f.renderText('Terminal 2.0'))
    while True:
        command = input('>>>')
        arguments_list = command.split()
        if command == "":
            pass
        else:
            if arguments_list[0] in command_list:
                if len(arguments_list) == 4:
                    if arguments_list[0] == 'create':

                        check_extention_return = check_extention(arguments_list)
                        if check_extention_return == '1':
                            try:
                                intial_path = os.getcwd()
                                #print(intial_path)
                                user_directory = arguments_list[3]
                                os.chdir(user_directory)
                                #go to path 'cd'
                                file_name = arguments_list[1]+extentions[arguments_list[2]]
                                open(file_name,'a').close()
                                os.system('code '+file_name)
                                os.chdir(intial_path)
                            except PermissionError:
                                print('you can not create files in this folder')

                        else:
                            ext_list = list(extentions.keys())
                            ext_list_len = len(ext_list)
                            _all = ''

                            for i in range(ext_list_len):
                                if i == ext_list_len - 1:
                                    _all += ext_list[i]
                                else:
                                    _all += ext_list[i]
                                    _all += ' , '
                            print('please use an extentions from this list:')
                            print(_all)

                if len(arguments_list) == 3:

                    if arguments_list[0] == 'ls':

                        if arguments_list[1] == '-a':
                            try:
                                user_path = arguments_list[2]
                                dir_list = os.listdir(user_path)
                                dir_list_len = len(dir_list)
                                _all = ''

                                for i in range(dir_list_len):
                                    if i == dir_list_len - 1:
                                        _all += dir_list[i]
                                    else:
                                        _all += dir_list[i]
                                        _all += ' , '
                                print(_all)
                                #print(dir_list)
                            except:
                                print(f'{user_path} path not found')

                    if arguments_list[0] == 'create':

                        check_extention_return = check_extention(arguments_list)
                        if check_extention_return == '1':
                            file_name = arguments_list[1]+extentions[arguments_list[2]]
                            open(file_name,'a').close()
                            os.system('code '+file_name)

                        else:
                            ext_list = list(extentions.keys())
                            ext_list_len = len(ext_list)
                            _all = ''

                            for i in range(ext_list_len):
                                if i == ext_list_len - 1:
                                    _all += ext_list[i]
                                else:
                                    _all += ext_list[i]
                                    _all += ' , '
                            print('please use an extentions from this list:')
                            print(_all)
                            #print(extentions.keys())

                if len(arguments_list) == 2:

                    if arguments_list[0] == 'ping':
                        target = arguments_list[1]
                        ping(target)
                    if arguments_list[0] == 'create':
                        file_name = arguments_list[1]+'.txt'
                        open(file_name,'a').close()
                        os.system('code '+file_name)

                if len(arguments_list) == 1:

                    if arguments_list[0] == 'ls':
                        print(ls())
                    if arguments_list[0] == 'ip':
                        print(f'your ip is {host_ip}')
                    if arguments_list[0] == 'name':
                        print(f'your name is {host_name}')
                    if arguments_list[0] == 'help':
                        print(get_help())
                    if arguments_list[0] == 'quit':
                        quit()
                    
                            
            else:
                print(f"'{arguments_list[0]}' command not found")