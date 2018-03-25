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
        rootDir = sys.argv[1]
        cipher = sys.argv[2]
        rootDest = sys.argv[3]

        if not isDirectoryExist(rootDir):
            sys.exit('Inexistant input')
        elif not isDirectory(rootDir):
            file_encoding1(rootDir, cipher, rootDest)
            
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
                        file_encoding1(ifname, cipher,ofname)
if __name__ == '__main__':
    main()


