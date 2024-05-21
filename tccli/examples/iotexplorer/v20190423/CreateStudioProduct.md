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
            "DevStatus": "1",
            "EncryptionType": "2",
            "DataProtocol": 1,
            "ProjectId": "0",
            "Region": "47",
            "ModuleId": 0,
            "EnableProductScript": "产品",
            "UpdateTime": 1,
            "ProductName": "name",
            "CreateUserId": 0,
            "ProductDesc": "备注",
            "NetType": "1",
            "ProductType": 0,
            "CreatorNickName": "name",
            "CreateTime": 1,
            "BindStrategy": 0,
            "CategoryId": 10,
            "ProductId": "id"
        },
        "RequestId": "tgb-0r89-4rcv"
    }
}
```

