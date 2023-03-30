**Example 1: RecognizeIndonesiaIDCardOCR**

印尼身份证

Input: 

```
tccli ocr RecognizeIndonesiaIDCardOCR --cli-unfold-argument  \
    --ReturnHeadImage false \
    --ImageUrl https://xx/a.jpg
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
        "TempatTglLahir": "JAKARTA 13-01-1987",
        "Provinsi": "DKI JAKARTA",
        "Kota": "DKI JAKARTA"
    }
}
```

