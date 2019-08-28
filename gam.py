#!/usr/bin/env python3

# MIT License

# Copyright (c) 2018 Luke Strohm

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# This program relies on GAM to function. You must install and configure it before using this program.
# GAM can be found at: https://github.com/jay0lee/GAM

# See lines 557, 654, 900, 909, 877, 917, 947 and 955 for a domain specific setting that will need changed.

import os
import time
import sys


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Gam:  # Various GAM arguments
    gam = '~/bin/gam/gam '
    user = '~/bin/gam/gam user '
    group = '~/bin/gam/gam group '
    ou = '~/bin/gam/gam ou '
    all = '~/bin/gam/gam all users '
    up = '~/bin/gam/gam update '
    add = 'add'
    remove = 'remove'
    de = '~/bin/gam/gam delete '
    cr = '~/bin/gam/gam create '
    info = '~/bin/gam/gam info '


class Msgs:  # Various repeated messages
    cont = 'Press ENTER to Continue...'
    err = 'Invalid Option Selected!'
    choose = 'Please Choose an Option:  '
    ent = 'Entity to apply to: [user | group | ou | all users]  '


def cred():

    print('\n')
    print(Color.DARKCYAN)
    print("*********************************")
    print("*     Python 3 Frontend for     *")
    print("*         GAM by Jay Lee        *")
    print("*                               *")
    print("*   Written and maintained by   *")
    print("*          Luke Strohm          *")
    print("*     strohm.luke@gmail.com     *")
    print("*  https://github.com/strohmy86 *")
    print("*                               *")
    print("*********************************")
    print(Color.END)


def main_menu():  # Main Menu
    while True:
        print('\n')
        print(Color.PURPLE + 'Main Menu:' + Color.END)
        print('\n')
        print('1)   User Management')
        print('2)   Calendar Management')
        print('3)   Drive Management')
        print('4)   Group Management')
        print('5)   Classroom Management')
        print('6)   Device Management')
        print('7)   Email Management')
        print('8)   Bulk Operations')
        print('9)   Vault Management')
        print('0)   Exit')
        print('\n')

        selection1 = input(Color.BOLD + Msgs.choose + Color.END)
        if selection1 == '0':
            sys.exit()
        elif selection1 == '1':
            users()
        elif selection1 == '2':
            calendar()
        elif selection1 == '3':
            drive()
        elif selection1 == '4':
            groups()
        elif selection1 == '5':
            classroom()
        elif selection1 == '6':
            devices()
        elif selection1 == '7':
            email()
        elif selection1 == '8':
            bulk()
        elif selection1 == '9':
            vault()
        else:
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)


def users():  # User Management Main Menu
    while True:
        print('\n')
        print(Color.PURPLE + 'User Management Menu:' + Color.END)
        print('\n')
        print('1)   User Information')
        print('2)   Export List of All Users')
        print('3)   Activate Suspended User')
        print('4)   Suspend User')
        print('5)   Transfer Drive Files')
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)
        if selection == '1':  # User Info menu item
            username = input(Color.BOLD + "Please enter a username: " + Color.END)
            cmd = Gam.gam + "info user " + username
            os.system(cmd)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            users()
        elif selection == '2':  # Export users menu item
            cmd = Gam.gam + " print users allfields > Userlist.csv"
            os.system(cmd)
            print('\n')
            print("Userlist.csv saved.")
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            users()
        elif selection == '3':  # Activate suspended user menu item
            username = input(Color.BOLD + "Please enter a username: " + Color.END)
            cmd = Gam.gam + " update user " + username + " suspended off"
            cmd2 = "~/bin/gam/gam info user " + username
            os.system(cmd)
            time.sleep(2)
            os.system(cmd2)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            users()
        elif selection == '4':  # Suspend a user menu item
            username = input(Color.BOLD + "Please enter a username: " + Color.END)
            cmd = Gam.gam + " update user " + username + " suspended on"
            os.system(cmd)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            users()
        elif selection == '5':  # Transfer drive files from one user to another
            user = input(Color.BOLD + 'Please enter username of source drive:  ' + Color.END)
            user2 = input(Color.BOLD + 'Please enter username of destination drive:  ' + Color.END)
            cmd = Gam.cr + 'datatransfer ' + user + ' gdrive ' + user2 + ' privacy_level shared,private'
            os.system(cmd)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            users()
        elif selection == '0':  # Back to main menu
            main_menu()
        else:  # Invalid selection. Return to this menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            users()


def calendar():  # Calendar Management Main Menu
    while True:
        print('\n')
        print(Color.PURPLE + 'Calendar Management Menu:' + Color.END)
        print('\n')
        print('1)   Show Permissions For a Calendar')
        print("2)   Add or Remove Calendar Permissions")
        print('3)   Delete a Calendar Event')
        print("4)   List a User's Calendar(s)")
        print("5)   Delete a User's Calendar (Cannot delete default calendar)")
        print("6)   Add a Calendar to a User")
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)
        if selection == '1':  # Calendar permissions menu item
            cal = input(Color.BOLD + 'Please enter a Google Calendar email address:' + Color.END)
            cmd = Gam.gam + ' calendar ' + cal + ' showacl'
            os.system(cmd)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            calendar()
        elif selection == '2':  # Change permissions menu item
            cal = input(Color.BOLD + 'Please enter a Google Calendar email address:' + Color.END)
            ar = input(Color.BOLD + 'What would you like to do? [add | remove]' + Color.END)
            user = input(Color.BOLD + 'User to add to/remove from the Calendar:' + Color.END)
            if ar == 'add' or ar == 'Add' or ar == 'a':
                act = input(Color.BOLD + 'What permission would you like to grant? [read | edit | owner]' + Color.END)
                if act == 'read' or act == 'r' or act == 'Read':
                    cmd = Gam.gam + ' calendar ' + cal + ' add read ' + user
                    os.system(cmd)
                    print('\n')
                    time.sleep(2)
                    input(Color.GREEN + Msgs.cont + Color.END)
                    calendar()
                elif act == 'edit' or act == 'editor' or act == 'e' or act == 'Edit':
                    cmd = Gam.gam + ' calendar ' + cal + ' add editor ' + user
                    os.system(cmd)
                    print('\n')
                    time.sleep(2)
                    input(Color.GREEN + Msgs.cont + Color.END)
                    calendar()
                elif act == 'owner' or act == 'own' or act == 'o' or act == 'Owner':
                    cmd = Gam.gam + ' calendar ' + cal + ' add owner ' + user
                    os.system(cmd)
                    print('\n')
                    time.sleep(2)
                    input(Color.GREEN + Msgs.cont + Color.END)
                    calendar()
                else:
                    print(Color.RED + Msgs.err + Color.END)
                    print('\n')
                    time.sleep(2)
                    input(Color.GREEN + Msgs.cont + Color.END)
                    calendar()
            elif ar == 'rem' or ar == 'remove' or ar == 'r' or ar == 'Remove' or ar == 'Rem':
                cmd = Gam.gam + ' calendar ' + cal + ' delete user ' + user
                os.system(cmd)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                calendar()
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                calendar()
        elif selection == '3':  # Delete event menu item
            cal = input(Color.BOLD + 'Please enter a Google Calendar email address:' + Color.END)
            ev = input(Color.BOLD + 'Enter the event ID:' + Color.END)
            yn = input(Color.BOLD + 'Are you sure? THIS CANNOT BE UNDONE!! [y/N]' + Color.END)
            if yn == '' or yn == 'N' or yn == 'n' or yn == 'no' or yn == 'No':
                calendar()
            elif yn == 'y' or yn == 'Y' or yn == 'yes' or yn == 'Yes':
                cmd = Gam.gam + ' calendar ' + cal + ' deleteevent ' + ev + ' doit'
                os.system(cmd)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                calendar()
        elif selection == '4':  # List calendars menu item
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' show calendars'
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' show calendars'
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" show calendars'
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + ' show calendars'
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                calendar()
            os.system(cmd)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            calendar()
        elif selection == '5':  # Delete calendar menu item
            cal = input(Color.BOLD + 'Please enter a Google Calendar email address:' + Color.END)
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' delete calendar ' + cal
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' delete calendar ' + cal
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" delete calendar ' + cal
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + ' delete calendar ' + cal
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                calendar()
            os.system(cmd)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            calendar()
        elif selection == '6':  # Add calendar to user menu item
            cal = input(Color.BOLD + 'Please enter a Google Calendar email address:' + Color.END)
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' add calendar ' + cal + ' selected true hidden false'
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' add calendar ' + cal + ' selected true hidden false'
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" add calendar ' + cal + ' selected true hidden false'
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + ' add calendar ' + cal + ' selected true hidden false'
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                calendar()
            os.system(cmd)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            calendar()
        elif selection == '0':  # Back to main menu
            main_menu()
        else:  # Invalid menu selection error. Returns to current menu
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            calendar()


