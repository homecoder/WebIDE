Pythonista Web IDE
==================

I'd like to start by thanking Noah Rosamilia (https://github.com/Ivoah) for creating this, 
I would have never thought of it myself.

However, in the interest of my own personal needs I am using Web IDE as a base, and working to
enhance it as best I can.

Full Disclosure: I've really only started doing python in the past 5-6 months, so if you see anything that
needs to be fixed, I've done wrong, etc, please either let me know, or submit a pull request.

Summary of Changes
------------------

*Note: All items listed below should be considered incomplete unless otherwise specified.* 

The source is being kept on public github as a method of allowing me easily maintain commit history & updates.


**New Features**

* Run mode - Click a button in the IDE and the app you are working on will run in Pythonista 
(or the host running Web IDE).
* Configuration - Ability to set/save configuration preferences/options 
* Configuration: Ability to toggle use of Bottle Debug mode (Previously: Always On)
* Configuration: Ability to toggle use of Bonjour (Previously: Always On) - For public networks such as Starbucks, etc.

**WebIDE.py Updates**

* Updated CodeMirror
* Imported remaining CodeMirror Modes and Themes
* Implement of six library for code compatibility
* Added 'json', 'tpl', 'html', 'htm', and 'md' to "Editable" filetypes 

**Planned Updates**

* Code: Fully document all methods & attributes
* Enable further coverage for other development languages (IDE/Editing Only)
* Dash Docsets (Browser) - http://lucasg.github.io/2017/02/05/Downloading-Dash-docsets/ (Long shot, just browsing)
* Deeper integration with Pythonista (Open files in the editor, etc)

     
    
      
