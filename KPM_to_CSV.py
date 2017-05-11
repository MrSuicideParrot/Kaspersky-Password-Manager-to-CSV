import argparse

def websiteParser(iterador, fdw):
    pala = next(iterador)

    while pala != 'Applications':
        str = 'Websites,'

        '''Website name'''
        str += pala[14:-1]

        pala = next(iterador)
        '''Website URL'''
        str += pala[13:-1]

        pala = next(iterador)
        '''Login'''
        str += pala[7:-1]

        pala = next(iterador)
        '''Password'''
        str += pala[10:-1]

        pala = next(iterador)
        '''Acount'''
        str += pala[14]

        fdw.write(str)

        next(iterador)
        next(iterador)
        next(iterador)
        pala = next(iterador)


def appParser(iterador, fdw):
    pala = next(iterador)

    while pala != 'Notes':
        str = 'Application,'


file = 'teste.txt'

output = 'password.csv'

fdr = open(file, 'r')

fdw = open(file, 'w')

fileIter = fdr.readlines()

line = next(fileIter)
if line == 'Websites':
    next(fileIter)
    websiteParser(fileIter, fdw)
    next(fileIter)
    next(fileIter)
    appParser(fileIter, fdw)