#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import glob
from Crypto.Cipher import XOR

def XorCipher(key, plaintext):
    cipher_obj = XOR.new(key)
    cipher_obj = cipher_obj.encrypt(plaintext)
    return cipher_obj

def FileEncoding(path, key,  destination_path = None):

    with open(path, mode='rb') as i_file:
        plaintext = i_file.read()
    if destination_path == None :
        return XorCipher(key, plaintext)
    else :
        with open(destination_path, mode='xb') as o_file:
            o_file.write(XorCipher(key, plaintext))



def IsDirectory(d):
    
    if os.path.isdir(d) :
        return True
    else:
        return False

def IsDirectoryExist(d):
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

        if not IsDirectoryExist(path):
            sys.exit('Inexistant input')
        elif not IsDirectory(path):
            sys.stdout.buffer.write(FileEncoding(path, cipher, None))
        else:
            sys.exit('Missing arguments, required 3 at least')
    elif arguments == 4:
        rootDir = sys.argv[1]
        cipher = sys.argv[2]
        rootDest = sys.argv[3]

        if not IsDirectoryExist(rootDir):
            sys.exit('Inexistant input')
        elif not IsDirectory(rootDir):
            FileEncoding(rootDir, cipher, rootDest)
            
        else:
            for dirName, subdirList, fileList in os.walk(rootDir):
                if len(dirName) == len(rootDest):
                    destDir = dirName.replace(rootDir, rootDest)
                else:
                    newPath = dirName
                    newPath = newPath[len(rootDir):]
                    destDir = rootDest + newPath
                
                
                if not os.path.exists(destDir):
                    os.makedirs(destDir)
                    for fname in fileList:
                        ifname = os.path.join(dirName, fname)
                        ofname = os.path.join(destDir, fname)
                        FileEncoding(ifname, cipher,ofname)
if __name__ == '__main__':
    main()


