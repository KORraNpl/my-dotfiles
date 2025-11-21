# my-dotfiles

## Credits / sources
* <https://github.com/Siilwyn/my-dotfiles>
* <https://news.ycombinator.com/item?id=11071754>
* <https://www.atlassian.com/git/tutorials/dotfiles>

## Setup (zsh)
```sh
git init --bare $HOME/.my-dotfiles
echo "alias mydotfiles='git --git-dir=$HOME/.my-dotfiles/ --work-tree=$HOME'" >> $HOME/.zshrc
omz reload
mydotfiles remote add origin git@github.com:KORraNpl/my-dotfiles.git
```

## Replication
```sh
git clone --separate-git-dir=$HOME/.my-dotfiles https://github.com/KORraNpl/my-dotfiles.git my-dotfiles-tmp
rsync --recursive --verbose --exclude '.git' my-dotfiles-tmp/ $HOME/
rm --recursive my-dotfiles-tmp
```

## Configuration
```sh
mydotfiles config status.showUntrackedFiles no
mydotfiles remote set-url origin git@github.com:KORraNpl/my-dotfiles.git
```

## Usage
```sh
mydotfiles status
mydotfiles add .gitconfig
mydotfiles commit -m 'Add gitconfig'
mydotfiles push
```
