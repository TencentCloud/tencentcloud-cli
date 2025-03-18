**Example 1: 创建产品**



Input: 

```
tccli iotcloud CreateProduct --cli-unfold-argument  \
    --ProductName dev-01 \
    --ProductProperties.ProductDescription adfsdd13 \
    --ProductProperties.EncryptionType 1 \
    --ProductProperties.Region gz \
    --ProductProperties.ProductType 1 \
    --ProductProperties.Format json
```

Output: 
```
{
    "Response": {
        "ProductId": "UTY5QRLMQY",
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
            "OriginUserId": 0,
            "Platform": "EQPOKD5111",
            "PrivateCAName": "",
            "ProductDescription": "",
            "ProductKey": "",
            "ProductSecret": "",
            "ProductType": 0,
            "Region": "",
            "RegisterLimit": 10000,
            "RegisterType": 0
        },
        "RequestId": "5186e731-d43c-43ef-956c-12ff9b0ce8f2"
    }
}
```

