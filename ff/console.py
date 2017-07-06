import ff,sys,copy,argparse

def _get_story(f):
    if f.startswith('https://') or f.startswith('http://'):
        s = Story(url=f)
    elif f.startswith('www'):
        s = Story(url='https://%s' % f)
    else:
        s = Story(id=int(f))
    return s

def ffdownload(): # basic copy of ffdownload script in repo, for easier inclusion in package
    parser = argparse.ArgumentParser(prog="ffdownload",description='Download stories from fanfiction.net')

    parser.add_argument('fictions', metavar='STORY', type=str, nargs='+', help='Story / stories to download.')
    parser.add_argument('-o', '--output', dest='output', metavar='OUTPUT', type=str, nargs=1, help='Output directory. Default is the current directory.')
    parser.add_argument('-t', '--filetype', dest='extension', metavar='EXT', default='PDF', type=str, nargs='?', help='Filetype to download as. Default is PDF. Options are PDF, MOBI, EPUB, TXT.')
    parser.add_argument('-n', '--no-message', dest='messages', help='Don\'t show messages', action='store_false')
    parser.add_argument('-f', '--file', dest='treat_as_file', help='Treat STORY arguments as files which list stories.', action='store_true')
    args = parser.parse_args()
    extension = args.extension
    fictions = args.fictions
    messages = args.messages
    output = args.output
    file = args.treat_as_file
    # get stories
    stories = []
    if file:
        for f in fictions:
            o = open(f, 'r+')
            for line in o.read():
                s = _get_story(line)
                stories.append(s)
            o.close()
    else:
        for f in fictions:
            s = _get_story(f)
            stories.append(s)
    # deal with output
    if output != None:
        output = output[0]
        if not output.endswith('/'):
            output = output + '/'
        if not os.path.isdir(output):
            os.makedirs(output)
    else:
        output = './'
    for story in stories:
        download(story, output="%s%s-%s" % (output, story.title.replace(' ', '_'), story.author.replace(' ', '_')), message=messages, ext=extension)
