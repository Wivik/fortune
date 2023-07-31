# Fortune

This is the sources of a [useless website](https://fortune.zedas.fr) that will display a daily result of the `fortune` command display with `cowsay` and `cowsay -f tux`.

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Wivik_fortune&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Wivik_fortune)

## Usage

**Breaking change with the original version, the tool is now fully containerized !**

Pull the container [latest version](https://github.com/Wivik/fortune/pkgs/container/fortune) :

```bash
docker pull ghcr.io/wivik/fortune:latest
```

In a folder of your choice, create a directory name `output` and `chmod` it to 777. That's ugly, but it's just for the container output, you may destroy it after.

Execute the container with a bind mount.

The important part here is the `-w` argument : you need to provide to the tool your website base URL, which is the URL from which the website will be displayed.


```bash
docker run --rm -v ${PWD}/output:/fortune/output ghcr.io/wivik/fortune:latest -w <your website base url>
```

Example in my case, the URL is https://fortune.zedas.fr, I use : `-w https://fortune.zedas.fr`. This URL will be inserted in the template to generate absolute paths.

Then, upload the `output/` content to your website root directory. The content folder will produce the following files :

```bash
./output/index.html
./output/cowsay_feed_atom.xml
./output/tuxsay_feed_atom.xml
./output/cowsay_feed_rss.xml
./output/cowsay.html
./output/tuxsay_feed_rss.xml
./output/tuxsay.html
```

For a daily output, just schedule the script every day at midnight.

## GitHub Actions example

```yaml
name: Publish daily fortune

on:
  workflow_dispatch:
  schedule:
    - cron: '00 00 * * *'

jobs:
  fortune:
    runs-on: ubuntu-latest
    steps:

      - name: Checkout code
        uses: actions/checkout@v3

      - name: Pull image
        run: |
          docker pull ghcr.io/wivik/fortune:latest

      - name: Generate fortune
        run: |
          mkdir output
          chmod 777 output
          docker run --rm -v ${{ github.workspace }}/output:/fortune/output ghcr.io/wivik/fortune:latest -w https://fortune.zedas.fr

      - name: Publish content
        run: |
          cd output
          # use here your publication method, rsync or whatever else, it's up to you.

```

## Under the hood

The first version was a mix of Python and Bash. This one is full Python with a script located in [container/scripts/fortune.py](container/scripts/fortune.py).

This script has only one mandatory param, the website base url.

```bash
usage: fortune.py [-h] -w WEBSITE_URL

options:
  -h, --help            show this help message and exit
  -w WEBSITE_URL, --website-url WEBSITE_URL
                        The website base url : https://fortune.example.com

```


