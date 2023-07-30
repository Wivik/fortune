#!/usr/bin/env python3

from datetime import datetime, time
from feedgen.feed import FeedGenerator
import glob
import jinja2
import os
import subprocess
import argparse


## argument
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-w', '--website-url', dest='website_url', help='The website base url : https://fortune.example.com', required=True)
args = arg_parser.parse_args()

global website_url
website_url = args.website_url
global script_path
script_path = os.path.dirname(__file__)

global fortune_cmd
fortune_cmd = '/usr/games/fortune'
global cowsay_cmd
cowsay_cmd = '/usr/games/cowsay'


## some vars
# locale_tz = 'Europe/Paris'

special_dates = {
    "0405": "vader",
    "2305": "turtle",
    "0106": "supermilker",
    "0607": "kiss",
    "0808": "meow",
    "1008": "moofasa",
    "2009": "head-in",
    "3110": "skeleton",
}

def fortune():
    """ Run the fortune and cowsay commands according to the day """
    fortune_output = subprocess.check_output(fortune_cmd, shell=True)

    return fortune_output

def is_it_a_special_day():
    """
    function that returns if the day is a special day according to a known list, if not it'll be false
    the event is an option ofr the cowsay command to change the display
    """
    today = datetime.now()
    today_str = today.strftime('%m%d')
    # today_str='1008'
    return special_dates.get(today_str, False)

def cowsay(fortune, special_day=False):
    """
    render the fortune using the cowsay command
    output is a list of two dict because we also have tuxsay
    """
    output = []
    if special_day:
        cowsay_output = subprocess.check_output([cowsay_cmd, '-f', special_day, fortune])
        tuxsay_output = subprocess.check_output([cowsay_cmd, '-f', special_day, fortune])
    else:
        cowsay_output = subprocess.check_output([cowsay_cmd, fortune])
        tuxsay_output = subprocess.check_output([cowsay_cmd, '-f', 'tux', fortune])

    output.append(
        {
            'say': 'cowsay',
            'content': cowsay_output
        }
    )
    output.append(
        {
            'say': 'tuxsay',
            'content': tuxsay_output
        }
    )

    return output


def write_rss(whosays, fortune):
    """ write the rss feed according to the histo folder """
    if whosays == 'cowsay':
        saidby = 'A Cow'
    else:
        saidby = 'Tux'

    feed = FeedGenerator()
    feed.id(website_url)
    feed.title(f'The daily fortune said by {whosays}.')
    feed.description(f'The daily fortune said by {whosays}.')
    feed.author({'name': saidby})
    feed.link(href=website_url, rel='alternate')
    feed.language('en')

    date = datetime.now()
    timestamp = datetime.timestamp(date)
    # print(date)
    # print(int(timestamp))

    fe = feed.add_entry()
    fe.title('Today\'s daily fortune')
    fe.id(f'{website_url}/{whosays}say-{str(int(timestamp))}.html')
    fe.content(f'<pre>{fortune}</pre>')
    fe.link(href=f'{website_url}/{whosays}-say.html')

    feed.atom_file(f'{whosays}_feed_atom.xml')
    feed.rss_file(f'{whosays}_feed_rss.xml')

    # print(feed.atom_str(pretty=True))
    # print(feed.rss_str(pretty=True))


def write_template(fortune, file):
    """ write the fortune page """
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(script_path, 'template')))
    template = env.get_template('index.html.j2')
    render = template.render(fortune=fortune, website_url=website_url, file=file)
    # print(render)
    with open(os.path.join(file), 'w') as f:
        f.write(render)
        f.close()

def main():
    """ main fuction ! """
    ## call fortune command
    today_fortune = fortune()
    special_day = is_it_a_special_day()
    ## format cowsay
    says_list = cowsay(today_fortune, special_day)

    ## write html files
    for say in says_list:
        if say['say'] == 'cowsay':
            who_said = say['say']
            say_content = say['content'].decode()
            write_template(say_content, 'index.html')
            write_template(say_content, f'{who_said}.html')
            write_rss(whosays=who_said, fortune=say_content)
        else:
            write_template(say_content, f'{who_said}.html')
            write_rss(whosays=who_said, fortune=say_content)


if __name__ == '__main__':
    main()

