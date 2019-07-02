If you are like me and like to use one main virtual environment for all your experimental modules and code you may find this useful. I made it to be compatible with pipenv since that is the reccomended way to set up virtualenvs according to the python community. I did find that going back and forth between the pipfile to install a module a little tedious, so I made this.
___

## Notes
* For Nix based OS's
* The lock skip option takes a really long time, especially for testing modules not for production. That is why it is skipped
___

## How to use
* Set the "pipenv_path" to where the pipfile is located on your system.
* Set "actual_path" to where the actual pipenvs are created. For Nix systems they will be at /home/user/.local/share/virtualenvs/ and have dynamic names. This is for getting a list of your envs if you need to.
* Run script.

![](https://github.com/tlscripts/pipenvtool/blob/master/image.png)


