#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import glob
from Crypto.Cipher import XOR

def cipherb(key, plaintext):
    cipher_obj = XOR.new(key)
    cipher_obj = cipher_obj.encrypt(plaintext)
    return cipher_obj

def file_encoding1(path, key,  destination_path):
    
    with open(path, mode='rb') as i_file:
        plaintext = i_file.read()
    
    with open(destination_path, mode='xb') as o_file:
        o_file.write(cipherb(key, plaintext))
        



def file_encoding2(path, key):
    
    with open(path, mode='rb') as i_file:
        plaintext = i_file.read()
    return cipherb(key, plaintext)



def isDirectory(d):
    
    if os.path.isdir(d) :
        return True
    else:
        return False

def isDirectoryExist(d):
    if os.path.exists(d):
        return True
    else:
        return False

def main():
    arguments = len(sys.argv)
    

    if arguments < 3 :
        sys.exit('Missing arguments , at least 2 required arguments ')
    elif arguments == 3:
        path = sys.argv[1]
        cipher = sys.argv[2]

        if not isDirectoryExist(path):
            sys.exit('Inexistant input')
        elif not isDirectory(path):
            sys.stdout.buffer.write(file_encoding2(path, cipher))
        else:
            sys.exit('Missing arguments, required 3 at least')
    elif arguments == 4:
        path = sys.argv[1]
        cipher = sys.argv[2]
        destination_path = sys.argv[3]

        if not isDirectoryExist(path):
            sys.exit('Inexistant input')
        elif not isDirectory(path):
            file_encoding1(path, cipher, destination_path)
            
        else:
            for root, dirs, files in os.walk(path, topdown=False):
                for name in files:
                    iroot = os.path.join(root)
                    ifile = os.path.join(root, name)
                   
                    oroot = iroot.replace(path, destination_path)
                    oroot = '{0}'.format(oroot)
                    ofile = ifile.replace(path, destination_path)
                    

                    
                    if not os.path.exists(oroot):
                        os.makedirs(oroot)
                        file_encoding1(ifile, cipher,ofile)
if __name__ == '__main__':
    main()


