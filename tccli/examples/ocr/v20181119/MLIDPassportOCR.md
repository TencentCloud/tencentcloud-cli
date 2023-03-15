**Example 1: 护照识别（港澳台地区及境外护照）示例代码[前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Action=MLIDPassportOCR)**

护照识别（港澳台地区及境外护照）

Input: 

```
tccli ocr MLIDPassportOCR --cli-unfold-argument  \
    --ImageBase64 base64编码
```

Output: 
```
{
    "Response": {
        "AdvancedInfo": "{\"IssuingCountry\":{\"Confidence\":\"0.9500\"},\"Name\":{\"Confidence\":\"0.9500\"},\"ID\":{\"Confidence\":\"0.9500\"},\"Nationality\":{\"Confidence\":\"0.9500\"},\"DateOfBirth\":{\"Confidence\":\"0.9500\"},\"Sex\":{\"Confidence\":\"0.9500\"},\"DateOfExpiration\":{\"Confidence\":\"0.9500\"},\"Surname\":{\"Confidence\":\"0.9500\"},\"GivenName\":{\"Confidence\":\"0.9500\"},\"CodeSet\":{\"Confidence\":\"0.9995\"},\"CodeCrc\":{\"Confidence\":\"0.9997\"}}",
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
        "RequestId": "9c42cdcf-53df-445d-b45b-ea3eaaf2bb70",
        "Sex": "F",
        "Surname": "CARTER",
        "Warn": [
            -9102
        ]
    }
}
```

