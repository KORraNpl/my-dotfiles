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
echo "alias mydotfiles='git --git-dir=$HOME/.my-dotfiles/ --work-tree=$HOME'" >> $HOME/.zshrc
omz reload
git clone --bare git@github.com:KORraNpl/my-dotfiles.git $HOME/.my-dotfiles
mydotfiles checkout
mydotfiles config status.showUntrackedFiles no
```
If the `mydotfiles checkout` fails, most probably this means that some of the files already exist. Rename them to merge after checkout or run `mydotfiles checkout --force`, if files are safe to overwrite.
