def kira_kuboid(panjang, lebar, tinggi):
    isipadu_kuboid = panjang * lebar * tinggi
    return isipadu_kuboid

def main():
    a = float(input("Masukkan panjang: "))
    b = float(input("Masukkan lebar: "))
    c = float(input("Masukkan tinggi: "))
    isipadu_kuboid = kira_kuboid(a, b, c)
    print(f"Isipadu kuboid = {isipadu_kuboid}")

if __name__ == "__main__":
    main()