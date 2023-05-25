**Example 1: 韩国驾驶证识别**



Input: 

```
tccli ocr RecognizeKoreanDrivingLicenseOCR --cli-unfold-argument  \
    --ReturnHeadImage false \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Address": "충청북도 청주사 덕벌로41번길 21,B동 104호(내덕동, 학사촌)",
        "AptitudeTesDate": "2020.01.01~2020.12.31",
        "DateOfIssue": "2002.06.08",
        "ID": "3237ZX",
        "LicenseNumber": "북 12-011234-80",
        "Name": "HASU YUNG",
        "Number": "",
        "Photo": "",
        "RequestId": "1234-1234-1234-1234",
        "Sex": "xx",
        "Birthday": "xx",
        "Type": "1종통"
    }
}
```

