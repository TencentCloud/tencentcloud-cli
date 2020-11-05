**Example 1: Recognizing passport issued in Hong Kong/Macao/Taiwan (China) or other countries/regions ([debugging tool](https://console.cloud.tencent.com/api/explorer?Product=ocr&Action=MLIDPassportOCR))**



Input: 

```
tccli ocr MLIDPassportOCR --cli-unfold-argument  \
    --ImageBase64 'Base64 encoding'
```

Output: 
```
{
    "Response": {
        "ID": "E6918C",
        "Name": "LIM HEG CHUN STEE",
        "IssuingCountry": "SGP",
        "Nationality": "SGP",
        "DateOfBirth": "",
        "Sex": "M",
        "DateOfExpiration": "230414",
        "Warn": [],
        "Image": "",
        "AdvancedInfo": "{\"IssuingCountry\":{\"Confidence\":\"0.9500\"},\"Name\":{\"Confidence\":\"0.9500\"},\"ID\":{\"Confidence\":\"0.9500\"},\"Nationality\":{\"Confidence\":\"0.9500\"},\"Sex\":{\"Confidence\":\"0.9500\"},\"DateOfExpiration\":{\"Confidence\":\"0.9500\"}}",
        "RequestId": "0ee989d3-d064-45ec-bccb-63f5064247b4"
    }
}
```

