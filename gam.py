#!/usr/bin/env python3

# MIT License

# Copyright (c) 2020 Luke Strohm

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# This program relies on GAMADV-XTD3 to function. You must install and
# configure it before using this program.

# See lines 689, 785, 1013, 1023, 1032, 1058, and 1067
# for a domain specific setting that will need changed.


import os
import time


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
    g = '~/bin/gamadv-xtd3/gam '
    u = '~/bin/gamadv-xtd3/gam user '
    gr = '~/bin/gamadv-xtd3/gam group '
    ou = '~/bin/gamadv-xtd3/gam ou '
    a = '~/bin/gamadv-xtd3/gam all users '
    up = '~/bin/gamadv-xtd3/gam update '
    add = 'add'
    remove = 'remove'
    de = '~/bin/gamadv-xtd3/gam delete '
    c = '~/bin/gamadv-xtd3/gam create '
    i = '~/bin/gamadv-xtd3/gam info '


class Msgs:  # Various repeated messages
    cont = 'Press ENTER to Continue...'
    err = 'Invalid Option Selected!'
    choose = 'Please Choose an Option:  '
    ent = 'Entity to apply to: [user | group | ou | all users]  '


def cred():
    print(Color.DARKCYAN+'\n' +
          '*********************************\n' +
          '*     Python 3 Frontend for     *\n' +
          '*  GAMADV-XTD3 by Ross Scroggs  *\n' +
          '*                               *\n' +
          '*   Written and maintained by   *\n' +
          '*          Luke Strohm          *\n' +
          '*     strohm.luke@gmail.com     *\n' +
          '*  https://github.com/strohmy86 *\n' +
          '*                               *\n' +
          '*********************************\n' +
          '\n'+Color.END)


def main_menu():  # Main Menu
    while True:
        print(Color.PURPLE+'\nMain Menu:\n'+Color.END)
        print('1)   User Management')
        print('2)   Calendar Management')
        print('3)   Drive Management')
        print('4)   Group Management')
        print('5)   Classroom Management')
        print('6)   Device Management')
        print('7)   Email Management')
        print('8)   Bulk Operations')
        print('9)   Vault Management')
        print('\n0)   Exit\n')
        selection1 = input(Color.BOLD+Msgs.choose+Color.END)
        if selection1 == '0':
            exit()
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
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(1)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)