def drive():  # Drive Management Main Menu
    while True:
        print('\n')
        print(Color.PURPLE + 'Drive Management Menu:' + Color.END)
        print('\n')
        print("1)   Export a List of a User(s) Drive Files")
        print("2)   Upload a Local File To a Google Drive")
        print('3)   Download File(s) from a Google Drive')
        print("4)   Delete a User's Drive File")
        print("5)   View a Team Drive(s)")
        print('6)   Create a Team Drive')
        print("7)   Delete a Team Drive")
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)
        if selection == '1':  # Export file list menu item
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                user1 = user
                cmd = Gam.user + user + " show filelist allfields > " + user + "-filelist.csv"
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                user1 = user
                cmd = Gam.group + user + " show filelist allfields > " + user + "-filelist.csv"
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                user1 = user.split('/')[-1]
                cmd = Gam.ou + ' "' + user + '" show filelist allfields > ' + user1 + '-filelist.csv'
            elif who == 'all' or who == 'all users':
                user1 = 'AllUsers'
                cmd = Gam.all + 'show filelist allfields > AllUsers-filelist.csv'
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                drive()
            os.system(cmd)
            print(Color.YELLOW + '\nFile saved as ' + user1 + '-filelist.csv\n' + Color.END)
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            drive()
        elif selection == '2':  # Upload file menu item
            filename = input(Color.BOLD + "Please enter the full path to the file you wish to upload "
                                          "(Case Sensitive):  " + Color.END)
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + " add drivefile localfile " + filename
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + " add drivefile localfile " + filename
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + user + " add drivefile localfile " + filename
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + " add drivefile localfile " + filename
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                drive()
            os.system(cmd)
            print('\n')
            print("File uploaded successfully")
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            drive()
        elif selection == '3':  # Download Drive File(s)
            who = input(Color.BOLD + Msgs.ent + Color.END)
            quant = input(Color.BOLD + 'Single file or all files [single | all]:  ' + Color.END)
            loc = input(Color.BOLD + 'Enter the full path to the save location:  ' + Color.END)
            if quant == 'single':
                filename = input(Color.BOLD + 'Please enter the filename to download:  ' + Color.END)
                filename1 = 'drivefilename "' + filename + '"'
            elif quant == 'all':
                filename = 'query "!me! in owners" '
                filename1 = filename.replace("!", r"'")
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                drive()
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                user1 = user
                cmd = Gam.user + user + ' get drivefile ' + filename1 + ' targetfolder ' + loc + ' format microsoft'
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                user1 = user
                cmd = Gam.group + user + ' get drivefile ' + filename1 + ' targetfolder ' + loc + ' format microsoft'
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                user1 = user.split('/')[-1]
                cmd = Gam.ou + ' "' + user + '" get drivefile ' + filename1 + ' targetfolder ' + loc + \
                    ' format microsoft'
            elif who == 'all' or who == 'all users':
                user1 = 'AllUsers'
                cmd = Gam.all + ' get drivefile ' + filename1 + ' targetfolder ' + loc + ' format microsoft'
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                drive()
            os.system(cmd)
        elif selection == '4':  # Delete User's drive file
            user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
            file = input(Color.BOLD + 'Please enter the file ID to be deleted:  ' + Color.END)
            cmd = Gam.user + user + ' delete drivefile ' + file + ' purge'
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            drive()
        elif selection == '5':  # View Team Drives menu item
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' show teamdrives'
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' print teamdrives todrive'
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + '"' + user + '" print teamdrives todrive'
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + ' print teamdrives todrive'
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                drive()
            os.system(cmd)
            time.sleep(2)
            print(Color.RED + '\nIf you chose any entity other than "user", a file was uploaded to your '
                  'Google Drive with the Team Drive information.' + Color.END)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            drive()
        elif selection == '6':  # Create team drive for user menu item
            user = input(Color.BOLD + "Please enter a username: " + Color.END)
            name = input(Color.BOLD + 'What is the name of the Team Drive?' + Color.END)
            cmd = Gam.gam + ' user ' + user + ' add teamdrive "' + name + '"'
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            drive()
        elif selection == '7':  # Delete user's Team Drive menu item
            user = input(Color.BOLD + "Please enter a username: " + Color.END)
            dr_id = input(Color.BOLD + 'What is the Team Drive ID? (Not the name)' + Color.END)
            cmd = Gam.gam + ' user ' + user + ' delete teamdrive ' + dr_id
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            drive()
        elif selection == '0':  # Return to main menu
            main_menu()
        else:  # Invalid selection. Returns to this menu
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            drive()


