import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BkRLXlCXXAmKcUHA-yvpsh0pCe1pBeZ93vB247Hj0u2WSL6nY-I2mG0w8Ikjys8M4DUGBTpi-LhggGDbqlBkMnbKdPsqh2-TcboR5_XQfQsoq58XmWXfc7s7HAtNolAz1O_rVLHwLs4v'
    transferData = TransferData(access_token)

    file_from = 'C:\Users\Nolan\Downloads\c101'
    file_to = ''  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()