def users():  # User Management Main Menu
    while True:
        print(Color.PURPLE+'\nUser Management Menu:\n'+Color.END)
        print('1)   User Information')
        print('2)   Export List of All Users')
        print('3)   Activate Suspended User')
        print('4)   Suspend User')
        print('5)   Transfer Drive Files')
        print('6)   Manage Verification Codes')
        print('7)   Manage User(s) Photo')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # User Info menu item
            username = input(Color.BOLD+'Please enter a username: ' +
                             Color.END)
            cmd = Gam.g+'info user '+username
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            users()
        elif selection == '2':  # Export users menu item
            cmd = Gam.g+'redirect csv ~/Userlist.csv multiprocess print ' +\
                'users allfields'
            os.system(cmd)
            print(Color.YELLOW+'\nUserlist.csv saved.'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            users()
        elif selection == '3':  # Activate suspended user menu item
            username = input(Color.BOLD+'Please enter a username: ' +
                             Color.END)
            cmd = Gam.g+' update user '+username+' suspended off'
            cmd2 = '~/bin/gamadv-xtd3/gam info user '+username
            os.system(cmd)
            time.sleep(2)
            os.system(cmd2)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            users()
        elif selection == '4':  # Suspend a user menu item
            username = input(Color.BOLD+'Enter a username: '+Color.END)
            cmd = Gam.g+' update user '+username+' suspended on'
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            users()
        elif selection == '5':  # Transfer files from one user to another
            user = input(Color.BOLD+'Please enter username of source ' +
                         'drive: '+Color.END)
            user2 = input(Color.BOLD+'Please enter username of destination' +
                          ' drive:  '+Color.END)
            cmd = Gam.c+'datatransfer '+user+' gdrive '+user2 +\
                ' privacy_level shared,private'
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            users()
        elif selection == '6':  # Manage Verificaion Codes
            user = input(Color.BOLD+'Enter a username: '+Color.END)
            act = input(Color.BOLD+'Show or Delete Codes?  [show | del]  ' +
                        Color.END)
            cmd = Gam.u+user+' '+act+' backupcodes'
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            users()
        elif selection == '7':  # Manage Photo
            users7()
        elif selection == '0':  # Back to main menu
            main_menu()
        else:  # Invalid selection. Return to this menu.
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            users()


def users7():  # Photo Management
    while True:
        print(Color.PURPLE+'\nPhoto Management Menu:\n'+Color.END)
        print('1)   Upload Profile Photo(s)  *Same photo for 1 or more ' +
              'user(s)*')
        print('2)   Mass Upload Photos *Different photos for multiple users*')
        print('3)   Download User(s) Profile Photo')
        print('4)   Delete User(s) Profile Photo')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # Upload same photo to 1 or more users
            users7_1()
        elif selection == '2':  # Upload different photos for multiple users
            users7_2()
        elif selection == '3':  # Download photos of 1 or more users
            users7_3()
        elif selection == '4':  # Delete photo of 1 or more users
            users7_4()
        elif selection == '0':
            users()
        else:
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            users7()


def users7_1():  # Upload same photo to 1 or more users
    who = input(Color.BOLD+Msgs.ent+Color.END)
    photo = input(Color.BOLD+'Enter the full path of the photo:  ' +
                  Color.END)
    if who == 'user' or who == 'group':
        user = input(Color.BOLD+'Enter a name:  '+Color.END)
        cmd = Gam.g+who+' update photo '+photo
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+'"'+user+'" update photo '+photo
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+'update photo '+photo
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        users7_1()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    users7()


def users7_2():  # Mass upload different photos for multiple users
    print(Color.YELLOW+'Photo names need to be formatted as such:'+Color.END)
    print(Color.RED+Color.BOLD+'#username#.jpg\n'+Color.END)
    srcdir = input(Color.BOLD+'Enter the source directory containing the ' +
                   'photos, with trailing "/":  '+Color.END)
    who = input(Color.BOLD+'Entity to apply to: [ou | all users]  '+Color.END)
    if who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+'"'+user+'" update photo sourcefolder '+srcdir +\
            ' filename ./#username#.jpg'
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+'update photo '+srcdir+' filename ./#username#.jpg'
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        users7_2()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    users7()


def users7_3():  # Download photos of 1 or more users
    who = input(Color.BOLD+Msgs.ent+Color.END)
    destdir = input(Color.BOLD+'Enter the destination directory to save ' +
                    'the photos, with trailing "/":  '+Color.END)
    if who == 'user' or who == 'group':
        user = input(Color.BOLD+'Enter a name:  '+Color.END)
        cmd = Gam.g+who+' get photo targetfolder '+destdir+' filename ' +\
            './#username#.jpg noshow'
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+'"'+user+'" get photo targetfolder '+destdir +\
            ' filename ./#username#.jpg noshow'
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+'get photo targetfolder '+destdir+' filename ' +\
            './#username#.jpg noshow'
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        users7_3()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    users7()


def users7_4():  # Delete photo of 1 or more users
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user' or who == 'group':
        user = input(Color.BOLD+'Enter a name:  '+Color.END)
        cmd = Gam.g+who+' del photo'
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+'"'+user+'" del photo'
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+'del photo'
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        users7_4()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    users7()


def calendar():  # Calendar Management Main Menu
    while True:
        print(Color.PURPLE+'\nCalendar Management Menu:\n'+Color.END)
        print('1)   Show Permissions For a Calendar')
        print('2)   Add or Remove Calendar Permissions')
        print('3)   Delete a Calendar Event')
        print('4)   List a User\'s Calendar(s)')
        print('5)   Delete a User\'s Calendar (Can\'t delete default ' +
              'calendar)')
        print('6)   Add a Calendar to a User')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # Calendar permissions menu item
            cal = input(Color.BOLD+'Please enter a Google Calendar email' +
                        ' address:'+Color.END)
            cmd = Gam.g+' calendar '+cal+' showacl'
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            calendar()
        elif selection == '2':  # Change permissions menu item
            calendar2()
        elif selection == '3':  # Delete event menu item
            calendar3()
        elif selection == '4':  # List calendars menu item
            calendar4()
        elif selection == '5':  # Delete calendar menu item
            calendar5()
        elif selection == '6':  # Add calendar to user menu item
            calendar6()
        elif selection == '0':  # Back to main menu
            main_menu()
        else:  # Invalid menu selection error. Returns to current menu
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            calendar()


def calendar2():  # Calendar menu option 2
    cal = input(Color.BOLD+'Please enter a Google Calendar email ' +
                'address:  '+Color.END)
    ar = input(Color.BOLD+'What would you like to do? [add | remove]  ' +
               Color.END)
    user = input(Color.BOLD+'User to add to/remove from the Calendar:  ' +
                 Color.END)
    if ar == 'add' or ar == 'Add' or ar == 'a':
        act = input(Color.BOLD+'What permission would you like to grant? ' +
                    '[read | edit | owner]'+Color.END)
        cmd = Gam.g+' calendar '+cal+' add '+act+' '+user
        os.system(cmd)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        calendar()
    elif ar == 'rem' or ar == 'remove' or ar == 'r' or ar == 'Remove' or \
            ar == 'Rem':
        cmd = Gam.g+' calendar '+cal+' delete user '+user
        os.system(cmd)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        calendar()
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        calendar()


def calendar3():  # Calendar menu option 3
    cal = input(Color.BOLD+'Please enter a Google Calendar email' +
                ' address:'+Color.END)
    ev = input(Color.BOLD+'Enter the event ID:'+Color.END)
    yn = input(Color.BOLD+'Are you sure? THIS CANNOT BE UNDONE!! ' +
               '[y/N]'+Color.END)
    if yn == '' or yn == 'N' or yn == 'n' or yn == 'no' or yn == 'No':
        calendar()
    elif yn == 'y' or yn == 'Y' or yn == 'yes' or yn == 'Yes':
        cmd = Gam.g+' calendar '+cal+' deleteevent '+ev+' doit'
        os.system(cmd)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        calendar()


def calendar4():  # Calendar menu option 4
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' show calendars'
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  '+Color.END)
        cmd = Gam.gr+user+' show calendars'
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+' "'+user+'" show calendars'
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+' show calendars'
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        calendar4()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    calendar()


def calendar5():  # Calendar menu option 5
    cal = input(Color.BOLD+'Please enter a Google Calendar email ' +
                'address:'+Color.END)
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' delete calendar '+cal
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  '+Color.END)
        cmd = Gam.gr+user+' delete calendar '+cal
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+' "'+user+'" delete calendar '+cal
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+' delete calendar '+cal
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        calendar5()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    calendar()


def calendar6():  # Calendar menu option 6
    cal = input(Color.BOLD+'Please enter a Google Calendar email ' +
                'address:'+Color.END)
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' add calendar '+cal+' selected true hidden false'
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  '+Color.END)
        cmd = Gam.gr+user+' add calendar '+cal+' selected true hidden false'
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+' "'+user+'" add calendar '+cal+' selected true ' +\
            'hidden false'
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+' add calendar '+cal+' selected true hidden false'
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        calendar6()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    calendar()


def drive():  # Drive Management Main Menu
    while True:
        print(Color.PURPLE+'\nDrive Management Menu:\n'+Color.END)
        print('1)   Export a List of a User(s) Drive Files')
        print('2)   Upload a Local File To a Google Drive')
        print('3)   Download File(s) from a Google Drive')
        print('4)   Delete a User\'s Drive File')
        print('5)   View a Shared Drive(s)')
        print('6)   Create a Shared Drive')
        print('7)   Delete a Shared Drive')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # Export file list menu item
            drive1()
        elif selection == '2':  # Upload file menu item
            drive2()
        elif selection == '3':  # Download Drive File(s)
            drive3()
        elif selection == '4':  # Delete User's drive file
            user = input(Color.BOLD+'Please enter a username:  '+Color.END)
            file = input(Color.BOLD+'Please enter the file ID to be ' +
                         'deleted:  '+Color.END)
            cmd = Gam.u+user+' delete drivefile '+file+' purge'
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            drive()
        elif selection == '5':  # View Shared Drives menu item
            drive5()
        elif selection == '6':  # Create team drive for user menu item
            user = input(Color.BOLD+'Please enter a username: '+Color.END)
            name = input(Color.BOLD+'What is the name of the Shared Drive?' +
                         Color.END)
            cmd = Gam.g+' user '+user+' add teamdrive "'+name+'"'
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            drive()
        elif selection == '7':  # Delete user's Shared Drive menu item
            user = input(Color.BOLD+'Please enter a username: '+Color.END)
            dr_id = input(Color.BOLD+'What is the Shared Drive ID? ' +
                          '(Not the name)'+Color.END)
            cmd = Gam.g+' user '+user+' delete teamdrive '+dr_id
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            drive()
        elif selection == '0':  # Return to main menu
            main_menu()
        else:  # Invalid selection. Returns to this menu
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            drive()


def drive1():  # Drive menu option 1
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user' or who == 'group':
        user = input(Color.BOLD+'Enter a name:  '+Color.END)
        user1 = user
        cmd = Gam.g+'redirect csv ~/'+user+'-filelist.csv ' +\
            'multiprocess '+who+' '+user+' print filelist allfields'
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        user1 = user.split('/')[-1]
        cmd = Gam.g+'redirect csv ~/'+user1+'-filelist.csv ' +\
            'multiprocess ou "'+user+'" print filelist allfields'
    elif who == 'all' or who == 'all users':
        user1 = 'AllUsers'
        cmd = Gam.g+'redirect csv ~/'+user1+'-filelist.csv ' +\
            'multiprocess all users print filelist allfields'
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        drive1()
    os.system(cmd)
    print(Color.YELLOW+'\nFile saved as '+user1+'-filelist.csv\n'+Color.END)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    drive()


def drive2():  # Drive menu option 2
    filename = input(Color.BOLD+'Please enter the full path to the' +
                     ' file you wish to upload: (Case Sensitive):  ' +
                     Color.END)
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' add drivefile localfile '+filename
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  ' +
                     Color.END)
        cmd = Gam.gr+user+' add drivefile localfile '+filename
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+user+' add drivefile localfile '+filename
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+' add drivefile localfile '+filename
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        drive()
    os.system(cmd)
    print('File uploaded successfully')
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    drive()