def groups():  # Groups Management Main Menu
    while True:
        print('\n')
        print(Color.PURPLE + 'Group Management Menu:' + Color.END)
        print('\n')
        print('1)   Create a Group')
        print('2)   Rename a Group')
        print('3)   Add or Remove Group Member')
        print('4)   Update User Role in a Group')
        print('5)   Get Group Information')
        print('6)   Delete a Group')
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)

        if selection == '1':  # Create group menu item
            name = input(Color.BOLD + 'What is the name of the group to be created?' + Color.END)
            cmd = Gam.gam + ' create group ' + name + '@madisonrams.net'  # CHANGE THIS DOMAIN TO MATCH YOURS.
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            groups()
        elif selection == '2':  # Rename group menu item
            name = input(Color.BOLD + 'What is the email address of the group to be renamed?' + Color.END)
            ren = input(Color.BOLD + 'What is the new name(email address) of the group?' + Color.END)
            cmd = Gam.gam + ' update group ' + name + ' email ' + ren
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            groups()
        elif selection == '3':  # Add/Remove group member menu item
            name = input(Color.BOLD + 'What is the email address of the group?')
            ar = input(Color.BOLD + 'Add or Remove user? [add | remove]' + Color.END)
            user = input(Color.BOLD + 'What user?' + Color.END)
            if ar == 'add' or ar == 'a' or ar == 'Add' or ar == 'A':
                cmd = Gam.gam + ' update group ' + name + ' add member user ' + user
                os.system(cmd)
                time.sleep(2)
                print('\n')
                input(Color.GREEN + Msgs.cont + Color.END)
                groups()
            elif ar == 'remove' or ar == 'r' or ar == 'R' or ar == 'Remove' or ar == 'rem' or ar == 'Rem':
                cmd = Gam.gam + ' update group ' + name + ' remove user ' + user
                os.system(cmd)
                time.sleep(2)
                print('\n')
                input(Color.GREEN + Msgs.cont + Color.END)
                groups()
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                groups()
        elif selection == '4':  # Update user role menu item
            name = input(Color.BOLD + 'What is the email address of the group?')
            user = input(Color.BOLD + "What user's role will be modified? " + Color.END)
            perm = input(Color.BOLD + 'New role to assign (Must be in Lower Case): [owner | member | manager]'
                         + Color.END)
            cmd = Gam.gam + ' update group ' + name + ' update ' + perm + ' user ' + user
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            groups()
        elif selection == '5':  # Group information menu item
            name = input(Color.BOLD + 'What is the email address of the group?')
            cmd = Gam.gam + ' info group ' + name
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            groups()
        elif selection == '6':  # Delete group menu item
            name = input(Color.BOLD + 'What is the email address of the group?')
            cmd = Gam.gam + ' delete group ' + name
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            groups()
        elif selection == '0':  # Back to main menu
            main_menu()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            groups()


def classroom():  # Classroom Management Main Menu
    while True:
        print('\n')
        print(Color.PURPLE + 'Classroom Management Main Menu:' + Color.END)
        print('\n')
        print('1)   Manage Courses')
        print('2)   Manage Course Participants')
        print('3)   Manage Guardians')
        print('4)   Reports')
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)
        if selection == '1':  # Manage courses menu item. Calls classroom1() function.
            classroom1()
        elif selection == '2':  # Manage course participants menu item
            al = input(Color.BOLD + 'What is the course ID or alias?' + Color.END)
            act = input(Color.BOLD + 'Do you want to Add or Remove? (Must be lower case) [add | remove]' + Color.END)
            who = input(Color.BOLD + 'Is the person a student or a teacher? (Must be lower case) [student | teacher]'
                        + Color.END)
            user = input(Color.BOLD + "What is the person's username? " + Color.END)
            cmd = Gam.gam + ' course ' + al + ' ' + act + ' ' + who + ' ' + user + '@madisonrams.net'  # CHANGE THIS DOMAIN TO MATCH YOURS.
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            classroom()
        elif selection == '3':  # Manage guardians menu item. Calls classroom3() function.
            classroom3()
        elif selection == '4':  # Reports menu item. calls classroom4() function.
            classroom4()
        elif selection == '0':  # Back to main menu
            main_menu()
        else:  # Invalid selection error. Returns to current menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            classroom()


def devices():  # Device Management Main Menu
    while True:
        print('\n')
        print(Color.PURPLE + 'Chrome Device Management Main Menu:' + Color.END)
        print('\n')
        print('1)   Get Device ID of a Chrome OS Device')
        print('2)   Update Device Info')
        print('3)   Export Device Info')
        print('4)   Disable, De-provision, or Re-Enable a Device')
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)
        if selection == '1':  # Get ID menu item
            cr_id = input(Color.BOLD + 'Please enter the Chrome Device Serial Number (Case sensitive):' + Color.END)
            cmd = Gam.gam + ' print cros query "id:' + cr_id + '"'
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            devices()
        elif selection == '2':  # Update info menu item
            cr_id = input(Color.BOLD + 'Please enter the Chrome Device Serial Number:' + Color.END)
            cmd = Gam.gam + ' print cros query "id:' + cr_id + '" > id.txt'
            print('Looking up the device ID...')
            time.sleep(1)
            os.system(cmd)
            time.sleep(1)
            f = open('id.txt')
            id2 = f.readlines()[-1]
            act = input(Color.BOLD + 'What do you want to update?  [location | asset id]' + Color.END)
            if act == 'location' or act == 'Location' or act == 'loc' or act == 'Loc' or act == 'L' or act == 'l':
                loc = input(Color.BOLD + 'Enter new location:' + Color.END)
                cmd2 = '~/bin/gam/gam update cros ' + id2 + ' location "' + loc + '"'
                os.system(cmd2)
                time.sleep(2)
                print('\n')
                input(Color.GREEN + Msgs.cont + Color.END)
                f.close()
                os.system('rm -rf id.txt')
                devices()
            elif act == 'asset' or act == 'asset id' or act == 'assetid' or act == 'Asset' or act == 'Asset Id' or \
                    act == 'Asset ID' or act == 'Asset id' or act == 'A' or act == 'a':
                asset = input(Color.BOLD + 'Enter new Asset ID:' + Color.END)
                cmd2 = '~/bin/gam/gam update cros ' + id2 + ' assetid "' + asset + '"'
                os.system(cmd2)
                time.sleep(2)
                print('\n')
                input(Color.GREEN + Msgs.cont + Color.END)
                f.close()
                os.system('rm -rf id.txt')
                devices()
            else:
                print(Color.RED + Msgs.err + Color.END)
                time.sleep(1)
                f.close()
                os.system('rm -rf id.txt')
                input(Color.GREEN + Msgs.cont + Color.END)
                devices()
        elif selection == '3':  # Export device info menu item. Calls devices3() function.
            devices3()
        elif selection == '4':  # Disable/de-provision/re-enable menu item. Calls devices4() function.
            devices4()
        elif selection == '0':  # Back to main menu
            main_menu()
        else:  # Invalid Selection. Returns to current menu
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            devices()


def classroom1():
    while True:
        print('\n')
        print(Color.CYAN + 'Course Management Menu:' + Color.END)
        print('\n')
        print('1)   Create Course')
        print('2)   Update Course')
        print('3)   Get Course Info')
        print('4)   Delete Course')
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)
        if selection == '1':  # Create course menu item
            al = input(Color.BOLD + 'What is the course alias? (All lower lase, no spaces)')
            name = input(Color.BOLD + 'What is the course name?' + Color.END)
            sec = input(Color.BOLD + 'What is the course section? (Numbers only)')
            head = input(Color.BOLD + 'What is the heading?' + Color.END)
            room = input(Color.BOLD + 'What room is the class in? (No spaces')
            teach = input(Color.BOLD + "What is the teacher's username? " + Color.END)
            cmd = Gam.gam + ' create course alias ' + al + ' name "' + name + '" section ' + sec + ' heading "' \
                + head + '" room ' + room + ' teacher ' + teach + ' status ACTIVE'
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            classroom()
        elif selection == '2':  # Update course menu item. Calls classroom1_2() function
            classroom1_2()
        elif selection == '3':  # Course info menu item
            al = input(Color.BOLD + 'What is the course ID or alias?' + Color.END)
            cmd = Gam.gam + ' info course ' + al
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            classroom()
        elif selection == '4':  # Delete course menu item
            al = input(Color.BOLD + 'What is the course ID or alias?' + Color.END)
            yn = input(Color.BOLD + 'Are you sure? This action cannot be undone! [y/N]' + Color.END)
            if yn == 'y' or yn == 'yes' or yn == 'Y' or yn == 'Yes':
                cmd = Gam.gam + ' delete course ' + al
                os.system(cmd)
                time.sleep(2)
                print('\n')
                input(Color.GREEN + Msgs.cont + Color.END)
                classroom()
            elif yn == '' or yn == 'n' or yn == 'no' or yn == 'N' or yn == 'No':
                classroom()
            else:
                print(Color.RED + Msgs.err + Color.END)
                time.sleep(1)
                classroom()
        elif selection == '0':  # Back to classroom main menu
            classroom()
        else:  # Invalid selection. Returns to current menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            classroom1()


