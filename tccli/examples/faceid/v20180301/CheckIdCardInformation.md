**Example 1: 身份证人像照片验真成功示例**



Input: 

```
tccli faceid CheckIdCardInformation --cli-unfold-argument  \
    --ImageBase64 /9j/4AAQSkZJRg.....s97n//2Q \
    --Config {"CopyWarn":true}
```

Output: 
```
{
    "Response": {
        "Address": "北京市东城区景山前街4号紫禁城敬事房",
        "Birth": "1654/12/20",
        "Description": "成功",
        "Encryption": null,
        "IdNum": "11204416541220243X",
        "Name": "韦小宝",
        "Nation": "汉",
        "Portrait": "/9j/4AAQSk...m3Zt62P//Z",
        "Quality": 98,
        "RequestId": "8dc2b640-caad-4a13-ad8c-204d46d29fe1",
        "Result": "Success",
        "Sex": "男",
        "Sim": 99.76,
        "Warnings": ""
    }
}
```

**Example 2: 身份证人像照片验真失败示例**



Input: 

```
tccli faceid CheckIdCardInformation --cli-unfold-argument  \
    --ImageBase64 /9j/4AAQSkZJRg.....s97n//2Q \
    --Config {"CopyWarn":true}
```

Output: 
```
{
    "Response": {
        "Address": "北京市东城区景山前街4号紫禁城敬事房",
        "Birth": "1654/12/20",
        "Description": "出现OCR告警",
        "IdNum": "11204416541220243X",
        "Name": "韦小宝",
        "Nation": "满",
        "Portrait": "/9j/4AAQSk...Se/wDkf//Z",
        "Quality": 99,
        "Encryption": null,
        "RequestId": "6e6cfaad-3271-4eb1-a203-2866100eb283",
        "Result": "FailedOperation.OcrWarningOccurred",
        "Sex": "男",
        "Sim": 0,
        "Warnings": "-9101"
    }
}
```