def drive3():  # Drive menu option 3
    who = input(Color.BOLD+Msgs.ent+Color.END)
    quant = input(Color.BOLD+'Single file or all files [single | all]:  ' +
                  Color.END)
    loc = input(Color.BOLD+'Enter the full path to the save location:  ' +
                Color.END)
    if quant == 'single':
        filename = input(Color.BOLD+'Please enter the filename to download: ' +
                         Color.END)
        filename1 = 'drivefilename "'+filename+'"'
    elif quant == 'all':
        filename = 'query "!me! in owners" '
        filename1 = filename.replace("!", r"'")
    else:
        filename1 = None  # To fix the possibility of an unbound variable
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        drive3()
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' get drivefile '+filename1+' targetfolder '+loc +\
            ' format microsoft'
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  '+Color.END)
        cmd = Gam.gr+user+' get drivefile '+filename1+' targetfolder '+loc +\
            ' format microsoft'
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive, Full ' +
                     'Path):  '+Color.END)
        cmd = Gam.ou+' "'+user+'" get drivefile '+filename1+' targetfolder ' +\
            loc+' format microsoft'
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+' get drivefile '+filename1+' targetfolder '+loc +\
            ' format microsoft'
    else:
        cmd = None  # To fix the possibility of an unbound variable
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        drive3()
    os.system(cmd)


def drive5():  # Drive menu option 5
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter username:  '+Color.END)
        cmd = Gam.u+user+' show teamdrives'
    elif who == 'group':
        user = input(Color.BOLD+'Please enter group name:  '+Color.END)
        cmd = Gam.gr+user+' print teamdrives todrive'
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive, Full ' +
                     'Path):  '+Color.END)
        cmd = Gam.ou+'"'+user+'" print teamdrives todrive'
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+' print teamdrives todrive'
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        drive5()
    os.system(cmd)
    time.sleep(2)
    print(Color.RED+'\nIf you chose any entity other than "user", a file ' +
          'was uploaded to your Google Drive with the Shared Drive ' +
          'information.'+Color.END)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    drive()


def groups():  # Groups Management Main Menu
    while True:
        print(Color.PURPLE+'\nGroup Management Menu:\n'+Color.END)
        print('1)   Create a Group')
        print('2)   Rename a Group')
        print('3)   Add or Remove Group Member')
        print('4)   Update User Role in a Group')
        print('5)   Get Group Information')
        print('6)   Delete a Group')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # Create group menu item
            name = input(Color.BOLD+'What is the name of the group to be ' +
                         'created?'+Color.END)
            cmd = Gam.g+' create group '+name +\
                '@madisonrams.net'  # CHANGE THIS DOMAIN TO MATCH YOURS.
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            groups()
        elif selection == '2':  # Rename group menu item
            name = input(Color.BOLD+'What is the email address of the ' +
                         'group to be renamed?'+Color.END)
            ren = input(Color.BOLD+'What is the new name(email address) of ' +
                        'the group?'+Color.END)
            cmd = Gam.g+' update group '+name+' email '+ren
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            groups()
        elif selection == '3':  # Add/Remove group member menu item
            groups3()
        elif selection == '4':  # Update user role menu item
            name = input(Color.BOLD+'What is the email address of the group?')
            user = input(Color.BOLD+'What user\'s role will be modified? ' +
                         Color.END)
            perm = input(Color.BOLD+'New role to assign (Must be in Lower ' +
                         'Case): [owner | member | manager]'+Color.END)
            cmd = Gam.g+' update group '+name+' update '+perm+' user '+user
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            groups()
        elif selection == '5':  # Group information menu item
            name = input(Color.BOLD+'What is the email address of the group?')
            cmd = Gam.g+' info group '+name
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            groups()
        elif selection == '6':  # Delete group menu item
            name = input(Color.BOLD+'What is the email address of the group?')
            cmd = Gam.g+' delete group '+name
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            groups()
        elif selection == '0':  # Back to main menu
            main_menu()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            groups()


def groups3():  # Groups menu option 3
    name = input(Color.BOLD+'What is the email address of the group?')
    ar = input(Color.BOLD+'Add or Remove user? [add | remove]'+Color.END)
    user = input(Color.BOLD+'What user?'+Color.END)
    if ar == 'add' or ar == 'a' or ar == 'Add' or ar == 'A':
        cmd = Gam.g+' update group '+name+' add member user '+user
        os.system(cmd)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        groups()
    elif ar == 'remove' or ar == 'r' or ar == 'R' or ar == 'Remove' or ar \
            == 'rem' or ar == 'Rem':
        cmd = Gam.g+' update group '+name+' remove user '+user
        os.system(cmd)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        groups()
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        groups()


def classroom():  # Classroom Management Main Menu
    while True:
        print(Color.PURPLE+'\nClassroom Management Main Menu:\n'+Color.END)
        print('1)   Manage Courses')
        print('2)   Manage Course Participants')
        print('3)   Manage Guardians')
        print('4)   Reports')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        # Manage courses menu item. Calls classroom1() function.
        if selection == '1':
            classroom1()
        elif selection == '2':  # Manage course participants menu item
            al = input(Color.BOLD+'What is the course ID or alias?'+Color.END)
            act = input(Color.BOLD+'Do you want to Add or Remove? ' +
                        '(Must be lower case) [add | remove]'+Color.END)
            who = input(Color.BOLD+'Is the person a student or a teacher? ' +
                        '(Must be lower case) [student | teacher]'+Color.END)
            user = input(Color.BOLD+'What is the person\'s username? ' +
                         Color.END)
            cmd = Gam.g+' course '+al+' '+act+' '+who+' '+user +\
                '@madisonrams.net'  # CHANGE THIS DOMAIN TO MATCH YOURS.
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            classroom()
        # Manage guardians menu item. Calls classroom3() function.
        elif selection == '3':
            classroom3()
        elif selection == '4':  # Reports menu item.
            classroom4()
        elif selection == '0':  # Back to main menu
            main_menu()
        else:  # Invalid selection error. Returns to current menu.
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            classroom()


def devices():  # Device Management Main Menu
    while True:
        print(Color.PURPLE+'\nChrome Device Management Main Menu:\n'+Color.END)
        print('1)   Get Device ID of a Chrome OS Device')
        print('2)   Update Device Info')
        print('3)   Export Device Info')
        print('4)   Disable, De-provision, or Re-Enable a Device')
        print('5)   Print Chrome Device Activity to CSV file')
        print('6)   Move Chrome Device')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # Get ID menu item
            cr_id = input(Color.BOLD+'Please enter the Chrome Device ' +
                          'Serial Number (Case sensitive):'+Color.END)
            cmd = Gam.g+'info cros cros_sn '+cr_id
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            devices()
        elif selection == '2':  # Update info menu item
            cr_id = input(Color.BOLD+'Please enter the Chrome Device ' +
                          'Serial Number:'+Color.END)
            time.sleep(1)
            act = input(Color.BOLD+'What do you want to update? [location ' +
                        '| asset id]'+Color.END)
            if act == 'location' or act == 'Location' or act == 'loc' or \
                    act == 'Loc' or act == 'L' or act == 'l':
                loc = input(Color.BOLD+'Enter new location:'+Color.END)
                cmd2 = Gam.g+'update cros cros_sn '+cr_id+' location "'+loc+'"'
                os.system(cmd2)
                time.sleep(2)
                input(Color.GREEN+'\n'+Msgs.cont+Color.END)
                os.system('rm -rf id.txt')
                devices()
            elif act == 'asset' or act == 'asset id' or act == 'assetid' or \
                    act == 'Asset' or act == 'Asset Id' or act == 'Asset ID' \
                    or act == 'Asset id' or act == 'A' or act == 'a':
                asset = input(Color.BOLD+'Enter new Asset ID:'+Color.END)
                cmd2 = Gam.g+'update cros cros_sn '+cr_id+' assetid "'+asset+'"'
                os.system(cmd2)
                time.sleep(2)
                input(Color.GREEN+'\n'+Msgs.cont+Color.END)
                os.system('rm -rf id.txt')
                devices()
            else:
                print(Color.RED+Msgs.err+'\n'+Color.END)
                time.sleep(1)
                input(Color.GREEN+'\n'+Msgs.cont+Color.END)
                devices()
        elif selection == '3':  # Export device info menu item.
            devices3()
        elif selection == '4':  # Disable/de-provision/re-enable menu item.
            devices4()
        elif selection == '5':  # Export device activity to csv file.
            devices5()
        elif selection == '6':  # Move Chrome Device
            devices6()
        elif selection == '0':  # Back to main menu
            main_menu()
        else:  # Invalid Selection. Returns to current menu
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            devices()


