from urllib import  request

response = request.urlopen("http://www.baidu.com")
fi = open("project.txt","w")
page = fi.write(str(response.read()))
fi.close()


def getfile_fix(filename):
    return filename[filename.rfind('.') + 1:]


print(getfile_fix('runoob.txt'))