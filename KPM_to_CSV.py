import argparse
import codecs


class Websites:
    def __init__(self, name, url, login, password, account):
        self.website = name
        self.url = url
        self.login = login
        self.password = password
        self.accountname = account

    def prepare_print(self, delimiter):
        return 'Websites'+delimiter+self.website + delimiter + self.url + delimiter + self.login + delimiter + self.password + self.accountname


class Applications:
    def __init__(self, app, login, password, account):
        self.app = app
        self.login = login
        self.password = password
        self.account = account

    def prepare_print(self, delimiter):
        return 'Applications'+delimiter+self.app + delimiter + self.login + delimiter + self.password + delimiter + self.account


class Note:
    def __init__(self, text):
        self.text = text


def main():
    file = 'Karsp.txt'
    delimiter = ';'
    websiteslist = []
    applicationslist = []
    notes = []
    change = False
    need_to_chamge = []
    fd = codecs.open(file, 'r', "utf-8")
    fd.readline()

    while True:
        args = []
        fd.readline()

        '''Website name'''
        buf = fd.readline()
        if buf == 'Applications\r\n':
            break

        args.append(buf[14:-2])

        '''Website URL'''
        buf = fd.readline()
        args.append(buf[13:-2])

        '''Login'''
        buf = fd.readline()
        args.append(buf[7:-2])

        '''Password'''
        buf = fd.readline()
        args.append(buf[10:-2])

        '''Account'''
        buf = fd.readline()
        args.append(buf[14:-2])

        websiteslist.append(Websites(*args))

        for aux in args:
            if delimiter in aux:
                need_to_chamge.append(websiteslist[-1])
                change = True
                break

        fd.readline()
        fd.readline()

    while True:
        args = []
        fd.readline()

        '''aplication name'''
        buf = fd.readline()

        if buf == 'Notes\r\n':
            break

        args.append(buf[13:-2])

        '''Login'''
        buf = fd.readline()
        args.append(buf[7:-2])

        '''Password'''
        buf = fd.readline()
        args.append(buf[10:-2])

        '''acount name'''
        buf = fd.readline()
        args.append(buf[14:-2])

        applicationslist.append(Applications(*args))

        for aux in args:
            if delimiter in aux:
                need_to_chamge.append(applicationslist[-1])
                change = True
                break

        fd.readline()
        fd.readline()

    while True:
        args = ''
        fd.readline()

        '''notes name'''
        buf = fd.readline()

        if buf is '':
            break

        while buf != '---\r\n':
            if buf is not '\r\n':
                args += buf
            buf = fd.readline()

    notes.append(Note(args))

    if change:
        print("Necessita de mudar as seguintes contas!")
        for aux in need_to_chamge:
            print(aux.prepare_print(delimiter))
        return

    ''' csv '''
    '''Grupo'''
    documento = 'passes_prontas.csv'

    fd = codecs.open(documento, 'wb', 'utf-8')

    for aux in websiteslist:
        fd.write((aux.prepare_print(delimiter)+'\n'))

    for aux in applicationslist:
        fd.write((aux.prepare_print(delimiter)+'\n'))


if __name__ == '__main__':
    main()