def classroom1():  # Manage Courses
    while True:
        print(Color.CYAN+'Course Management Menu:'+Color.END)
        print('1)   Create Course')
        print('2)   Update Course')
        print('3)   Get Course Info')
        print('4)   Delete Course')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # Create course menu item
            al = input(Color.BOLD+'What is the course alias? (All lower lase' +
                       ', no spaces)')
            name = input(Color.BOLD+'What is the course name?'+Color.END)
            sec = input(Color.BOLD+'What is the course section?(Numbers only)')
            head = input(Color.BOLD+'What is the heading?'+Color.END)
            room = input(Color.BOLD+'What room is the class in? (No spaces')
            teach = input(Color.BOLD+'What is the teacher\'s username? ' +
                          Color.END)
            cmd = Gam.g+' create course alias '+al+' name "'+name +\
                '" section '+sec+' heading "'+head+'" room '+room +\
                ' teacher '+teach+' status ACTIVE'
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            classroom()
        elif selection == '2':  # Update course menu item.
            classroom1_2()
        elif selection == '3':  # Course info menu item
            al = input(Color.BOLD+'What is the course ID or alias?'+Color.END)
            cmd = Gam.g+' info course '+al
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            classroom()
        elif selection == '4':  # Delete course menu item
            al = input(Color.BOLD+'What is the course ID or alias?'+Color.END)
            yn = input(Color.BOLD+'Are you sure? This action cannot be ' +
                       'undone! [y/N]'+Color.END)
            if yn == 'y' or yn == 'yes' or yn == 'Y' or yn == 'Yes':
                cmd = Gam.g+' delete course '+al
                os.system(cmd)
                time.sleep(2)
                input(Color.GREEN+'\n'+Msgs.cont+Color.END)
                classroom()
            elif yn == '' or yn == 'n' or yn == 'no' or yn == 'N' or \
                    yn == 'No':
                classroom()
            else:
                print(Color.RED+Msgs.err+'\n'+Color.END)
                time.sleep(1)
                classroom()
        elif selection == '0':  # Back to classroom main menu
            classroom()
        else:  # Invalid selection. Returns to current menu.
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            classroom1()


def classroom1_2():  # Classroom main menu option 1, submenu 2
    al = input(Color.BOLD+'What is the course ID or alias that will be ' +
               'updated?'+Color.END)
    while True:
        print(Color.YELLOW+'\nUpdate What?\n'+Color.END)
        print('1)   Name')
        print('2)   Section')
        print('3)   Heading')
        print('4)   Room')
        print('5)   Status')
        print('6)   Teacher')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # Update name menu item
            name = input(Color.BOLD+'Enter the new name:'+Color.END)
            cmd = Gam.g+' update course '+al+' name '+name
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            classroom1()
        elif selection == '2':  # Update section menu item
            name = input(Color.BOLD+'Enter new section:'+Color.END)
            cmd = Gam.g+' update course '+al+' section '+name
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            classroom1()
        elif selection == '3':  # Update heading menu item
            name = input(Color.BOLD+'Enter new heading:'+Color.END)
            cmd = Gam.g+' update course '+al+' heading "'+name+'"'
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            classroom1()
        elif selection == '4':  # Update room menu item
            name = input(Color.BOLD+'Enter new room:'+Color.END)
            cmd = Gam.g+' update course '+al+' room '+name
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            classroom1()
        elif selection == '5':  # Update status menu item
            name = input(Color.BOLD+'Enter new status (Must be uppercase): ' +
                         '[ACTIVE | ARCHIVED | DECLINED]'+Color.END)
            cmd = Gam.g+' update course '+al+' status '+name
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            classroom1()
        elif selection == '6':  # Update teacher menu item
            name = input(Color.BOLD+'Enter new teacher username:'+Color.END)
            cmd = Gam.g+' update course '+al+' owner '+name
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            classroom1()
        elif selection == '0':  # Back to previous menu
            classroom1()
        else:  # Invalid selection. Returns to current menu.
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            classroom1_2()


def classroom3():  # Classroom main menu option 3 submenu
    while True:
        print(Color.CYAN+'\nGuardian Management Menu:\n'+Color.END)
        print('1)   Invite Guardian')
        print('2)   Delete Guardian')
        print('3)   View a Student\'s Guardian(s)')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # Invite guardian menu item
            stu = input(Color.BOLD+'What is the student\'s username? ' +
                        Color.END)
            guard = input(Color.BOLD+'What is the guardian\'s email ' +
                          'address? '+Color.END)
            cmd = Gam.g+' create guardianinvite '+guard+' '+stu +\
                '@madisonrams.net'  # CHANGE THIS DOMAIN TO MATCH YOURS.
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            classroom3()
        elif selection == '2':  # Delete guardian menu item
            stu = input(Color.BOLD+'What is the student\'s username? ' +
                        Color.END)
            guard = input(Color.BOLD+'Guardian\'s email address? '+Color.END)
            cmd = Gam.g+' delete guardian '+guard+' '+stu +\
                '@madisonrams.net'  # CHANGE THIS DOMAIN TO MATCH YOURS.
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            classroom3()
        elif selection == '3':  # View a student's guardian(s) menu item
            stu = input(Color.BOLD+'What is the student\'s username? ' +
                        Color.END)
            cmd = Gam.g+' print guardians student '+stu +\
                '@madisonrams.net'  # CHANGE THIS DOMAIN TO MATCH YOURS.
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            classroom3()
        elif selection == '0':  # Back to Classroom main menu
            classroom()
        else:  # Invalid selection. Returns to current menu.
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            classroom3()


def classroom4():  # Classroom main menu option 4 submenu
    while True:
        print(Color.CYAN+'\nClassroom Reports Menu:\n'+Color.END)
        print('1)   View a Teacher\'s Courses')
        print('2)   View a Student\'s Courses')
        print('3)   View a Course\'s Participants')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # View teacher's courses menu item
            user = input(Color.BOLD+'What is the teacher\'s username? ' +
                         Color.END)
            cmd = Gam.g+' print courses teacher '+user +\
                '@madisonrams.net'  # CHANGE THIS DOMAIN TO MATCH YOURS.
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            classroom4()
        elif selection == '2':  # View student's courses menu item
            user = input(Color.BOLD+'What is the student\'s username? ' +
                         Color.END)
            cmd = Gam.g+' print courses student '+user +\
                '@madisonrams.net'  # CHANGE THIS DOMAIN TO MATCH YOURS.
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            classroom4()
        elif selection == '3':  # View course participants menu item
            al = input(Color.BOLD+'What is the course ID or alias?'+Color.END)
            file = input(Color.BOLD+'Output to a CSV file? [Y/n]')
            if file == '' or file == 'y' or file == 'Y' or file == 'yes' or \
                    file == 'Yes':
                cmd = Gam.g+'redirect csv ~/'+al+'-participants.csv ' +\
                    'multiprocess print course-participants course '+al
                os.system(cmd)
                time.sleep(2)
                input(Color.GREEN+'\n'+Msgs.cont+Color.END)
                classroom4()
            elif file == 'n' or file == 'N' or file == 'no' or file == 'No':
                cmd = Gam.g+' print course-participants course '+al
                os.system(cmd)
                time.sleep(2)
                input(Color.GREEN+'\n'+Msgs.cont+Color.END)
                classroom4()
            else:
                print(Color.RED+Msgs.err+'\n'+Color.END)
                time.sleep(2)
                input(Color.GREEN+'\n'+Msgs.cont+Color.END)
                classroom4()
        elif selection == '0':  # Back to classroom main menu
            classroom()
        else:  # Invalid selection. Returns to current menu
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            classroom4()


