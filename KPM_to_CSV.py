import codecs


class Websites:
    def __init__(self, name, url, login_name, login, password, account):
        self.website = name
        self.url = url
        self.login_name = login_name
        self.login = login
        self.password = password
        self.accountname = account

    def prepare_print(self, delimiter):
        return 'Websites'+delimiter+self.website + delimiter + self.url + delimiter + self.login_name + delimiter + self.login + delimiter + self.password + delimiter +self.accountname


class Applications:
    def __init__(self, app, login_name, login, password, comment):
        self.app = app
        self.login_name = login_name
        self.login = login
        self.password = password
        self.comment = comment

    def prepare_print(self, delimiter):
        return 'Applications'+delimiter+self.app + delimiter +self.login_name + delimiter + self.login + delimiter + self.password + delimiter + self.comment


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
    
    while True:
        args = []
        
        ''' Header '''
        buf = fd.readline()
        if buf == 'Applications\r\n':
           break
        
        fd.readline()

        '''Website name'''
        buf = fd.readline()
        if buf == 'Applications\r\n' or  buf == 'Notes\r\n' or buf == '':
           break
        args.append(buf[14:-2])

        '''Website URL'''
        buf = fd.readline()
        args.append(buf[13:-2])

        '''Login name'''
        buf = fd.readline()
        args.append(buf[12:-2])

        '''Login'''
        buf = fd.readline()
        args.append(buf[7:-2])

        '''Password'''
        buf = fd.readline()
        args.append(buf[10:-2])

        '''Comment'''
        buf = fd.readline()
        args.append(buf[14:-2])

        if args == ['', '', '', '', '', '']:
            break

        websiteslist.append(Websites(*args))

        for aux in args:
            if delimiter in aux:
                need_to_chamge.append(websiteslist[-1])
                change = True
                break

        fd.readline()

    while True:
        args = []
        fd.readline()

        '''aplication name'''
        buf = fd.readline()

        if buf == 'Notes\r\n' or buf == '':
            break

        args.append(buf[13:-2])

        '''Login name'''
        buf = fd.readline()
        args.append(buf[12:-2])

        '''Login'''
        buf = fd.readline()
        args.append(buf[7:-2])

        '''Password'''
        buf = fd.readline()
        args.append(buf[10:-2])

        '''comment'''
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

        if buf == '':
            break

        while buf != '---\r\n':
            if buf != '\r\n':
                args += buf
            buf = fd.readline()

    notes.append(Note(args))

    if change:
        print("You need to change the following accounts:")
        for aux in need_to_chamge:
            print(aux.prepare_print(delimiter))
        return

    ''' csv '''
    '''Grupo'''
    documento = 'converted_passwords.csv'

    fd = codecs.open(documento, 'wb', 'utf-8')

    for aux in websiteslist:
        fd.write((aux.prepare_print(delimiter)+'\n'))

    for aux in applicationslist:
        fd.write((aux.prepare_print(delimiter)+'\n'))

    print("Conversion finished - %d converted accounts" % (len(websiteslist)+len(applicationslist)))


if __name__ == '__main__':
    main()
