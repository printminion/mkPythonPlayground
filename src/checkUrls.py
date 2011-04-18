'''
Created on 15.04.2011

@author: m.kupriyanov
'''

import os, urllib

dirname = os.path.dirname(__file__) + '\\..\\data\\' 

print '[i]dowloading page'

urls = {'archer': {'url': 'http://gomiso.com/m/archer--2',
                   'search': 'Episode 13',
                   'preconnect': 0},
        'bobs-burgers': {'url': 'http://gomiso.com/m/bobs-burgers',
                         'search': 'Episode 11',
                         'preconnect': 0},
        'tbbt4':{'url': 'http://gomiso.com/m/the-big-bang-theory',
                 'search': 'Episode 21',
                 'preconnect': 0}
        }




for key in urls:
    
    #preconnect if needed
    if urls[key]['preconnect'] == 1:
        response = urllib.urlopen(urls[key]['url'])
        #print '[i]check ' + urls[key]['url']
        html = response.read()

    #download content
    response = urllib.urlopen(urls[key]['url'])
    print '[i]check ' + urls[key]['url']
    html = response.read()

    #print '[i]search:' + urls[key]['search']
    pos = html.find(urls[key]['search'])
    if pos > 0:
        
        #get end of the string
        #concatinate
        position = pos
        begin = pos - len(urls[key]['search'])
        
        #get begin of the string
        while position > 0:
                if html[position] == '"' or html[position] == '<' or html[position] == '>' or html[position] == ' ' or html[position] == '\n':
                    break;
                position = position - 1
        begin = position + 1

        #get end of the string
        position = pos + len(urls[key]['search'])
        while position <= len(html):
                if html[position] == '"' or html[position] == '<' or html[position] == '>' or html[position] == ' ' or html[position] == '\n':
                    break;
                position = position + 1
        end = position

        
        print '[!]found[' + str(begin) + ':' + str(end) + ']:' + html[begin: end]
        
    

    f = open(dirname + key + '.html', 'w')
    f.write(html)
    f.close()

print '[i]done'

if __name__ == '__main__':
    pass