def devices3():  # Devices main menu option 3 submenu
    while True:
        print(Color.CYAN+'\nChrome Device Info Menu:\n'+Color.END)
        print('1)   View Single Device Info')
        print('2)   Export All Devices in an OU')
        print('3)   Export All Devices')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # View device info menu item
            cr_id = input(Color.BOLD+'Enter the Chrome Device Serial ' +
                          'Number (Case sensitive):'+Color.END)
            cmd2 = Gam.g+'info cros cros_sn '+cr_id+' full'
            os.system(cmd2)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            devices3()
        elif selection == '2':  # Export devices in ou menu item
            ou = input(Color.BOLD+'Please enter the full path of the OU you ' +
                       'wish to export (Case Sensitive):'+Color.END)
            ou2 = ou.split("/")[-1]
            cmd = Gam.g+'redirect csv ~/'+ou2+'-export.csv multiprocess ' +\
                'print cros full limit_to_ou "'+ou+'"'
            os.system(cmd)
            time.sleep(1)
            print('Exported as '+ou2+'-export.csv')
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            devices3()
        elif selection == '3':  # Export all devices menu item
            cmd = Gam.g+' print cros full > all-devices.csv'
            os.system(cmd)
            time.sleep(1)
            print('Device list exported as all-devices.csv')
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            devices3()
        elif selection == '0':  # Back to devices main menu
            devices()
        else:  # Invalid selection. Returns to current menu.
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            devices3()


def devices4():  # Devices main menu option 4 submenu
    while True:
        print(Color.CYAN+'\nDisable/De-Provision/Re-Enable Menu:\n'+Color.END)
        print('1)   Disable')
        print('2)   Re-Enable')
        print('3)   De-Provision')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # Disable menu item
            cr_id = input(Color.BOLD+'Please enter the Chrome Device ' +
                          'Serial Number (Case sensitive):'+Color.END)
            cmd2 = Gam.g+'update cros cros_sn '+cr_id+' action disable ' +\
                'acknowledge_device_touch_requirement'
            os.system(cmd2)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            devices4()
        elif selection == '2':  # Re-enable menu item
            cr_id = input(Color.BOLD+'Enter the Chrome Device Serial ' +
                          'Number (Case sensitive):'+Color.END)
            cmd2 = Gam.up+'cros cros_sn '+cr_id+' action reenable ' +\
                'acknowledge_device_touch_requirement'
            os.system(cmd2)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            devices4()
        elif selection == '3':  # Deprovision menu item.
            devices4_3()
        elif selection == '0':  # Back to devices main menu
            devices()
        else:  # Invalid selection. Returns to current menu.
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            devices4()


def devices4_3():  # Devices Main menu option 4. submenu 3
    while True:
        print(Color.DARKCYAN+'\nDe-Provision Menu:\n'+Color.END)
        print('1)   De-Provision to Replace With Same Model')
        print('2)   De-Provision to Replace With Different Model')
        print('3)   De-Provision to Retire')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # Replace with same model menu item
            cr_id = input(Color.BOLD+'Please enter the Chrome Device ' +
                          'Serial Number (Case sensitive):'+Color.END)
            cmd2 = Gam.up+'cros cros_sn '+cr_id+' action deprovision_same_model_' +\
                'replace acknowledge_device_touch_requirement'
            os.system(cmd2)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            devices4_3()
        elif selection == '2':  # Replace with diff model menu item
            cr_id = input(Color.BOLD+'Please enter the Chrome Device Serial ' +
                          'Number (Case sensitive):'+Color.END)
            cmd2 = Gam.up+'cros cros_sn '+cr_id+' action deprovision_different_model_' +\
                'replace acknowledge_device_touch_requirement'
            os.system(cmd2)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            devices4_3()
        elif selection == '3':  # Retire menu item
            cr_id = input(Color.BOLD+'Please enter the Chrome Device Serial ' +
                          'Number (Case sensitive):'+Color.END)
            cmd2 = Gam.up+'cros cros_sn '+cr_id+' action deprovision_retiring_device ' +\
                'acknowledge_device_touch_requirement'
            os.system(cmd2)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            devices4_3()
        elif selection == '0':  # Return to previous menu
            devices4()
        else:  # Invalid selection. Returns to current menu.
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            devices4_3()


def devices5():  # Print Chrome Device Activity to CSV file.
    action = input(
        Color.BOLD+'Entity to apply to: [single | ou | all]:  '+Color.END)
    if action == 'single':
        cr_id = input(Color.BOLD+'Please enter the Chrome Device Serial ' +
                      'Number (Case sensitive):  '+Color.END)
        cmd = Gam.g+'redirect csv ~/'+cr_id + \
            '-activity.csv multiprocess cros cros_sn '+cr_id+' print crosactivity all'
        os.system(cmd)
        print(Color.CYAN+'\nFile saved as ~/'+cr_id+'activity.csv'+Color.END)
        time.sleep(1)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        devices()
    elif action == 'ou':
        ou = input(
            Color.BOLD+'Please enter the entire OU path (Case sensitive):  '+Color.END)
        cmd = Gam.g+'redirect csv ~/'+ou.replace('/', '_').lstrip(
            '_')+'-cros_activity.csv multiprocess cros_ou_and_children '+ou+' print crosactivity all'
        os.system(cmd)
        print(Color.CYAN+'\nFile saved as ~/' +
              ou.replace('/', '_').lstrip('_')+'-cros_activity.csv'+Color.END)
        time.sleep(1)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        devices()
    elif action == 'all':
        cmd = Gam.g+'redirect csv ~/All_cros_activity.csv multiprocess print crosactivity all'
        os.system(cmd)
        print(Color.CYAN+'\nFile saved as ~/All_cros_activity.csv'+Color.END)
        time.sleep(1)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        devices()
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        devices()


def devices6():  # Move Chrome Device
    cr_id = input(Color.BOLD+'Please enter the Chrome Device Serial ' +
                  'Number (Case sensitive):  '+Color.END)
    ou = input(
        Color.BOLD+'Please enter the entire OU path (Case sensitive):  '+Color.END)
    cmd = Gam.g+'update cros cros_sn '+cr_id+' ou '+ou+' quickcrosmove true'
    os.system(cmd)
    time.sleep(1)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    devices()


def email():  # Email Management main menu
    while True:
        print(Color.PURPLE+'\nEmail Management Menu:\n'+Color.END)
        print('1)   User Signature and Vacation Message')
        print('2)   Labels and Filters')
        print('3)   IMAP and POP Settings')
        print('4)   Send As Settings')
        print('5)   Show User(s) Gmail Profile')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
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
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            email()


def email1():  # Email main menu option 1 submenu
    while True:
        print(Color.CYAN+'\nUser Signature Management Menu:\n'+Color.END)
        print('1)   Set User Signature From Text File')
        print('2)   Set User Signature From HTML File')
        print('3)   Set User Signature Manually')
        print('4)   View a User(s) Signature')
        print('5)   Set a User(s) Vacation Responder')
        print('6)   Turn off a User(s) Vacation Responder')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # Set sig from txt file
            email1_1()
        elif selection == '2':  # Set sig from html file
            email1_2()
        elif selection == '3':  # Set sig manually
            email1_3()
        elif selection == '4':  # View user's signature
            email1_4()
        elif selection == '5':  # Set vacation responder
            email1_5()
        elif selection == '6':  # Turn off responder
            email1_6()
        elif selection == '0':  # Back to main menu
            email()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            email1()


