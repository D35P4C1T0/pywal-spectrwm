# Pywal-spectrwm

So this is a simple script that basically updates your background color variable inside [spectrwm](https://github.com/conformal/spectrwm) config file, fetching the colours from your pywal colorscheme inside the file `~/.cache/wal/colors.json`.This is my first python script ever so I hope there's some room for improvement. Spectrwm unthemed config file is supposed to be located inside the proper folder (`~/.config/spectrwm/spectrwm.conf`), if this is not the case for you, well, there's no need to clutter your home directory with dotfiles all over the place like spectrwm suggests you to do if you don't dive deeper into the manual. The config file will be overwritten but a 1:1 copy of the unmodified file will be stored in the same folder, with `.backup` as the extension.

## Dependencies

- [pywal](https://github.com/dylanaraps/pywal)
- [spectrwm](https://github.com/conformal/spectrwm)

## Why does this thing exists

I was playing around with this tiny window manager and I felt like it needed some style, like all the other wm I've used in the past (dwm, i3, bspwm+polybar). Since I couldn't find any practical solution for this specific need I felt I could contribute.

## What's missing

Basically anything that could make this script noob proof. It has no actual arguments and it has to be run each time you update your colorscheme, either manually or through some automation/further scripting, but that's up to you.
