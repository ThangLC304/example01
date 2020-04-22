#Phan mem quan li khach san
csdl = {}
def nhap_lieu():
    ten = input('Nhap ten khach hang: ')
    tuoi = input('Tuoi: ')
    job = input('Nghe nghiep: ')
    du_lieu = [tuoi, job]
    csdl[ten] = du_lieu

def tim_kiem():
    ten = input('Nhap ten khach hang can tim: ')
    if ten not in csdl:
        print('Khong co khac hang tren!')
    else:
        print(ten, csdl[ten])

nhap_lieu()
tim_kiem()

