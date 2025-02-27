# anti-mindblock for Linux

A tool for osu! standart mode to prevent mindblocking for Linux.

Original idea was taken from [this](https://github.com/ShikkesoraSIM/anti-mindblock) project.

Actually, I just rewrote it and ported it to Linux :)

## Installation
Download the latest release from [here](https://github.com/Kartavkun/anti-mindblock/releases/latest).

I don't want to write README for projest that's not ready yet...

## Building

Build with nuitka (install with `pip install nuitka`):
```bash
nuitka --standalone --onefile --output-dir=build main.py
```
bin file will be in `build` directory.
Added it because I don't want to forget build command.

TODO:
- Restoring by a keybind
- Work with other init systems except systemd
- Invert skin's numbers
- Invert of mouse for mouse players
