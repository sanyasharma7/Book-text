import gdown

def download_file(drive_url):
    file_id = drive_url.split('/d/')[1].split('/')[0]
    direct_url = f'https://drive.google.com/uc?id={file_id}'
    output = 'book.pdf'
    gdown.download(direct_url, output, quiet=False)
    return output

if __name__ == "__main__":
    # Paste your shareable Drive link here
    drive_url = 'https://drive.google.com/file/d/1IKmiIWFSMmZ0AAKizSjbMYJNIgwwmqnm/view?usp=drivesdk'
    download_file(drive_url)
  