def classroom1_2():  # Classroom main menu option 1, submenu 2
    al = input(Color.BOLD + 'What is the course ID or alias that will be updated?' + Color.END)
    while True:
        print('\n')
        print(Color.YELLOW + 'Update What?' + Color.END)
        print('\n')
        print('1)   Name')
        print('2)   Section')
        print('3)   Heading')
        print('4)   Room')
        print('5)   Status')
        print('6)   Teacher')
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)
        if selection == '1':  # Update name menu item
            name = input(Color.BOLD + 'Enter the new name:' + Color.END)
            cmd = Gam.gam + ' update course ' + al + ' name ' + name
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            classroom1()
        elif selection == '2':  # Update section menu item
            name = input(Color.BOLD + 'Enter new section:' + Color.END)
            cmd = Gam.gam + ' update course ' + al + ' section ' + name
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            classroom1()
        elif selection == '3':  # Update heading menu item
            name = input(Color.BOLD + 'Enter new heading:' + Color.END)
            cmd = Gam.gam + ' update course ' + al + ' heading "' + name + '"'
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            classroom1()
        elif selection == '4':  # Update room menu item
            name = input(Color.BOLD + 'Enter new room:' + Color.END)
            cmd = Gam.gam + ' update course ' + al + ' room ' + name
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            classroom1()
        elif selection == '5':  # Update status menu item
            name = input(Color.BOLD + 'Enter new status (Must be uppercase): [ACTIVE | ARCHIVED | DECLINED]'
                         + Color.END)
            cmd = Gam.gam + ' update course ' + al + ' status ' + name
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            classroom1()
        elif selection == '6':  # Update teacher menu item
            name = input(Color.BOLD + 'Enter new teacher username:' + Color.END)
            cmd = Gam.gam + ' update course ' + al + ' owner ' + name
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            classroom1()
        elif selection == '0':  # Back to previous menu
            classroom1()
        else:  # Invalid selection. Returns to current menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            classroom1_2()


def classroom3():  # Classroom main menu option 3 submenu
    while True:
        print('\n')
        print(Color.CYAN + 'Guardian Management Menu:' + Color.END)
        print('\n')
        print('1)   Invite Guardian')
        print('2)   Delete Guardian')
        print("3)   View a Student's Guardian(s)")
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)
        if selection == '1':  # Invite guardian menu item
            stu = input(Color.BOLD + "What is the student's username? " + Color.END)
            guard = input(Color.BOLD + "What is the guardian's email address? " + Color.END)
            cmd = Gam.gam + ' create guardianinvite ' + guard + ' ' + stu + '@madisonrams.net'  # CHANGE THIS DOMAIN TO MATCH YOURS.
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            classroom3()
        elif selection == '2':  # Delete guardian menu item
            stu = input(Color.BOLD + "What is the student's username? " + Color.END)
            guard = input(Color.BOLD + "What is the guardian's email address? " + Color.END)
            cmd = Gam.gam + ' delete guardian ' + guard + ' ' + stu + '@madisonrams.net'  # CHANGE THIS DOMAIN TO MATCH YOURS.
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            classroom3()
        elif selection == '3':  # View a student's guardian(s) menu item
            stu = input(Color.BOLD + "What is the student's username? " + Color.END)
            cmd = Gam.gam + ' print guardians student ' + stu + '@madisonrams.net'  # CHANGE THIS DOMAIN TO MATCH YOURS.
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            classroom3()
        elif selection == '0':  # Back to Classroom main menu
            classroom()
        else:  # Invalid selection. Returns to current menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            classroom3()


def classroom4():  # Classroom main menu option 4 submenu
    while True:
        print('\n')
        print(Color.CYAN + 'Classroom Reports Menu:' + Color.END)
        print('\n')
        print("1)   View a Teacher's Courses")
        print("2)   View a Student's Courses")
        print("3)   View a Course's Participants")
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)
        if selection == '1':  # View teacher's courses menu item
            user = input(Color.BOLD + "What is the teacher's username? " + Color.END)
            cmd = Gam.gam + ' print courses teacher ' + user + '@madisonrams.net'  # CHANGE THIS DOMAIN TO MATCH YOURS.
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            classroom4()
        elif selection == '2':  # View student's courses menu item
            user = input(Color.BOLD + "What is the student's username? " + Color.END)
            cmd = Gam.gam + ' print courses student ' + user + '@madisonrams.net'  # CHANGE THIS DOMAIN TO MATCH YOURS.
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            classroom4()
        elif selection == '3':  # View course participants menu item
            al = input(Color.BOLD + 'What is the course ID or alias?' + Color.END)
            file = input(Color.BOLD + 'Output to a CSV file? [Y/n]')
            if file == '' or file == 'y' or file == 'Y' or file == 'yes' or file == 'Yes':
                cmd = Gam.gam + ' print course-participants course ' + al + ' > ' + al + '-participants.csv'
                os.system(cmd)
                time.sleep(2)
                print('\n')
                input(Color.GREEN + Msgs.cont + Color.END)
                classroom4()
            elif file == 'n' or file == 'N' or file == 'no' or file == 'No':
                cmd = Gam.gam + ' print course-participants course ' + al
                os.system(cmd)
                time.sleep(2)
                print('\n')
                input(Color.GREEN + Msgs.cont + Color.END)
                classroom4()
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                classroom4()
        elif selection == '0':  # Back to classroom main menu
            classroom()
        else:  # Invalid selection. Returns to current menu
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            classroom4()


def devices3():  # Devices main menu option 3 submenu
    while True:
        print('\n')
        print(Color.CYAN + 'Chrome Device Info Menu:' + Color.END)
        print('\n')
        print('1)   View Single Device Info')
        print('2)   Export All Devices in an OU')
        print('3)   Export All Devices')
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)
        if selection == '1':  # View device info menu item
            cr_id = input(Color.BOLD + 'Please enter the Chrome Device Serial Number (Case sensitive):' + Color.END)
            cmd = Gam.gam + ' print cros query "id:' + cr_id + '" > id.txt'
            print('Looking up the device ID...')
            os.system(cmd)
            time.sleep(1)
            f = open('id.txt')
            id2 = f.readlines()[-1]
            cmd2 = '~/bin/gam/gam info cros ' + id2 + ' full'
            os.system(cmd2)
            time.sleep(2)
            f.close()
            os.system('rm -rf id.txt')
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            devices3()
        elif selection == '2':  # Export devices in ou menu item
            ou = input(Color.BOLD + 'Please enter the full path of the OU you wish to export (Case Sensitive):'
                       + Color.END)
            ou2 = ou.split("/")[-1]
            cmd = Gam.gam + ' print cros full limit_to_ou "' + ou + '" > ' + ou2 + '-export.csv'
            os.system(cmd)
            time.sleep(1)
            print('Exported as ' + ou2 + '-export.csv')
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            devices3()
        elif selection == '3':  # Export all devices menu item
            cmd = Gam.gam + ' print cros full > all-devices.csv'
            os.system(cmd)
            time.sleep(1)
            print('Device list exported as all-devices.csv')
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            devices3()
        elif selection == '0':  # Back to devices main menu
            devices()
        else:  # Invalid selection. Returns to current menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            devices3()


