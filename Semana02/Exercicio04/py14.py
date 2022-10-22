import os

os.chdir('local do arquivo')

print(os.getcwd())

for f in os.listdir():
    print(f)
    print(os.path.splitext(f))
    file_name, file_ext = os.path.splitext(f)
    print(file_name.split('-'))
    ftitle, fcourse, fnum = file_name.split('-')
    print(fnum)
    ftitle = ftitle.strip()
    fcourse = fcourse.strip()
    fnum = fnum.strip()[1:].zfill(2)
    print('{}-{}-{}{}'.format(fnum,fcourse,ftitle,file_ext))
    newname = '{}-{}{}'.format(fnum,ftitle,file_ext)
    os.rename(f,newname)