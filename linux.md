# Package install command list for a bash script

## Update System Repository
`sudo apt-get update`


## Cubic for custom ISO creation: 


* `sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 081525E2B4F1283B`

* `sudo apt-add-repository ppa:cubic-wizard/release`

* `sudo apt update`

* `sudo apt install cubic`

## Vscode

  `wget -O vscode.deb  https://go.microsoft.com/fwlink/?LinkID=760868 && sudo dpkg -i vscode.deb`


## Anaconda for Python 3.6

  `wget -O anaconda.deb  https://repo.anaconda.com/archive/Anaconda3-2019.03-MacOSX-x86_64.pkg && sudo dpkg -i anaconda.deb`

## Spotify 

#### 1. Add the Spotify repository signing keys to be able to verify downloaded packages
`sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 931FF8E79F0876134EDDBDCCA87FF9DF48BF1C90`

#### 2. Add the Spotify repository
`echo deb http://repository.spotify.com stable non-free | sudo tee /etc/apt/sources.list.d/spotify.list`

#### 3. Update list of available packages
`sudo apt-get update`

#### 4. Install Spotify
`sudo apt-get install spotify-client`

## Node JS

* `wget https://deb.nodesource.com/setup_10.x -o nodesource_setup.sh`
* `sudo bash nodesource_setup.sh`
* `sudo apt install nodejs`
* `nodejs -v`

## Simple Screen Recoder
`sudo apt-get install simplescreenrecorder`

