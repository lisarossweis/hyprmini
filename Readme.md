## My Personal Hyprland setup
My personal Hyprland setup inspired [MathisP75/summer-day-and-night](https://github.com/MathisP75/summer-day-and-night)
with some adjustment for my potato laptop
- Arch linux
- yay
- Hyprland 
- waybar
- wofi
- waypaper
- swaybg
- cliphist
- swaylock
- sddm
- kitty
- neovim



### Setup
to make it properly render icon and japanese number on waybar we need to install some packages
```sh
yay -S ttf-font-awesome ttf-jetbrains-mono-nerd noto-fonts-cjk noto-fonts \
noto-fonts-emoji ttf-freefont ttf-ms-fonts ttf-linux-libertine \
ttf-dejavu ttf-inconsolata ttf-ubuntu-font-family
```

then install Hyperland with
```sh
yay -S Hyperland-git waybar-git wofi waypaper swaybg cliphist swaylock kitty \
neovim sddm-git polkit-kde-agent swappy grim slurp file-roller ristretto \
thunar thunar-archive-plugin gvfs pamixer pavucontroll brightnessctl nwg-look \
wirepipe wirepipe-pulse wireplumber sddm-sugar-candy
```

copy the config file to the `~/.config`
```sh
cp -R hyper ~/.config/
cp -R waybar ~/.config/
cp -R wofi ~/.config/
```


### Credit
- [MathisP75/summer-day-and-night](https://github.com/MathisP75/summer-day-and-night) -> waybar & wofi theme
- [SolDoesTech/HyprV4](https://github.com/SolDoesTech/HyprV4) -> sddm theme