def devices4():  # Devices main menu option 4 submenu
    while True:
        print('\n')
        print(Color.CYAN + 'Disable/De-Provision/Re-Enable Menu:' + Color.END)
        print('\n')
        print('1)   Disable')
        print('2)   Re-Enable')
        print('3)   De-Provision')
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)
        if selection == '1':  # Disable menu item
            cr_id = input(Color.BOLD + 'Please enter the Chrome Device Serial Number (Case sensitive):' + Color.END)
            cmd = Gam.gam + ' print cros query "id:' + cr_id + '" > id.txt'
            print('Looking up the device ID...')
            os.system(cmd)
            time.sleep(1)
            f = open('id.txt')
            id2 = f.readlines()[-1]
            cmd2 = '~/bin/gam/gam update cros ' + id2 + ' action disable acknowledge_device_touch_requirement'
            os.system(cmd2)
            time.sleep(2)
            f.close()
            os.system('rm -rf id.txt')
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            devices4()
        elif selection == '2':  # Re-enable menu item
            cr_id = input(Color.BOLD + 'Please enter the Chrome Device Serial Number (Case sensitive):' + Color.END)
            cmd = Gam.gam + ' print cros query "id:' + cr_id + '" > id.txt'
            print('Looking up the device ID...')
            os.system(cmd)
            time.sleep(1)
            f = open('id.txt')
            id2 = f.readlines()[-1]
            cmd2 = '~/bin/gam/gam update cros ' + id2 + ' action reenable acknowledge_device_touch_requirement'
            os.system(cmd2)
            time.sleep(2)
            f.close()
            os.system('rm -rf id.txt')
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            devices4()
        elif selection == '3':  # Deprovision menu item. Calls devices4_3() function
            devices4_3()
        elif selection == '0':  # Back to devices main menu
            devices()
        else:  # Invalid selection. Returns to current menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            devices4()


def devices4_3():  # Devices Main menu option 4. submenu 3
    while True:
        print('\n')
        print(Color.DARKCYAN + 'De-Provision Menu:' + Color.END)
        print('\n')
        print('1)   De-Provision to Replace With Same Model')
        print('2)   De-Provision to Replace With Different Model')
        print('3)   De-Provision to Retire')
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)
        if selection == '1':  # Replace with same model menu item
            cr_id = input(Color.BOLD + 'Please enter the Chrome Device Serial Number (Case sensitive):' + Color.END)
            cmd = Gam.gam + ' print cros query "id:' + cr_id + '" > id.txt'
            print('Looking up the device ID...')
            os.system(cmd)
            time.sleep(1)
            f = open('id.txt')
            id2 = f.readlines()[-1]
            cmd2 = '~/bin/gam/gam update cros ' + id2 + \
                   ' action deprovision_same_model_replace acknowledge_device_touch_requirement'
            os.system(cmd2)
            time.sleep(2)
            f.close()
            os.system('rm -rf id.txt')
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            devices4_3()
        elif selection == '2':  # Replace with diff model menu item
            cr_id = input(Color.BOLD + 'Please enter the Chrome Device Serial Number (Case sensitive):' + Color.END)
            cmd = Gam.gam + ' print cros query "id:' + cr_id + '" > id.txt'
            print('Looking up the device ID...')
            os.system(cmd)
            time.sleep(1)
            f = open('id.txt')
            id2 = f.readlines()[-1]
            cmd2 = '~/bin/gam/gam update cros ' + id2 + \
                   ' action deprovision_different_model_replace acknowledge_device_touch_requirement'
            os.system(cmd2)
            time.sleep(2)
            f.close()
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            devices4_3()
        elif selection == '3':  # Retire menu item
            cr_id = input(Color.BOLD + 'Please enter the Chrome Device Serial Number (Case sensitive):' + Color.END)
            cmd = Gam.gam + ' print cros query "id:' + cr_id + '" > id.txt'
            print('Looking up the device ID...')
            os.system(cmd)
            time.sleep(1)
            f = open('id.txt')
            id2 = f.readlines()[-1]
            cmd2 = '~/bin/gam/gam update cros ' + id2 + \
                   ' action deprovision_retiring_device acknowledge_device_touch_requirement'
            os.system(cmd2)
            time.sleep(2)
            f.close()
            os.system('rm -rf id.txt')
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            devices4_3()
        elif selection == '0':  # Return to previous menu
            devices4()
        else:  # Invalid selection. Returns to current menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            devices4_3()


def email():  # Email Management main menu
    while True:
        print('\n')
        print(Color.PURPLE + 'Email Management Menu:' + Color.END)
        print('\n')
        print('1)   User Signature and Vacation Message')
        print('2)   Labels and Filters')
        print('3)   IMAP and POP Settings')
        print('4)   Send As Settings')
        print('5)   Profile Settings')
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)

        if selection == '1':  # Edit User's signature
            email1()
        elif selection == '2':  # Edit a user's labels and filters
            email2()
        elif selection == '3':  # IMAP and POP settings
            email3()
        elif selection == '4':  # Send As address settings
            email4()
        elif selection == '5':  # Profile Settings
            email5()
        elif selection == '0':  # Back to main menu
            main_menu()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            email()


def email1():  # Email main menu option 1 submenu
    while True:
        print('\n')
        print(Color.CYAN + 'User Signature Management Menu:' + Color.END)
        print('\n')
        print('1)   Set User Signature From Text File')
        print('2)   Set User Signature From HTML File')
        print('3)   Set User Signature Manually')
        print("4)   View a User(s) Signature")
        print("5)   Set a User(s) Vacation Responder")
        print("6)   Turn off a User(s) Vacation Responder")
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)

        if selection == '1':  # Set sig from txt file
            txt = input(Color.BOLD + 'Please enter the full path to the text file to read:' + Color.END)
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' signature file ' + txt
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + '  signature file ' + txt
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" signature file ' + txt
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + '  signature file ' + txt
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email1()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email1()
        elif selection == '2':  # Set sig from html file
            txt = input(Color.BOLD + 'Please enter the full path to the html file to read:' + Color.END)
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' signature file ' + txt + ' html'
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + '  signature file ' + txt + ' html'
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" signature file ' + txt + ' html'
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + '  signature file ' + txt + ' html'
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email1()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email1()
        elif selection == '3':  # Set sig manually
            print(Color.YELLOW + 'Line breaks must be designated by <br>. EX: Acme Inc<br>123 Main Ave<br>'
                                 'http://www.acme.com' + Color.END)
            time.sleep(1)
            txt = input(Color.BOLD + 'Please enter the full text of the signature:' + Color.END)
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' signature  "' + txt + '"'
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + '  signature  "' + txt + '"'
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" signature  "' + txt + '"'
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + '  signature  "' + txt + '"'
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email1()

            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email1()
        elif selection == '4':  # View user's signature
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' show signature format'
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' show signature format'
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" show signature format'
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + ' show signature format'
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email1()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email1()
        elif selection == '5':  # Set vacation responder
            sub = input(Color.BOLD + 'Please enter a message subject: ' + Color.END)
            print(Color.YELLOW + r'Line breaks must be designated using "\n".' + Color.END)
            mes = input(Color.BOLD + 'Please enter the vacation message: ' + Color.END)
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' vacation on subject "' + sub + '" message "' + mes + '"'
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' vacation on subject "' + sub + '" message "' + mes + '"'
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" vacation on subject "' + sub + '" message "' + mes + '"'
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + ' vacation on subject "' + sub + '" message "' + mes + '"'
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email1()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email1()
        elif selection == '6':  # Turn off responder
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' vacation off'
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' vacation off'
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" vacation off'
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + ' vacation off'
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email1()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email1()
        elif selection == '0':  # Back to main menu
            email()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            email1()


