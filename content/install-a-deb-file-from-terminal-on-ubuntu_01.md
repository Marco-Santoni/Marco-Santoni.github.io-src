Title: Install a .deb file from terminal on Ubuntu
Date: 2016-05-23 08:18
Author: mrsantoni
Category: Uncategorized
Slug: install-a-deb-file-from-terminal-on-ubuntu
Status: published

I use Ubuntu 16.04. Sometimes, when I double-click a *.deb* file, the
installation program does not work. What often solves the problem is
installing it from terminal.

\[code\]

sudo dpkg -i my\_deb\_file.deb  
sudo apt-get -f install

\[/code\]