def email1_1():  # Email1 menu option 1
    txt = input(Color.BOLD+'Please enter the full path to the text ' +
                'file to read:'+Color.END)
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' signature file '+txt
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  '+Color.END)
        cmd = Gam.gr+user+'  signature file '+txt
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+' "'+user+'" signature file '+txt
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+'  signature file '+txt
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(1)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        email1_1()
    os.system(cmd)
    time.sleep(1)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email1()


def email1_2():  # Email1 menu option 2
    txt = input(Color.BOLD+'Please enter the full path to the html ' +
                'file to read:'+Color.END)
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' signature file '+txt+' html'
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  '+Color.END)
        cmd = Gam.gr+user+'  signature file '+txt+' html'
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+' "'+user+'" signature file '+txt+' html'
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+'  signature file '+txt+' html'
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        email1_2()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email1()


def email1_3():  # Email1 menu option 3
    print(Color.YELLOW+'Line breaks must be designated by <br>. EX: Acme ' +
          'Inc<br>123 Main Ave<br>http://www.acme.com'+Color.END)
    time.sleep(1)
    txt = input(Color.BOLD+'Please enter the full text of the signature:' +
                Color.END)
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' signature  "'+txt+'"'
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  '+Color.END)
        cmd = Gam.gr+user+'  signature  "'+txt+'"'
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+' "'+user+'" signature  "'+txt+'"'
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+'  signature  "'+txt+'"'
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        email1_3()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email1()


def email1_4():  # Email1 menu option 4
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' show signature format'
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  '+Color.END)
        cmd = Gam.gr+user+' show signature format'
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+' "'+user+'" show signature format'
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+' show signature format'
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        email1_4()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email1()


def email1_5():  # Email1 menu option 5
    sub = input(Color.BOLD+'Please enter a message subject: '+Color.END)
    print(Color.YELLOW+r'Line breaks must be designated using "\n".' +
          Color.END)
    mes = input(Color.BOLD+'Please enter the vacation message: '+Color.END)
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' vacation on subject "'+sub+'" message "'+mes+'"'
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  '+Color.END)
        cmd = Gam.gr+user+' vacation on subject "'+sub+'" message "'+mes+'"'
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+' "'+user+'" vacation on subject "'+sub +\
            '" message "'+mes+'"'
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+' vacation on subject "'+sub+'" message "'+mes+'"'
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        email1_5()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email1()


def email1_6():  # Email1 menu option 6
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' vacation off'
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  '+Color.END)
        cmd = Gam.gr+user+' vacation off'
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+' "'+user+'" vacation off'
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+' vacation off'
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        email1_6()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email1()


def email2():  # Email main menu option 2 menu
    while True:
        print(Color.CYAN+'\nLabels and Filters Menu:\n'+Color.END)
        print('1)   Create a Label')
        print('2)   View User(s) Labels')
        print('3)   Delete a Label')
        print('4)   Create a Filter')
        print('5)   View User(s) Filters')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # Create a label
            email2_1()
        elif selection == '2':  # View labels
            email2_2()
        elif selection == '3':  # Delete Label
            email2_3()
        elif selection == '4':  # Create Filter
            email2_4()
        elif selection == '5':  # View user's filters
            email2_5()
        elif selection == '0':  # Back to main menu
            email()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            email2()


def email2_1():  # Email2 menu option 1
    lab = input(Color.BOLD+'Please enter a name for the label: '+Color.END)
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' label "'+lab+'"'
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  '+Color.END)
        cmd = Gam.gr+user+' label "'+lab+'"'
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+' "'+user+'" label "'+lab+'"'
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+' label "'+lab+'"'
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        email2_1()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email2()


def email2_2():  # Email2 menu option 2
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' show labels'
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  '+Color.END)
        cmd = Gam.gr+user+' show labels'
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+' "'+user+'" show labels'
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+' show labels'
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        email2_2()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email2()


def email2_3():  # Email2 menu option 3
    lab = input(Color.BOLD+'Please enter the label name: '+Color.END)
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' delete label "'+lab+'"'
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  '+Color.END)
        cmd = Gam.gr+user+' delete label "'+lab+'"'
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+' "'+user+'" delete label "'+lab+'"'
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+' delete label "'+lab+'"'
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        email2_3()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email2()


def email2_4():  # create filter menu
    while True:
        print(Color.DARKCYAN+'\nFilter Criteria:\n'+Color.END)
        print('1)   "FROM" Address Only')
        print('2)   "FROM" Address and Subject')
        print('3)   Subject Only')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # Filter by from address only
            email2_4_1()
        elif selection == '2':  # Filter by address and subject
            email2_4_2()
        elif selection == '3':  # Filter by subject
            email2_4_3()
        elif selection == '0':  # Back to main menu
            email2()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            email2_4()


def email2_4_1():  # Email2_4 menu option 1
    eml = input(Color.BOLD+'Please enter an email address to filter ' +
                'on: '+Color.END)
    print('Separate action using a space')
    act = input(Color.BOLD+'What action to take? [markread | archive | star' +
                ' | trash | neverspam] '+Color.END)
    lab = input(Color.BOLD+'Please enter a label for the filtered messages: ' +
                Color.END)
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' filter from '+eml+' label "'+lab+'" '+act
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  '+Color.END)
        cmd = Gam.gr+user+' filter from '+eml+' label "'+lab+'" '+act
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+' "'+user+'" filter from '+eml+' label "'+lab+'" '+act
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+' filter from '+eml+' label "'+lab+'" '+act
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        email2_4_1()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email2_4()


def email2_4_2():  # Email2_4 menu option 2
    eml = input(Color.BOLD+'Please enter an email address to filter on: ' +
                Color.END)
    sub = input(Color.BOLD+'Please enter a subject to filter on: '+Color.END)
    print('Separate action using a space')
    act = input(Color.BOLD+'What action to take? [markread | archive | star' +
                ' | trash | neverspam] '+Color.END)
    lab = input(Color.BOLD+'Enter a label for the filtered messages: ' +
                Color.END)
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' filter from '+eml+' subject "'+sub+'" label "' +\
            lab+'" '+act
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  '+Color.END)
        cmd = Gam.gr+user+' filter from '+eml+' subject "'+sub+'" label "' +\
            lab+'" '+act
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+' "'+user+'" filter from '+eml+' subject "'+sub +\
            '" label "'+lab+'" '+act
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+' filter from '+eml+' subject "'+sub+'" label "'+lab +\
            '" '+act
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        email2_4_2()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email2_4()


def email2_4_3():  # Email2_4 menu option 3
    sub = input(Color.BOLD+'Enter a subject to filter on: '+Color.END)
    print(Color.YELLLOW+'\nSeparate action using a space\n'+Color.END)
    act = input(Color.BOLD+'What action to take? [markread | archive | star' +
                ' | trash | neverspam] '+Color.END)
    lab = input(Color.BOLD+'Enter a label for the filtered messages: ' +
                Color.END)
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' filter subject '+sub+' label "'+lab+'" '+act
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  '+Color.END)
        cmd = Gam.gr+user+' filter subject '+sub+' label "'+lab+'" '+act
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+' "'+user+'" filter subject '+sub+' label "'+lab+'" '+act
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+' filter subject '+sub+' label "'+lab+'" '+act
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        email2_4_3()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email2_4()


