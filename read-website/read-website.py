# reads the content of a site and writes it a new file with custom name
import requests, sys

sys.argv

if len(sys.argv) > 1:
    res = requests.get(sys.argv[1]);
    if (res.status_code == 200):
        newFile = open(sys.argv[2] + '.txt', 'wb')
        for chunk in res.iter_content(100000):
            newFile.write(chunk)
    else:
        res.raise_for_status()
else:
    print('Usage: [url, name of file]')

