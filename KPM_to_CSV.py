import argparse


class Websites:
    def __init__(self, name, url, login, password, account):
        self.website = name
        self.url = url
        self.login = login
        self.password = password
        self.accountname = account

    def prepare_print(self, delimiter):
        return self.website + delimiter + self.url + delimiter + self.login + delimiter + self.password + self.accountname


class Applications:
    def __init__(self, app, login, password, account):
        self.app = app
        self.login = login
        self.password = password
        self.account = account

    def prepare_print(self, delimiter):
        return self.app + delimiter + self.login + delimiter + self.password + delimiter + self.account


class Note:
    def __init__(self, text):
        self.text = text


def main():
    file = 'Karsp.txt'
    websiteslist = []
    applicationslist = []
    notes = []

    fd = open(file, 'r')
    fd.readline()

    while True:
        args = []
        fd.readline()

        '''Website name'''
        buf = fd.readline()
        if buf == 'Applications\n':
            break

        args.append(buf[14:-1])

        '''Website URL'''
        buf = fd.readline()
        args.append(buf[13:-1])

        '''Login'''
        buf = fd.readline()
        args.append(buf[7:-1])

        '''Password'''
        buf = fd.readline()
        args.append(buf[10:-1])

        '''Account'''
        buf = fd.readline()
        args.append(buf[14:-1])

        websiteslist.append(Websites(*args))

        fd.readline()
        fd.readline()

    while True:
        args = []
        fd.readline()

        '''aplication name'''
        buf = fd.readline()

        if buf == 'Notes\n':
            break

        args.append(buf[13:-1])

        '''Login'''
        buf = fd.readline()
        args.append(buf[7:-1])

        '''Password'''
        buf = fd.readline()
        args.append(buf[10:-1])

        '''acount name'''
        buf = fd.readline()
        args.append(buf[14:-1])

        applicationslist.append(Applications(*args))

        fd.readline()
        fd.readline()

    while True:
        args = ''
        fd.readline()

        '''aplication name'''
        buf = fd.readline()

        while buf != '---\n':
            if buf is not '\n':
                args += buf
            buf = fd.readline()

        notes.append(Note(args))

    delimiter = ';'


if __name__ == '__main__':
    main()
