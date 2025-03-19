**Example 1: 获取产品列表（旧）**



Input: 

```
tccli iotcloud DescribeProducts --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Products": [
            {
                "ProductId": "UTY4QRLMQY",
                "ProductMetadata": {
                    "CreateUserId": 631833365,
                    "CreationDate": 1740475425,
                    "UserId": 0
                },
                "ProductName": "dev02",
                "ProductProperties": {
                    "AppEUI": "",
                    "DeviceLimit": 1000000,
                    "EncryptionType": "1",
                    "ForbiddenStatus": 0,
                    "Format": "json",
                    "ModelId": "-1",
                    "ModelName": "",
                    "OriginProductId": "",
                    "OriginUserId": 0,
                    "Platform": "DEFAULT",
                    "PrivateCAName": "",
                    "ProductDescription": "IotHub",
                    "ProductKey": "",
                    "ProductSecret": "",
                    "ProductType": 0,
                    "Region": "",
                    "RegisterLimit": 0,
                    "RegisterType": 0
                }
            },
            {
                "ProductId": "ODX4QWWUF1",
                "ProductMetadata": {
                    "CreateUserId": 631833365,
                    "CreationDate": 1740475291,
                    "UserId": 0
                },
                "ProductName": "dev01",
                "ProductProperties": {
                    "AppEUI": "",
                    "DeviceLimit": 1000000,
                    "EncryptionType": "2",
                    "ForbiddenStatus": 0,
                    "Format": "json",
                    "ModelId": "-1",
                    "ModelName": "",
                    "OriginProductId": "",
                    "OriginUserId": 0,
                    "Platform": "DEFAULT",
                    "PrivateCAName": "",
                    "ProductDescription": "",
                    "ProductKey": "",
                    "ProductSecret": "",
                    "ProductType": 0,
                    "Region": "",
                    "RegisterLimit": 0,
                    "RegisterType": 0
                }
            }
        ],
        "RequestId": "c70b3902-2b4e-4f2b-983f-765fd4aa0d88",
        "TotalCount": 2
    }
}
```

