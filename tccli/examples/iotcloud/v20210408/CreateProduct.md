**Example 1: 创建产品**



Input: 

```
tccli iotcloud CreateProduct --cli-unfold-argument  \
    --ProductName fruit \
    --ProductProperties.ProductDescription test \
    --ProductProperties.EncryptionType 1 \
    --ProductProperties.Region gz \
    --ProductProperties.ProductType 0 \
    --ProductProperties.Format json
```

Output: 
```
{
    "Response": {
        "ProductId": "ABCDE12345",
        "ProductName": "fruit",
        "ProductProperties": {
            "ProductDescription": "test",
            "EncryptionType": 1,
            "Region": "gz",
            "ProductType": 0,
            "Format": "json",
            "Platform": "DEFAULT",
            "Appeui": ""
        },
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

