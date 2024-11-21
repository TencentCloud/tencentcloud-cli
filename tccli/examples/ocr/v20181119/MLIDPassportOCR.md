**Example 1: 护照识别（港澳台地区及境外护照）示例代码[前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Action=MLIDPassportOCR)**

护照识别（港澳台地区及境外护照）

Input: 

```
tccli ocr MLIDPassportOCR --cli-unfold-argument  \
    --ImageBase64 https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/card/MLIDPassportOCR/MLIDPassportOCR1.png
```

Output: 
```
{
    "Response": {
        "AdvancedInfo": "{\"GivenName\":{\"Confidence\":\"1.0000\"},\"IssuingCountry\":{\"Confidence\":\"1.0000\"},\"Name\":{\"Confidence\":\"1.0000\"},\"Surname\":{\"Confidence\":\"1.0000\"},\"Type\":{\"Confidence\":\"1.0000\"},\"CodeSet\":{\"Confidence\":\"1.0000\"},\"CodeCrc\":{\"Confidence\":\"0.9995\"},\"Nationality\":{\"Confidence\":\"0.9995\"},\"ID\":{\"Confidence\":\"0.9995\"},\"Sex\":{\"Confidence\":\"0.9995\"},\"DateOfBirth\":{\"Confidence\":\"0.9995\"},\"DateOfExpiration\":{\"Confidence\":\"0.9995\"},\"PassportRecognizeInfos\":{\"IssuingCountry\":{\"Confidence\":\"1.0000\"},\"Type\":{\"Confidence\":\"0.9995\"},\"PassportID\":{\"Confidence\":\"0.9961\"},\"Surname\":{\"Confidence\":\"1.0000\"},\"GivenName\":{\"Confidence\":\"1.0000\"},\"Nationality\":{\"Confidence\":\"1.0000\"},\"DateOfBirth\":{\"Confidence\":\"1.0000\"},\"Sex\":{\"Confidence\":\"1.0000\"},\"DateOfIssuance\":{\"Confidence\":\"0.9997\"},\"DateOfExpiration\":{\"Confidence\":\"1.0000\"}}}",
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

