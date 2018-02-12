# whoami

Make whoami fun with the classic Kuthiravattom Pappu dialog

## Requirements

* python3
* playsound :
  ```
  pip3 install playsound --user
  ```

## Install

* Download the `whoami` file
* Make a symlink to this file :
  ```bash
  ln -s /home/$USER/Downloads/whoami ~/.local/bin/whoami
  ```
* Open a new terminal and run `whoami`

## Bonus

A custom `whoareyou` command is included with sound of Mohanlal's dialog `Njan ninte thanthayaada thantha`.

Make the file with : 

```
python3 make-whoareyou.py
```

Installation and running is the same as [whoami](#install)
