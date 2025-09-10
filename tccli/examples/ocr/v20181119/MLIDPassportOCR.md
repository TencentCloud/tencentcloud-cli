**Example 1: 护照识别（多国多地区护照）示例代码**

护照识别（多国多地区护照）

Input: 

```
tccli ocr MLIDPassportOCR --cli-unfold-argument  \
    --ImageBase64 https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/card/MLIDPassportOCR/MLIDPassportOCR1.png
```

Output: 
```
{
    "Response": {
        "AdvancedInfo": "",
        "CodeCrc": "4567123452USA9004117F2107268713843748<708026",
        "CodeSet": "P<USACARTER<<ESTHER<<<<<<<<<<<<<<<<<<<<<<<<<",
        "DateOfBirth": "19900411",
        "DateOfExpiration": "20210726",
        "GivenName": "ESTHER",
        "ID": "456712345",
        "Image": "",
        "IssuingCountry": "USA",
        "Name": "CARTER ESTHER",
        "Nationality": "USA",
        "PassportRecognizeInfos": {
            "DateOfBirth": "11 Apr 1990",
            "DateOfExpiration": "26 Jul 2021",
            "DateOfIssuance": "27 Jul 2011",
            "GivenName": "ESTHER",
            "IssuePlace": "",
            "IssuingAuthority": "",
            "IssuingCountry": "USA",
            "Name": "",
            "Nationality": "UNITED STATES OF AMERICA",
            "PassportID": "456712345",
            "Sex": "F",
            "Signature": "",
            "Surname": "CARTER",
            "Type": "P"
        },
        "RequestId": "dad946b2-1288-4df9-a0b4-6abfaba1e170",
        "Sex": "F",
        "Surname": "CARTER",
        "Type": "P",
        "Warn": [
            -9108,
            -9102
        ],
        "WarnCardInfos": [
            -9109
        ]
    }
}
```

