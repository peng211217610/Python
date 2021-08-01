from subprocess import PIPE, Popen

popen = Popen(
    'dir c:\\wsdwsadsds',
    stdout = PIPE,
    stderr = PIPE,
    shell=True,
    encoding='gbk')


output, err = popen.communicate()
print(output)
print('-------------------------------')
print(err)

