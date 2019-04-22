import os
os.chdir('d:\Anime\Ao Haru Ride')
#print(os.getcwd())

for f in os.listdir():

    f_name, f_ext = os.path.splitext(f)
    f_title, f_num = f_name.split('_')
    f_num = f_num.strip().zfill(2)
    name = f_title.split(' ')

    rename = '{}-{} {} {}{}'.format(f_num, name[1], name[2], name[3],f_ext)
    print(rename)

    os.rename(f,rename)
    