def email2_5():  # Email2 menu option 5
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' show filters'
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  '+Color.END)
        cmd = Gam.gr+user+' show filters'
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+' "'+user+'" show filters'
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+' show filters'
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        email2_5()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email2()


def email3():  # Pop and imap settings
    while True:
        print(Color.CYAN+'\nIMAP and POP Settings:\n'+Color.END)
        print('1)   Turn IMAP/POP On or Off for a User')
        print('2)   Show IMAP/POP status for a User')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # IMAP/POP on/off
            email3_1()
        elif selection == '2':  # IMAP/POP status
            email3_2()
        elif selection == '0':  # Back to main menu
            email()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            email3()


def email3_1():  # Email3 menu option 1
    prot = input(Color.BOLD+'What protocol? [pop | imap] '+Color.END)
    act = input(Color.BOLD+'Turn ON or OFF? [on | off] '+Color.END)
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' '+prot+' '+act
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  '+Color.END)
        cmd = Gam.gr+user+' '+prot+' '+act
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+' "'+user+'" '+prot+' '+act
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+' '+prot+' '+act
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        email3_1()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email3()


def email3_2():  # Email3 menu option 2
    prot = input(Color.BOLD+'What protocol? [pop | imap] '+Color.END)
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        cmd = Gam.u+user+' show '+prot
    elif who == 'group':
        user = input(Color.BOLD+'Please enter a group name:  '+Color.END)
        cmd = Gam.gr+user+' show '+prot
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        cmd = Gam.ou+' "'+user+'" show '+prot
    elif who == 'all' or who == 'all users':
        cmd = Gam.a+' show '+prot
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        email3_2()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email3()


def email4():  # Send As settings
    while True:
        print(Color.CYAN+'\nSend As Settings Menu:\n'+Color.END)
        print('1)   Add Send As Address')
        print('2)   Update Send As Address')
        print('3)   Delete Send As Address')
        print('4)   Show Send As Addresses for a User')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # Add send as address
            email4_1()
        elif selection == '2':  # Update send as
            email4_2()
        elif selection == '3':  # delete send as
            email4_3()
        elif selection == '4':  # View send as
            email4_4()
        elif selection == '0':  # Back to main menu
            email()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            email4()


def email4_1():  # Email4 menu option 1
    usr = input(Color.BOLD+'Please enter a username: '+Color.END)
    eml = input(Color.BOLD+'Please enter an email address to send as: ' +
                Color.END)
    nm = input(Color.BOLD+'Please Enter a name for the email address' +
               ' (ex. John Smith): '+Color.END)
    cmd = Gam.g+' user '+usr+' sendas '+eml+' '+nm+' replyto '+eml +\
        ' treatasalias true'
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email4()


def email4_2():  # Email4 menu option 2
    usr = input(Color.BOLD+'Please enter a username: '+Color.END)
    eml = input(Color.BOLD+'Please enter the send as email address: ' +
                Color.END)
    nm = input(Color.BOLD+'Please Enter an updated name for the ' +
               'email address (ex. John Smith): '+Color.END)
    cmd = Gam.g+' user '+usr+' update sendas '+eml+' name '+nm +\
        ' replyto '+eml+' treatasalias true'
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email4()


def email4_3():  # Email4 menu option 3
    usr = input(Color.BOLD+'Please enter a username: '+Color.END)
    eml = input(Color.BOLD+'Enter the send as email address: '+Color.END)
    cmd = Gam.g+' user '+usr+' delete sendas '+eml
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email4()


def email4_4():  # Email4 menu option 4
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user' or who == 'group':
        user = input(Color.BOLD+'Please enter a username:  '+Color.END)
        user1 = user
        cmd = Gam.g+'redirect csv ~/'+user1+'-sendas.csv multiprocess '+who +\
            user+' print sendas'
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        user1 = user.split('/')[-1]
        cmd = Gam.g+'redirect csv ~/'+user1+'-sendas.csv multiprocess ou "' +\
            user+'" print sendas'
    elif who == 'all' or who == 'all users':
        user1 = 'AllUsers'
        cmd = Gam.g+'redirect csv ~/'+user1+'-sendas.csv multiprocess all ' +\
            'users print sendas'
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        email4_4()
    os.system(cmd)
    print(Color.YELLOW+'\nFile saved as '+user1+'-sendas.csv\n'+Color.END)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email4()


def email5():  # Email5 menu option 4
    who = input(Color.BOLD+Msgs.ent+Color.END)
    if who == 'user' or who == 'group':
        user = input(Color.BOLD+'Please enter a name:  '+Color.END)
        cmd = Gam.g+'redirect csv ~/'+user+'-gmail-profile.csv multiprocess' +\
            who+' '+user+' print gmailprofile'
        user1 = user
    elif who == 'ou':
        user = input(Color.BOLD+'Please enter an OU (Case Sensitive' +
                     ', Full Path):  '+Color.END)
        user1 = user.split('/')[-1]
        cmd = Gam.g+'redirect csv ~/'+user1+'-gmail-profile.csv ' +\
            'multiprocess ou "'+user+'" print gmailprofile'
    elif who == 'all' or who == 'all users':
        user1 = 'AllUsers'
        cmd = Gam.g+'redirect csv ~/'+user1+'-gmail-profile.csv ' +\
            'multiprocess all users print gmailprofile'
    else:
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        email5()
    os.system(cmd)
    print(Color.YELLOW+'\nFile saved as '+user1+'-gmail-profile.csv\n' +
          Color.END)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    email()


def bulk():  # Bulk operations main menu
    while True:
        print(Color.PURPLE+'\nBulk Operations Menu:\n'+Color.END)
        print(Color.RED+'WARNING: Using these will affect multiple users. ' +
              'Some actions are unrecoverable. PROCEED WITH CAUTION!' +
              Color.END)
        print('1)   GAM Batch Mode Using CSV Files')
        print('2)   GAM Batch Mode Using Text Files')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # CSV Batch Mode
            csv()
        elif selection == '2':  # Batch file mode
            batch()
        elif selection == '0':  # Back to main menu
            main_menu()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            bulk()


def batch():  # GAM batch file commands
    print(Color.YELLOW+'\nThe file to be used in this batch mode must have ' +
          'a GAM command, one per line, with correct syntax\n'+Color.END)
    print(Color.RED+'If the syntax in your file is incorrect, the entire ' +
          'operation will fail.\n'+Color.END)
    file = input(Color.BOLD+'Please enter the full path of the file to be ' +
                 'used: '+Color.END)
    cmd = Gam.g+' batch '+file
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    bulk()


def csv():  # GAM CSV file batch mode
    print(Color.UNDERLINE+'\nCOMING SOON!\n'+Color.END)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    bulk()


def vault():  # Vault Management
    while True:
        print(Color.PURPLE+'\nVault Management Menu:\n'+Color.END)
        print('1)   Create Matter')
        print('2)   Update Matter')
        print('3)   Retrieve Matter Info')
        print('4)   Create Hold')
        print('5)   Update Hold')
        print('6)   Retrieve Hold Info')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # Create Matter
            vault1()
        elif selection == '2':  # Update Matter
            vault2()
        elif selection == '3':  # Retrieve Matter Info
            name = input(Color.BOLD+'Please enter the matter name:  ' +
                         Color.END)
            cmd = Gam.i+' vaultmatter "'+name+'"'
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            vault()
        elif selection == '4':  # Create Hold
            vault4()
        elif selection == '5':  # Update Hold
            vault5()
        elif selection == '6':  # Hold Info
            matname = input(Color.BOLD+'Please enter the matter name:  ' +
                            Color.END)
            name = input(Color.BOLD+'Please enter the hold name:  ' +
                         Color.END)
            cmd = Gam.i+'vaulthold "'+name+'" matter "'+matname+'"'
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            vault()
        elif selection == '0':  # Back to main menu
            main_menu()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            vault()


