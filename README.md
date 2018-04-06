# GAM-Frontend
### Front End Python program for GAM by Jay Lee

**_You must first install and configure [GAM by Jay Lee](https://github.com/jay0lee/GAM "GAM by Jay Lee")_**. I have included the installer for Gam and python in the [Release](https://github.com/strohmy86/GAM/releases "Releases").

This Python program is written in Python 3 and assumes that you are running Linux with the default install location (`~/bin/gam/`) for GAM. If your environment is different, you will need to change the code to meet your needs.

This program does not yet contain all of GAM's capabilities, but I am regularly adding functionality. Check back often for updates and added features.

I am always looking for suggestions. Please feel free to add your suggestions for features that are not yet included in this program.


## Install Instructions

If you wish to convert this python program to a single executable, follow the following instructions:

1. Make your domain-specific changes to `gam.py` as mentioned on line 28.
2. Make sure that you have the `pyinstaller` module installed:
    * `sudo pip3 install pyinstaller`
      * If already installed you should make sure it's up to date: `sudo pip3 install --upgrade pyinstaller`
    
3. CD to the `GAM-Frontend` directory
4. Run the following command: `pyinstaller gam.py --onefile`
    * This will create various directories and a `gam.spec` file. The executable will be in the `dist` directory. You can delete all other files and directories and the gam executable will still function fine.