def email2():  # Email main menu option 2 menu
    while True:
        print('\n')
        print(Color.CYAN + 'Labels and Filters Menu:' + Color.END)
        print('\n')
        print('1)   Create a Label')
        print("2)   View User(s) Labels")
        print('3)   Delete a Label')
        print('4)   Create a Filter')
        print("5)   View User(s) Filters")
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)

        if selection == '1':  # Create a label
            lab = input(Color.BOLD + 'Please enter a name for the label: ' + Color.END)
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' label "' + lab + '"'
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' label "' + lab + '"'
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" label "' + lab + '"'
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + ' label "' + lab + '"'
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email2()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email2()
        elif selection == '2':  # View labels
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' show labels'
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' show labels'
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" show labels'
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + ' show labels'
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email2()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email2()
        elif selection == '3':  # Delete Label
            lab = input(Color.BOLD + 'Please enter the label name: ' + Color.END)
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' delete label "' + lab + '"'
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' delete label "' + lab + '"'
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" delete label "' + lab + '"'
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + ' delete label "' + lab + '"'
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email2()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email2()
        elif selection == '4':  # Create Filter
            email2_4()
        elif selection == '5':  # View user's filters
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' show filters'
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' show filters'
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" show filters'
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + ' show filters'
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email2()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email2()
        elif selection == '0':  # Back to main menu
            email()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            email2()


def email2_4():  # create filter menu
    while True:
        print('\n')
        print(Color.DARKCYAN + 'Filter Criteria:' + Color.END)
        print('\n')
        print('1)   "FROM" Address Only')
        print('2)   "FROM" Address and Subject')
        print('3)   Subject Only')
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)

        if selection == '1':  # Filter by from address only
            eml = input(Color.BOLD + 'Please enter an email address to filter on: ' + Color.END)
            print('Separate action using a space')
            act = input(Color.BOLD + 'What action to take? [markread | archive | star | trash | neverspam] '
                        + Color.END)
            lab = input(Color.BOLD + 'Please enter a label for the filtered messages: ' + Color.END)
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' filter from ' + eml + ' label "' + lab + '" ' + act
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' filter from ' + eml + ' label "' + lab + '" ' + act
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" filter from ' + eml + ' label "' + lab + '" ' + act
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + ' filter from ' + eml + ' label "' + lab + '" ' + act
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email2_4()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email2_4()
        elif selection == '2':  # Filter by address and subject
            eml = input(Color.BOLD + 'Please enter an email address to filter on: ' + Color.END)
            sub = input(Color.BOLD + 'Please enter a subject to filter on: ' + Color.END)
            print('Separate action using a space')
            act = input(Color.BOLD + 'What action to take? [markread | archive | star | trash | neverspam] '
                        + Color.END)
            lab = input(Color.BOLD + 'Please enter a label for the filtered messages: ' + Color.END)
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' filter from ' + eml + ' subject "' + sub + '" label "' + lab + '" ' + act
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' filter from ' + eml + ' subject "' + sub + '" label "' + lab + '" ' + act
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" filter from ' + eml + ' subject "' + sub + '" label "' + lab + '" '\
                    + act
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + ' filter from ' + eml + ' subject "' + sub + '" label "' + lab + '" ' + act
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email2_4()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email2_4()
        elif selection == '3':  # Filter by subject
            sub = input(Color.BOLD + 'Please enter a subject to filter on: ' + Color.END)
            print('Separate action using a space')
            act = input(Color.BOLD + 'What action to take? [markread | archive | star | trash | neverspam] '
                        + Color.END)
            lab = input(Color.BOLD + 'Please enter a label for the filtered messages: ' + Color.END)
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' filter subject ' + sub + ' label "' + lab + '" ' + act
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' filter subject ' + sub + ' label "' + lab + '" ' + act
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" filter subject ' + sub + ' label "' + lab + '" ' + act
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + ' filter subject ' + sub + ' label "' + lab + '" ' + act
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email2_4()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email2_4()
        elif selection == '0':  # Back to main menu
            email2()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            email2_4()


def email3():  # Pop and imap settings
    while True:
        print('\n')
        print(Color.CYAN + 'IMAP and POP Settings:' + Color.END)
        print('\n')
        print('1)   Turn IMAP/POP On or Off for a User')
        print('2)   Show IMAP/POP status for a User')
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)

        if selection == '1':  # IMAP/POP on/off
            prot = input(Color.BOLD + 'What protocol? [pop | imap] ' + Color.END)
            act = input(Color.BOLD + 'Turn ON or OFF? [on | off] ' + Color.END)
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' ' + prot + ' ' + act
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' ' + prot + ' ' + act
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" ' + prot + ' ' + act
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + ' ' + prot + ' ' + act
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email3()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email3()
        elif selection == '2':  # IMAP/POP status
            prot = input(Color.BOLD + 'What protocol? [pop | imap] ' + Color.END)
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' show ' + prot
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' show ' + prot
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" show ' + prot
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + ' show ' + prot
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email3()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email3()
        elif selection == '0':  # Back to main menu
            email()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            email3()


