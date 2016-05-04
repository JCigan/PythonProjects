#Program which checks for files which have been modified with the past 24
#hours and copies them to different folder

import os
import datetime
import shutil

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

def modified_within_day(filename):
    if modification_date(filename) + datetime.timedelta(1) >= datetime.datetime.now():
        return True
    else:
        return False

def copy_file(filename, source, destination):
    shutil.copyfile(source + filename, destination + filename)

def file_transfer():
    source = 'C:/Users/Student/Desktop/AllFiles/'
    destination = 'C:/Users/Student/Desktop/RecentFiles/'
    source_files = os.listdir(source)
    for files in source_files:
        if modified_within_day(source + files) == True:
            copy_file(files, source, destination)
            print 'Moved file: ' + files

def main():
    print 'Daily File Transfer Program - runs at 10:30am daily.'
    if datetime.datetime.now().time().hour == 10 and \
       datetime.datetime.now().time().minute == 30 and \
       datetime.datetime.now().time().second == 0:
        file_transfer()
    else:
        answer = raw_input('It is not 10:30am now. Run anyway? y or n: ')
        if answer == 'y' or answer == 'Y':
            file_transfer()
        else:
            print 'Goodbye!'

if __name__ == "__main__": main()