def vault1():  # Create Matter
    name = input(Color.BOLD+'Enter a name for the matter:  '+Color.END)
    desc = input(Color.BOLD+'Enter a short description for the matter:  ' +
                 Color.END)
    collab = input(Color.BOLD+'Add collaborators [y/N]?  '+Color.END)
    if collab == 'n' or collab == 'no':
        cmd = Gam.c+'vaultmatter name "'+name+'" description "'+desc+'"'
    elif collab == 'y' or collab == 'yes':
        collab1 = input(Color.BOLD+'Enter collaborator email address(es), ' +
                        'separated by commas without spaces:  ')
        cmd = Gam.c+'vaultmatter name "'+name+'" description "'+desc +\
            '" collaborators "'+collab1+'"'
    else:  # Invalid selection. returns to current menu.
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        vault()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    vault()


def vault2():  # Update Vault matter menu
    while True:
        print(Color.CYAN+'\nUpdate Matter Menu:\n'+Color.END)
        print('1)   Update Collaborators')
        print('2)   Update Description')
        print('3)   Close/Re-open Matter ')
        print('4)   Delete/Undelete Matter')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # Update Collaborators
            name = input(Color.BOLD+'Please enter the matter name:  ' +
                         Color.END)
            ar = input(Color.BOLD+'Add or remove collaborators [add | ' +
                       'remove]?  '+Color.END)
            coll = input(Color.BOLD+' Collaborator(s) to add/remove, comma ' +
                         'separated(no spaces):  '+Color.END)
            cmd = Gam.up+'vaultmatter "'+name+'" '+ar+'collaborators "'+coll +\
                '"'
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            vault2()
        elif selection == '2':  # Update description
            name = input(Color.BOLD+'Please enter the matter name:  ' +
                         Color.END)
            desc = input(Color.BOLD+'Please enter a short description:  ' +
                         Color.END)
            cmd = Gam.up+'vaultmatter "'+name+'" description "'+desc+'"'
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            vault2()
        elif selection == '3':  # Close/Reopen matter
            name = input(Color.BOLD+'Please enter the matter name:  ' +
                         Color.END)
            co = input(Color.BOLD+'Close or Re-open matter [close | reopen]?' +
                       '  '+Color.END)
            cmd = Gam.up+'vaultmatter "'+name+'" action '+co
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            vault2()
        elif selection == '4':  # Delete/Undelete matter
            print(Color.RED+'Matters must be closed before they can be ' +
                  'deleted!\n'+Color.END)
            name = input(Color.BOLD+'Please enter the matter name:  ' +
                         Color.END)
            co = input(Color.BOLD+'Delete or Undelete matter [delete | ' +
                       'undelete]?  '+Color.END)
            cmd = Gam.up+'vaultmatter "'+name+'" action '+co
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            vault2()
        elif selection == '0':  # Back to previous menu
            vault()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            vault2()


def vault4():  # Create Hold
    matname = input(Color.BOLD+'Enter the matter name:  '+Color.END)
    name = input(Color.BOLD+'Enter a name for the hold:  '+Color.END)
    corpus = input(Color.BOLD+'Hold what items? [mail | drive]  '+Color.END)
    wt = input(Color.BOLD+'Individual users or OU [user | ou]?  '+Color.END)
    start = input(Color.BOLD+'Start time [YYYY-MM-DD]?  '+Color.END)
    end = input(Color.BOLD+'End time [YYYY-MM-DD]?  '+Color.END)
    if wt == 'user':
        user = input(Color.BOLD+'Enter 1 or more email addresses separated ' +
                     'by commas (no spaces):  '+Color.END)
        cmd = Gam.c+'vaulthold matter "'+matname+'" name "'+name+'" corpus ' +\
            corpus+' accounts "'+user+'" starttime '+start+' endtime '+end
    elif wt == 'ou':
        ou = input(Color.BOLD+'Enter an ou (Case Sensitive): '+Color.END)
        cmd = Gam.c+'vaulthold matter "'+matname+'" name "'+name+'" corpus ' +\
            corpus+' orgunit "'+ou+'" starttime '+start+' endtime '+end
    else:  # Invalid selection. returns to current menu.
        print(Color.RED+Msgs.err+'\n'+Color.END)
        time.sleep(2)
        input(Color.GREEN+'\n'+Msgs.cont+Color.END)
        vault()
    os.system(cmd)
    time.sleep(2)
    input(Color.GREEN+'\n'+Msgs.cont+Color.END)
    vault()


def vault5():  # Update vault hold menu
    while True:
        print(Color.CYAN+'\nUpdate Hold Menu:\n'+Color.END)
        print('1)   Update Org Unit/User Account(s)')
        print('2)   Update Start/End time')
        print('3)   Delete Hold')
        print('\n0)   Back\n')
        selection = input(Color.BOLD+Msgs.choose+Color.END)
        if selection == '1':  # Update ou
            matname = input(Color.BOLD+'Please enter the matter name:  ' +
                            Color.END)
            name = input(Color.BOLD+'Please enter the hold name:  '+Color.END)
            wt = input(Color.BOLD+'Individual user(s) or OU [user | ou]?  ' +
                       Color.END)
            if wt == 'user':
                user = input(Color.BOLD+'Please enter 1 or more email ' +
                             'addresses separated by commas (no spaces):  ' +
                             Color.END)
                ar = input(Color.BOLD+'Add or remove [add | remove]?  ' +
                           Color.END)
                cmd = Gam.up+'vaulthold "'+name+'" matter "'+matname+'" '+ar +\
                    'accounts "'+user+'"'
            elif wt == 'ou':
                ou = input(Color.BOLD+'Please enter an ou (Case Sensitive): ' +
                           Color.END)
                cmd = Gam.up+'vaulthold "'+name+'" matter "'+matname+'"  ' +\
                    'orgunit "'+ou+'"'
            else:  # Invalid selection. returns to current menu.
                print(Color.RED+Msgs.err+'\n'+Color.END)
                time.sleep(2)
                input(Color.GREEN+'\n'+Msgs.cont+Color.END)
                vault5()
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            vault5()
        elif selection == '2':  # Update start/end
            matname = input(Color.BOLD+'Please enter the matter name:  ' +
                            Color.END)
            name = input(Color.BOLD+'Please enter the hold name:  '+Color.END)
            start = input(Color.BOLD+'What is the new start time ' +
                          '[YYYY-MM-DD]?  '+Color.END)
            end = input(Color.BOLD+'What is the new end time [YYYY-MM-DD]?  ' +
                        Color.END)
            cmd = Gam.up+'vaulthold "'+name+'" matter "'+matname +\
                '" starttime '+start+' endtime '+end
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            vault5()
        elif selection == '3':  # Delete Hold
            matname = input(Color.BOLD+'Please enter the matter name:  ' +
                            Color.END)
            name = input(Color.BOLD+'Please enter the hold name:  '+Color.END)
            cmd = Gam.de+'vaulthold "'+name+'" matter "'+matname+'"'
            os.system(cmd)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            vault5()
        elif selection == '0':  # Back to previous menu
            vault()
        else:  # Invalid selection. returns to current menu.
            print(Color.RED+Msgs.err+'\n'+Color.END)
            time.sleep(2)
            input(Color.GREEN+'\n'+Msgs.cont+Color.END)
            vault5()


cred()
main_menu()
