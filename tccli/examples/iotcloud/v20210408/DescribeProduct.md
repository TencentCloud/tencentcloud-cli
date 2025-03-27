**Example 1: 查看产品详情示例**



Input: 

```
tccli iotcloud DescribeProduct --cli-unfold-argument  \
    --ProductId UTY6QRLMQY
```

Output: 
```
{
    "Response": {
        "ProductId": "UTY6QRLMQY",
        "ProductMetadata": {
            "CreateUserId": 630811165,
            "CreationDate": 1740475425,
            "UserId": 630811165
        },
        "ProductName": "dev02",
        "ProductProperties": {
            "AppEUI": "",
            "DeviceLimit": 0,
            "EncryptionType": "1",
            "ForbiddenStatus": 0,
            "Format": "json",
            "ModelId": "-1",
            "ModelName": "",
            "OriginProductId": "",
            "OriginUserId": "1034534234",
            "Platform": "DEFAULT",
            "PrivateCAName": "",
            "ProductDescription": "",
            "ProductKey": "",
            "ProductSecret": "",
            "ProductType": 0,
            "Region": "",
            "RegisterLimit": 10000,
            "RegisterType": 0
        },
        "RequestId": "e2e44a73-6612-4355-88cf-b8a35041ac10"
    }
}
```

