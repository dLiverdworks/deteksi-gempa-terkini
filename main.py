"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    """
    Tanggal: 17 Mei 2023
    Waktu: 22:29:25 WIB
    Magnitudo: 4.6
    Kedalaman: 29 km
    Lokasi: LS=3.26 BT=135.30
    Pusat Gempa: Pusat gempa berada di darat 26 km BaratLaut Nabire
    Dirasakan: Dirasakan (Skala MMI): II - III Nabire
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '17 Mei 2023'
    hasil['waktu'] = '22:29:25 WIB'
    hasil['magnitudo'] = 4.6
    hasil['lokasi'] = {'ls': 3.26, 'bt': 135.30}
    hasil['pusat'] = 'Pusat gempa berada di darat 26 km BaratLaut Nabire'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II - III Nabire'

    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat Gempa {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)