def email4():  # Send As settings
    while True:
        print('\n')
        print(Color.CYAN + 'Send As Settings Menu:' + Color.END)
        print('\n')
        print('1)   Add Send As Address')
        print('2)   Update Send As Address')
        print('3)   Delete Send As Address')
        print('4)   Show Send As Addresses for a User')
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)

        if selection == '1':  # Add send as address
            usr = input(Color.BOLD + 'Please enter a username: ' + Color.END)
            eml = input(Color.BOLD + 'Please enter an email address to send as: ' + Color.END)
            nm = input(Color.BOLD + 'Please Enter a name for the email address (ex. John Smith): ' + Color.END)
            cmd = Gam.gam + ' user ' + usr + ' sendas ' + eml + ' ' + nm + ' replyto ' + eml + ' treatasalias true'
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email4()
        elif selection == '2':  # Update send as
            usr = input(Color.BOLD + 'Please enter a username: ' + Color.END)
            eml = input(Color.BOLD + 'Please enter the send as email address: ' + Color.END)
            nm = input(Color.BOLD + 'Please Enter an updated name for the email address (ex. John Smith): ' + Color.END)
            cmd = Gam.gam + ' user ' + usr + ' update sendas ' + eml + ' name ' + nm + ' replyto ' + eml + \
                ' treatasalias true'
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email4()
        elif selection == '3':  # delete send as
            usr = input(Color.BOLD + 'Please enter a username: ' + Color.END)
            eml = input(Color.BOLD + 'Please enter the send as email address: ' + Color.END)
            cmd = Gam.gam + ' user ' + usr + ' delete sendas ' + eml
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email4()
        elif selection == '4':  # View send as
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                user1 = user
                cmd = Gam.user + user + ' print sendas > ' + user + '-sendas.csv'
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                user1 = user
                cmd = Gam.group + user + ' print sendas > ' + user + '-sendas.csv'
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                user1 = user.split('/')[-1]
                cmd = Gam.ou + ' "' + user + '" print sendas > ' + user1 + '-sendas.csv'
            elif who == 'all' or who == 'all users':
                user1 = 'AllUsers'
                cmd = Gam.all + ' print sendas > ' + user1 + '-sendas.csv'
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email4()
            os.system(cmd)
            print(Color.YELLOW + '\nFile saved as ' + user1 + '-sendas.csv\n' + Color.END)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email4()
        elif selection == '0':  # Back to main menu
            email()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            email4()


def email5():  # Profile Settings
    while True:
        print('\n')
        print(Color.CYAN + 'Profile Settings Menu:' + Color.END)
        print('\n')
        print('1)   Add/Update User(s) Profile Photo')
        print("2)   Download User(s) Profile Photo")
        print("3)   Delete User(s) Profile Photo")
        print("4)   Show User(s) Gmail Profile")
        print("5)   Show User(s) Google+ Profile")
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)

        if selection == '1':  # Update profile photo
            print(Color.YELLOW + 'Photos must be jpg format, and the file path and name are case sensitive.'
                  + Color.END)
            fn = input(Color.BOLD + 'Please enter the full path to the photo you wish to upload: ' + Color.END)
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' update photo ' + fn
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' update photo ' + fn
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" update photo ' + fn
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + ' update photo ' + fn
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email5()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email5()
        elif selection == '2':  # Download profile photo
            fn = input(Color.BOLD + 'Please enter the full path to a folder to save the photo(s): ' + Color.END)
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' get photo targetfolder ' + fn
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' get photo targetfolder ' + fn
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" get photo targetfolder ' + fn
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + ' get photo targetfolder ' + fn
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email5()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email5()
        elif selection == '3':  # Delete profile photo
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' delete photo'
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' delete photo'
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                cmd = Gam.ou + ' "' + user + '" delete photo'
            elif who == 'all' or who == 'all users':
                cmd = Gam.all + ' delete photo'
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email5()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email5()
        elif selection == '4':  # Show Gmail profile
            who = input(Color.BOLD + Msgs.ent + Color.END)
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' show gmailprofile > ' + user + '-gmail-profile.csv'
                user1 = user
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' show gmailprofile > ' + user + '-gmail-profile.csv'
                user1 = user
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                user1 = user.split('/')[-1]
                cmd = Gam.ou + ' "' + user + '" show gmailprofile > ' + user1 + '-gmail-profile.csv'
            elif who == 'all' or who == 'all users':
                user1 = 'AllUsers'
                cmd = Gam.all + ' show gmailprofile > ' + user1 + '-gmail-profile.csv'
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email5()
            os.system(cmd)
            print(Color.YELLOW + '\nFile saved as ' + user1 + '-gmail-profile.csv\n' + Color.END)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email5()
        elif selection == '4':  # Show Google+ profile
            if who == 'user':
                user = input(Color.BOLD + 'Please enter a username:  ' + Color.END)
                cmd = Gam.user + user + ' show gplusprofile > ' + user + '-gplus-profile.csv'
                user1 = user
            elif who == 'group':
                user = input(Color.BOLD + 'Please enter a group name:  ' + Color.END)
                cmd = Gam.group + user + ' show gplusprofile > ' + user + '-gplus-profile.csv'
                user1 = user
            elif who == 'ou':
                user = input(Color.BOLD + 'Please enter an OU (Case Sensitive, Full Path):  ' + Color.END)
                user1 = user.split('/')[-1]
                cmd = Gam.ou + ' "' + user + '" show gplusprofile > ' + user1 + '-gplus-profile.csv'
            elif who == 'all' or who == 'all users':
                user1 = 'AllUsers'
                cmd = Gam.all + ' show gplusprofile > ' + user1 + '-gplus-profile.csv'
            else:
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                email5()
            os.system(cmd)
            print(Color.YELLOW + '\nFile saved as ' + user1 + '-gplus-profile.csv\n' + Color.END)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            email5()
        elif selection == '0':  # Back to main menu
            email()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            email5()


def bulk():  # Bulk operations main menu
    while True:
        print('\n')
        print(Color.PURPLE + 'Bulk Operations Menu:' + Color.END)
        print('\n')
        print(Color.RED + 'WARNING: Using these will affect multiple users. Some actions are unrecoverable.'
              ' PROCEED WITH CAUTION! ' + Color.END)
        print('\n')
        print('1)   GAM Batch Mode Using CSV Files')
        print('2)   GAM Batch Mode Using Text Files')
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)

        if selection == '1':  # CSV Batch Mode
            csv()
        elif selection == '2':  # Batch file mode
            batch()
        elif selection == '0':  # Back to main menu
            main_menu()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            bulk()


def batch():  # GAM batch file commands
    print(Color.YELLOW + '\nThe file to be used in this batch mode must have a GAM command, one per line,'
          ' with correct syntax\n' + Color.END)
    print(Color.RED + 'If the syntax in your file is incorrect, the entire operation will fail.\n' + Color.END)
    file = input(Color.BOLD + 'Please enter the full path of the file to be used: ' + Color.END)
    cmd = Gam.gam + ' batch ' + file
    os.system(cmd)
    time.sleep(2)
    print('\n')
    input(Color.GREEN + Msgs.cont + Color.END)
    bulk()


def csv():  # GAM CSV file batch mode
    print(Color.UNDERLINE + '\nCOMING SOON!\n' + Color.END)
    time.sleep(2)
    print('\n')
    input(Color.GREEN + Msgs.cont + Color.END)
    bulk()


