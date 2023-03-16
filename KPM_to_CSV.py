import codecs
from argparse import ArgumentParser


class Websites:
    def __init__(self, name, url, login_name, login, password, comment):
        self.website = name
        self.url = url
        self.login_name = login_name
        self.login = login
        self.password = password
        self.comment = comment

    def prepare_print(self, delimiter, nordpass=False):
        if nordpass:
            res = self.website + delimiter + self.url + delimiter + self.login + delimiter + "\"" + self.password + "\"" + delimiter + "\"" + self.comment + "\""
        else:
            res = 'Websites' + delimiter + self.website + delimiter + self.url + delimiter + self.login_name + delimiter + self.login + delimiter + "\"" + self.password + "\"" + delimiter + "\"" + self.comment + "\""
        return res

class Applications:
    def __init__(self, app, login_name, login, password, comment):
        self.app = app
        self.login_name = login_name
        self.login = login
        self.password = password
        self.comment = comment

    def prepare_print(self, delimiter, nordpass=False):
        if nordpass:
            res = self.app + delimiter*2 + self.login + delimiter + "\"" + self.password + "\"" + delimiter + "\"" + self.comment + "\""
        else:
            res = 'Applications' + delimiter + self.app + delimiter +self.login_name + delimiter + self.login + delimiter + "\"" + self.password + "\"" + delimiter + "\"" + self.comment + "\""
        return res

class Note:
    def __init__(self, name, text):
        self.name = name
        self.text = text

    def prepare_print(self, delimiter, nordpass=False):
        if nordpass:
            res = self.name + delimiter*4 + "\"" + self.text + "\""
        else:
            res = 'Note' + delimiter + self.name + delimiter + "\"" + self.text + "\""
        return res


def main():

    argsParser = ArgumentParser(description='Kaspersky Password Manager conveter to CSV')
    argsParser.add_argument('-i', '--input_file', help='Kaspersky Password Manager export file')
    argsParser.add_argument('-o', '--output_file', default='converted_passwords.csv', type=str, help='Custom CSV file name')
    argsParser.add_argument('-n', '--nordpass', default=False, action='store_true', help='Convert to NordPass CSV')

    args = argsParser.parse_args()

    file = args.input_file
    documento = args.output_file
    nordpass = args.nordpass

    if file == None:
        argsParser.print_help()
        exit(1)
    
    delimiter = ';'
    websiteslist = []
    applicationslist = []
    noteslist = []
    fd = codecs.open(file, 'r', "utf-8")
    buf = fd.readline()

    #Start by reading Websites attributes until Applications section
    while buf !="Applications\n" :
        args = []
        
        ''' Header '''
        buf = fd.readline()
        if buf[:12] == "Website name":
            args.append(buf[14:-1])

            '''Website URL'''
            buf = fd.readline()
            args.append(buf[13:-1])

            '''Login name'''
            buf = fd.readline()
            args.append(buf[12:-1])

            '''Login'''
            buf = fd.readline()
            args.append(buf[7:-1])

            '''Password'''
            buf = fd.readline()
            args.append(buf[10:-1])

            '''Comment'''
            buf = fd.readline()
            buf = buf[:-1]
            buf_tmp = fd.readline()
            while buf_tmp != '\n':
                buf += ' \\r ' + buf_tmp[:-1]
                buf_tmp = fd.readline()
            args.append(buf[9:])

            websiteslist.append(Websites(*args))

    while buf!="Notes\n" :
        args = []
        
        ''' Header '''
        buf = fd.readline()
        if buf[:11] == "Application" :
            args.append(buf[13:-1])

            '''Login name'''
            buf = fd.readline()
            args.append(buf[12:-1])

            '''Login'''
            buf = fd.readline()
            args.append(buf[7:-1])

            '''Password'''
            buf = fd.readline()
            args.append(buf[10:-1])

            '''Comment'''
            buf = fd.readline()
            buf = buf[:-1]
            buf_tmp = fd.readline()
            while buf_tmp != '\n':
                buf += ' \\r ' + buf_tmp[:-1]
                buf_tmp = fd.readline()
            args.append(buf[9:])

            applicationslist.append(Applications(*args))
        
    while buf :
        args = []

        buf = fd.readline()
        if buf[:4] == "Name" :
            args.append(buf[6:-1])

            '''Text'''
            buf = fd.readline()
            buf = buf[:-1]
            buf_tmp = fd.readline()
            while buf_tmp != '\n':
                buf += ' \\r ' + buf_tmp[:-1]
                buf_tmp = fd.readline()
            args.append(buf[6:])
    
            noteslist.append(Note(*args))

    ''' csv '''
    '''Grupo'''

    fd = codecs.open(documento, 'wb', 'utf-8')

    if nordpass:
        fd.write("name;url;username;password;note;cardholdername;cardnumber;cvc;expirydate;zipcode;folder;full_name;phone_number;email;address1;address2;city;country;state\n")
    for aux in websiteslist:
        fd.write((aux.prepare_print(delimiter, nordpass)+'\n'))

    for aux in applicationslist:
        fd.write((aux.prepare_print(delimiter, nordpass)+'\n'))

    for aux in noteslist:
        fd.write((aux.prepare_print(delimiter, nordpass)+'\n'))

    print("Conversion finished - %d converted accounts" % (len(websiteslist)+len(applicationslist)+len(noteslist)))


if __name__ == '__main__':
    main()
