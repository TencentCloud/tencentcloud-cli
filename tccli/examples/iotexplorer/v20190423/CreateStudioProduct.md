**Example 1: 新建产品**



Input: 

```
tccli iotexplorer CreateStudioProduct --cli-unfold-argument  \
    --ProductName name \
    --CategoryId 10 \
    --ProductType 0 \
    --EncryptionType 1 \
    --NetType wifi \
    --DataProtocol 1 \
    --ProductDesc desc \
    --ProjectId prj-zunfat46
```

Output: 
```
{
    "Response": {
        "Product": {
            "DevStatus": "xx",
            "EncryptionType": "xx",
            "DataProtocol": 1,
            "ProjectId": "xx",
            "Region": "xx",
            "ModuleId": 0,
            "EnableProductScript": "xx",
            "UpdateTime": 1,
            "ProductName": "xx",
            "CreateUserId": 0,
            "ProductDesc": "xx",
            "NetType": "xx",
            "ProductType": 0,
            "CreatorNickName": "xx",
            "CreateTime": 1,
            "CategoryId": 10,
            "ProductId": "xx"
        },
        "RequestId": "xx"
    }
}
```

