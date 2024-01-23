#!/usr/bin/bash
echo "Uninstalling"
sudo rm -rf /usr/lib/python3/dist-packages/calculadorita
sudo rm /usr/bin/com.github.lozanotux.calculadorita 
echo "Rebuilding"
rm -rf build/
meson build --prefix=/usr && cd build
ninja
echo "Installing"
sudo ninja install