**Example 1: 调用失败示例**



Input: 

```
tccli bda DetectBody --cli-unfold-argument  \
    --Url IamNotUrl
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.UrlIllegal",
            "Message": "URL格式不合法。"
        },
        "RequestId": "b5f77c78-efaf-42d1-b0ac-419cc70b4994"
    }
}
```

**Example 2: 调用成功示例**



Input: 

```
tccli bda DetectBody --cli-unfold-argument  \
    --Url test.jpg
```

Output: 
```
{
    "Response": {
        "BodyDetectResults": [
            {
                "BodyRect": {
                    "X": 260,
                    "Y": 1,
                    "Width": 272,
                    "Height": 365
                },
                "Confidence": 0.91490805149078
            }
        ],
        "BodyModelVersion": "1.0",
        "RequestId": "13ce6864-614a-4a9f-8207-c68fc9c552c4"
    }
}
```
