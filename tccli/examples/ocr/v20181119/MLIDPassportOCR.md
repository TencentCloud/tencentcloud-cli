**Example 1: 护照识别（港澳台地区及境外护照）示例代码[前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Action=MLIDPassportOCR)**



Input: 

```
tccli ocr MLIDPassportOCR --cli-unfold-argument  \
    --ImageBase64 base64编码
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
        "CodeSet": "P<CANBROWN<<BENJAMIN<<<<<<<<<<<<<<<<<<<<<<<<",
        "CodeCrc": "JK123488<3CAN8510168M2603298<<<<<<<<<<<<<<04",
        "RequestId": "0ee989d3-d064-45ec-bccb-63f5064247b4"
    }
}
```

