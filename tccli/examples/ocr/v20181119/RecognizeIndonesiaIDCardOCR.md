**Example 1: RecognizeIndonesiaIDCardOCR**



Input: 

```
tccli ocr RecognizeIndonesiaIDCardOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
    --ReturnHeadImage false
```

Output: 
```
{
    "Response": {
        "Agama": "ATHOLIK",
        "Alamat": "BANJARSARI",
        "BerlakuHingga": "SEUMUR HIDUP",
        "GolDarah": "O",
        "IssuedDate": "15-05-2015",
        "JenisKelamin": "LAKEI AKI",
        "Kecamatan": "",
        "KelDesa": "PAKEMBINANGUN",
        "KewargaNegaraan": "INM",
        "NIK": "360000000006",
        "Nama": "",
        "Perkerjaan": "KARYAWAN SWASTA",
        "Photo": "",
        "RTRW": "00/000",
        "RequestId": "0000-0000-0000-0001",
        "StatusPerkawinan": "KAWFN",
        "TempatTglLahir": "JAKARTA 13-01-1987"
    }
}
```

