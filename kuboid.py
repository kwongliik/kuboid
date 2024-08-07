def kira_isipadu(x, y, z):
    isipadu_kuboid = x * y * z
    return isipadu_kuboid

def kuboid():
    a = float(input("Masukkan panjang: "))
    b = float(input("Masukkan lebar: "))
    c = float(input("Masukkan tinggi: "))
    isipadu = kira_isipadu(a, b, c)
    print(f"Isipadu kuboid = {isipadu}"))

# JANGAN ubah kod di bawah
if __name__ == "__main__":
    kuboid()
