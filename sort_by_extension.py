'''
You are given a list of files.
You need to sort this list by the file extension. 
The files with the same extension should be sorted by name.

Some possible cases:
* Filename cannot be an empty string n != 0
* Files without the extension should go before the files with one
* Filename ".config" has an empty extension and a name ".config" n == 1
* Filename "config." has an empty extension and a name "config." n == 1
* Filename "no.config." has an empty extension and a name "no.config." n == 2
* Filename "table.imp.xls" has an extension "xls" and a name "table.imp" n == 3
* Filename ".imp.xls" has an extension "xls" and a name ".imp" n == 2
'''

def sort_by_ext(files: list) -> list:
    data = {'files': [],}
    output = []
    # build dict
    for f in files:
        # check if filename (f) contains an extension
        filestrip = f.strip('.')
        exttest = filestrip.split('.')[-1:][0]
        if len(exttest) > 0 and len(exttest) <=3 and len(filestrip.split('.')) > 1:
            # contains extension
            ext = f.split('.')[-1:][0]
            if ext in data:
                data[ext].append(f)
            else:
                data[ext] = [f,]
        else:
            # no extension
            data['files'].append(f)
    # create sorted list from dict
    if len(data['files']) > 0:
        output.extend(sorted(data.pop('files')))
    for d in sorted(data.keys()):
        output.extend(sorted(data[d]))
    return output

assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']

assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']

assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']

assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']

assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']

assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']

assert sort_by_ext([".config","my.doc","1.exe","345.bin","green.bat","format.c","no.name.","best.test.exe"]) == [".config","no.name.","green.bat","345.bin","format.c","my.doc","1.exe","best.test.exe"]

assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
