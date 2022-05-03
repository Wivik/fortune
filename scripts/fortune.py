#!/usr/bin/env python3

import os
import jinja2

## where are we
script_path = os.path.dirname(__file__)

def load_fortune(file):
    """ load the fortune file for a variable """
    with open(file, 'r') as fortune:
        output = fortune.read()
    fortune.close()
    return output

def write_template(fortune, file):
    """ write the fortune page """
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(script_path, 'template')))
    template = env.get_template('index.html.j2')
    render = template.render(fortune=fortune)
    # print(render)
    with open(os.path.join(script_path.replace('scripts', 'www'), file), 'w') as f:
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
    ## replace www content


if __name__ == '__main__':
    main()

