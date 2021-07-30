#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'hjB6lXQRXqYAAAAAAAAAAeDgmsykZEt8DAHP_xC7jVQCCQy2F8RBJUgJR5PKS78S'
    transferData = TransferData(access_token)

    file_from = 'C:/class-python/sample1.txt'
    file_to = '/PythonFolder4514/test01.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()