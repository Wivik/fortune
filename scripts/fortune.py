#!/usr/bin/env python3

from datetime import datetime, time
from feedgen.feed import FeedGenerator
import glob
import jinja2
import os
import pytz

## where are we
script_path = os.path.dirname(__file__)
www_path = script_path.replace('scripts', 'www')
histo_path = os.path.join(script_path, 'histo')

## some vars
website_url = 'https://fortune.zedas.fr'
locale_tz = 'Europe/Paris'

def load_fortune(file):
    """ load the fortune file for a variable """
    with open(file, 'r') as fortune:
        output = fortune.read()
    fortune.close()
    return output

def write_rss(whosays, fortune):
    """ write the rss feed according to the histo folder """
    if whosays == 'cow':
        saidby = 'A Cow'
    else:
        saidby = 'Tux'

    feed = FeedGenerator()
    feed.id(website_url)
    feed.title('The daily fortune said by '+ saidby +'.')
    feed.description('The daily fortune said by a '+ saidby +'.')
    feed.author({'name': saidby})
    feed.link(href=website_url, rel='alternate')
    feed.language('en')

    date = datetime.now()
    timestamp = datetime.timestamp(date)
    # print(date)
    # print(int(timestamp))

    fe = feed.add_entry()
    fe.title('Today\'s daily fortune')
    fe.id(website_url + '/'+ whosays +'say-'+ str(int(timestamp)) +'.html')
    fe.content('<pre>' + fortune + '</pre>')
    fe.link(href=website_url + '/'+ whosays +'say.html')

    feed.atom_file(os.path.join(www_path, whosays +'feed_atom.xml'))
    feed.rss_file(os.path.join(www_path, whosays +'feed_rss.xml'))

    # print(feed.atom_str(pretty=True))
    # print(feed.rss_str(pretty=True))


def write_template(fortune, file):
    """ write the fortune page """
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(script_path, 'template')))
    template = env.get_template('index.html.j2')
    render = template.render(fortune=fortune, website_url=website_url, file=file)
    # print(render)
    with open(os.path.join(www_path, file), 'w') as f:
        f.write(render)
        f.close()

def main():
    """ main fuction ! """
    ## get the two fortune files
    cowsay = load_fortune(os.path.join(script_path, 'cowsay.txt'))
    tuxsay = load_fortune(os.path.join(script_path, 'tuxsay.txt'))
    # print(cowsay)
    # print(tuxsay)
    ## write template
    write_template(cowsay, 'index.html')
    write_template(cowsay, 'cowsay.html')
    write_template(tuxsay, 'tuxsay.html')
    ## write RSS
    write_rss(whosays='cow', fortune=cowsay)
    write_rss(whosays='tux', fortune=tuxsay)


if __name__ == '__main__':
    main()

