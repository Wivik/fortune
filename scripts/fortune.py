#!/usr/bin/env python3

from datetime import datetime
from feedgen.feed import FeedGenerator
import glob
import jinja2
import os

## where are we
script_path = os.path.dirname(__file__)
www_path = script_path.replace('scripts', 'www')
histo_path = os.path.join(script_path, 'histo')

## some vars
website_url = 'https://fortune.zedas.fr'

def load_fortune(file):
    """ load the fortune file for a variable """
    with open(file, 'r') as fortune:
        output = fortune.read()
    fortune.close()
    return output

def write_rss(whosays):
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

    for say_file in sorted(glob.glob(histo_path + '/'+ whosays +'say_*.txt'), key=os.path.getmtime, reverse=True):
        # print(cowsay_file)
        with open(say_file, 'r') as file:
            content = file.read()
        date = say_file.split('_')[1].replace('.txt', '')
        date = datetime.fromtimestamp(int(date)).isoformat()
        fe = feed.add_entry()
        fe.title('Today\'s daily fortune')
        fe.id(website_url + '/'+ whosays +'say.html')
        fe.content('<pre>' + content + '</pre>')
        fe.link(href=website_url + '/'+ whosays +'say.html')
        # print(cowsay_date)
        file.close()

    feed.atom_file(os.path.join(www_path, whosays +'feed_atom.xml'))
    feed.rss_file(os.path.join(www_path, whosays +'feed_rss.xml'))


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
    print(cowsay)
    print(tuxsay)
    ## write template
    write_template(cowsay, 'index.html')
    write_template(cowsay, 'cowsay.html')
    write_template(tuxsay, 'tuxsay.html')
    ## write RSS
    write_rss(whosays='cow')
    write_rss(whosays='tux')


if __name__ == '__main__':
    main()

