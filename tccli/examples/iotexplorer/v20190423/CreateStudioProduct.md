**Example 1: 新建产品**



Input: 

```
tccli iotexplorer CreateStudioProduct --cli-unfold-argument  \
    --EncryptionType 1 \
    --DataProtocol 1 \
    --ProjectId prj-zunfat46 \
    --ProductName name \
    --ProductDesc desc \
    --NetType wifi \
    --ProductType 0 \
    --CategoryId 10
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
            "BindStrategy": 0,
            "CategoryId": 10,
            "ProductId": "xx"
        },
        "RequestId": "xx"
    }
}
```