def vault():  # Vault Management
    while True:
        print('\n')
        print(Color.PURPLE + 'Vault Management Menu:' + Color.END)
        print('\n')
        print('1)   Create Matter')
        print('2)   Update Matter')
        print('3)   Retrieve Matter Info')
        print('4)   Create Hold')
        print('5)   Update Hold')
        print('6)   Retrieve Hold Info')
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)

        if selection == '1':  # Create Matter
            name = input(Color.BOLD + 'Please enter a name for the matter:  ' + Color.END)
            desc = input(Color.BOLD + 'Please enter a short description for the matter:  ' + Color.END)
            collab = input(Color.BOLD + 'Would you like to add collaborators [y/N]?  ' + Color.END)
            if collab == 'n' or collab == 'no':
                cmd = Gam.cr + 'vaultmatter name "' + name + '" description "' + desc + '"'
            elif collab == 'y' or collab == 'yes':
                collab1 = input(Color.BOLD + ' Please enter collaborator email address(es), '
                                'separated by commas without spaces:  ')
                cmd = Gam.cr + 'vaultmatter name "' + name + '" description "' + desc + '" collaborators "' \
                    + collab1 + '"'
            else:  # Invalid selection. returns to current menu.
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                vault()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            vault()
        elif selection == '2':  # Update Matter
            vault2()
        elif selection == '3':  # Retrieve Matter Info
            name = input(Color.BOLD + 'Please enter the matter name:  ' + Color.END)
            cmd = Gam.info + ' vaultmatter "' + name + '"'
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            vault()
        elif selection == '4':  # Create Hold
            matname = input(Color.BOLD + 'Please enter the matter name:  ' + Color.END)
            name = input(Color.BOLD + 'Please enter a name for the hold:  ' + Color.END)
            corpus = input(Color.BOLD + 'Hold what items? [mail | drive]  ' + Color.END)
            wt = input(Color.BOLD + 'Individual users or OU [user | ou]?  ' + Color.END)
            start = input(Color.BOLD + 'What is the start time [YYYY-MM-DD]?  ' + Color.END)
            end = input(Color.BOLD + 'What is the end time [YYYY-MM-DD]?  ' + Color.END)
            if wt == 'user':
                user = input(Color.BOLD + 'Please enter 1 or more email addresses separated by commas (no spaces):  '
                             + Color.END)
                cmd = Gam.cr + 'vaulthold matter "' + matname + '" name "' + name + '" corpus ' + corpus + \
                    ' accounts "' + user + '" starttime ' + start + ' endtime ' + end
            elif wt == 'ou':
                ou = input(Color.BOLD + 'Please enter an ou (Case Sensitive):  ' + Color.END)
                cmd = Gam.cr + 'vaulthold matter "' + matname + '" name "' + name + '" corpus ' + corpus + \
                    ' orgunit "' + ou + '" starttime ' + start + ' endtime ' + end
            else:  # Invalid selection. returns to current menu.
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                vault()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            vault()
        elif selection == '5':  # Update Hold
            vault5()
        elif selection == '6':  # Hold Info
            matname = input(Color.BOLD + 'Please enter the matter name:  ' + Color.END)
            name = input(Color.BOLD + 'Please enter the hold name:  ' + Color.END)
            cmd = Gam.info + 'vaulthold "' + name + '" matter "' + matname + '"'
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            vault()
        elif selection == '0':  # Back to main menu
            main_menu()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            vault()


def vault2():  # Update Vault matter menu
    while True:
        print('\n')
        print(Color.CYAN + 'Update Matter Menu:' + Color.END)
        print('\n')
        print('1)   Update Collaborators')
        print('2)   Update Description')
        print('3)   Close/Re-open Matter ')
        print('4)   Delete/Undelete Matter')
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)

        if selection == '1':  # Update Collaborators
            name = input(Color.BOLD + 'Please enter the matter name:  ' + Color.END)
            ar = input(Color.BOLD + 'Add or remove collaborators [add | remove]?  ' + Color.END)
            coll = input(Color.BOLD + ' Collaborator(s) to add/remove, comma separated(no spaces):  ' + Color.END)
            cmd = Gam.up + 'vaultmatter "' + name + '" ' + ar + 'collaborators "' + coll + '"'
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            vault2()
        elif selection == '2':  # Update description
            name = input(Color.BOLD + 'Please enter the matter name:  ' + Color.END)
            desc = input(Color.BOLD + 'Please enter a short description:  ' + Color.END)
            cmd = Gam.up + 'vaultmatter "' + name + '" description "' + desc + '"'
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            vault2()
        elif selection == '3':  # Close/Reopen matter
            name = input(Color.BOLD + 'Please enter the matter name:  ' + Color.END)
            co = input(Color.BOLD + 'Close or Re-open matter [close | reopen]?  ' + Color.END)
            cmd = Gam.up + 'vaultmatter "' + name + '" action ' + co
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            vault2()
        elif selection == '4':  # Delete/Undelete matter
            print(Color.RED + 'Matters must be closed before they can be deleted!\n' + Color.END)
            name = input(Color.BOLD + 'Please enter the matter name:  ' + Color.END)
            co = input(Color.BOLD + 'Delete or Undelete matter [delete | undelete]?  ' + Color.END)
            cmd = Gam.up + 'vaultmatter "' + name + '" action ' + co
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            vault2()
        elif selection == '0':  # Back to previous menu
            vault()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            vault2()


def vault5():  # Update vault hold menu
    while True:
        print('\n')
        print(Color.CYAN + 'Update Hold Menu:' + Color.END)
        print('\n')
        print('1)   Update Org Unit/User Account(s)')
        print('2)   Update Start/End time')
        print('3)   Delete Hold')
        print('0)   Back')
        print('\n')

        selection = input(Color.BOLD + Msgs.choose + Color.END)

        if selection == '1':  # Update ou
            matname = input(Color.BOLD + 'Please enter the matter name:  ' + Color.END)
            name = input(Color.BOLD + 'Please enter the hold name:  ' + Color.END)
            wt = input(Color.BOLD + 'Individual user(s) or OU [user | ou]?  ' + Color.END)
            if wt == 'user':
                user = input(Color.BOLD + 'Please enter 1 or more email addresses separated by commas (no spaces):  '
                             + Color.END)
                ar = input(Color.BOLD + 'Add or remove [add | remove]?  ' + Color.END)
                cmd = Gam.up + 'vaulthold "' + name + '" matter "' + matname + '" ' + ar + 'accounts "' + user + '"'
            elif wt == 'ou':
                ou = input(Color.BOLD + 'Please enter an ou (Case Sensitive):  ' + Color.END)
                cmd = Gam.up + 'vaulthold "' + name + '" matter "' + matname + '"  orgunit "' + ou + '"'
            else:  # Invalid selection. returns to current menu.
                print(Color.RED + Msgs.err + Color.END)
                print('\n')
                time.sleep(2)
                input(Color.GREEN + Msgs.cont + Color.END)
                vault5()
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            vault5()
        elif selection == '2':  # Update start/end
            matname = input(Color.BOLD + 'Please enter the matter name:  ' + Color.END)
            name = input(Color.BOLD + 'Please enter the hold name:  ' + Color.END)
            start = input(Color.BOLD + 'What is the new start time [YYYY-MM-DD]?  ' + Color.END)
            end = input(Color.BOLD + 'What is the new end time [YYYY-MM-DD]?  ' + Color.END)
            cmd = Gam.up + 'vaulthold "' + name + '" matter "' + matname + '" starttime ' + start + ' endtime ' + end
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            vault5()
        elif selection == '3':  # Delete Hold
            matname = input(Color.BOLD + 'Please enter the matter name:  ' + Color.END)
            name = input(Color.BOLD + 'Please enter the hold name:  ' + Color.END)
            cmd = Gam.de + 'vaulthold "' + name + '" matter "' + matname + '"'
            os.system(cmd)
            time.sleep(2)
            print('\n')
            input(Color.GREEN + Msgs.cont + Color.END)
            vault5()
        elif selection == '0':  # Back to previous menu
            vault()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED + Msgs.err + Color.END)
            print('\n')
            time.sleep(2)
            input(Color.GREEN + Msgs.cont + Color.END)
            vault5()


cred()
main_menu()
