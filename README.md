# Fortune

This is the sources of a [useless website](https://fortune.zedas.fr) that will display a daily result of the `fortune` command display with `cowsay` and `cowsay -f tux`.

## Prerequisites

`fortune` and `cowsay` must be installed on the system.

On Red Hat/CentOS/Fedora/Rocky Linux :

```bash
dnf install cowsay fortune-mod
```

On Debian/Ubuntu

```bash
apt get install cowsay fortune
```

## Usage

Clone this repository.

Go to the `scripts` folder.

Install the Python requirements.

```bash
pip install -r requirements.txt
```

Open `fortune.py` and adapt the first variable content according to your website URL.

```python
website_url = 'https://fortune.zedas.fr'
```

Launch `fortune.sh`.

Expose with the webserver of your choice the `www` folder.

You may crontab it if you want the daily magic to happens.

```
00 00 * * * /path/to/scripts/fortune.sh
```


