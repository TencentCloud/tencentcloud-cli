**Example 1: 使用身份证照片Base64进行验证**



Input: 

```
tccli faceid CheckIdCardInformation --cli-unfold-argument  \
    --ImageBase64 <base64字符串> \
    --Config {"CopyWarn":true}
```

Output: 
```
{
    "Response": {
        "Address": "广东省xxxxxxxxxxxx",
        "Birth": "1995/8/6",
        "Description": "成功",
        "IdNum": "xxxxxxx",
        "Name": "洪**",
        "Nation": "汉",
        "RequestId": "eb10******579b9a",
        "Result": "FailedOperation.OcrWarningOccurred",
        "Sex": "男",
        "Sim": 98.819999694824,
        "Portrait": "zok/tK7k2bLjyJE",
        "Warnings": "-9101|-9106|-9104",
        "Quality": 0.0,
        "Encryption": {
            "Iv": "abc",
            "EncryptList": [
                "IdName"
            ],
            "CiphertextBlob": "abc"
        }
    }
}
```

