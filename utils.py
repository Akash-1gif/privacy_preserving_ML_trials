import base64

# write operation:
def write_data(file_name:str,data:bytes):
    data=base64.b64encode(data)
    with open(file_name,'wb') as f:
        f.write(data)

# read operation:
def read_data(file_name:str)->bytes:
    with open(file_name,'rb') as f:
        data=f.read()
    return base64.b64decode(data)