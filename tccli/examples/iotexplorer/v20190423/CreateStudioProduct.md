**Example 1: 新建产品**



Input: 

```
tccli iotexplorer CreateStudioProduct --cli-unfold-argument  \
    --ProductName name\
    --CategoryId 10\
    --ProductType 0\
    --EncryptionType 1\
    --NetType wifi\
    --DataProtocol 1\
    --ProductDesc desc\
    --ProjectId prj-zunfat46
```

Output: 
```
{
    "Response": {
        "Product": {
            "ProductId": "ROF2GLJ5FS",
            "ProductName": "name",
            "CategoryId": 10,
            "ProductType": 0,
            "EncryptionType": "1",
            "NetType": "wifi",
            "DataProtocol": 1,
            "ProductDesc": "desc",
            "ProjectId": "prj-zunfat46",
            "DevStatus": "dev",
            "CreateTime": 1557460361,
            "UpdateTime": 1557460361,
            "Region": "gz",
            "ModuleId": 0
        },
        "RequestId": "ef8a00e2-4166-4336-aa69-a2b5156d471f"
    }
}
```

