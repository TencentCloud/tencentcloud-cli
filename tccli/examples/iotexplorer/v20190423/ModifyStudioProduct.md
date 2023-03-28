**Example 1: 修改产品**

修改产品名称和描述等信息

Input: 

```
tccli iotexplorer ModifyStudioProduct --cli-unfold-argument  \
    --BindStrategy 1 \
    --ModuleId 0 \
    --ProductName testProduct \
    --ProductDesc Pdesc \
    --ProductId 4GDIU5HTEN
```

Output: 
```
{
    "Response": {
        "Product": {
            "DevStatus": "dev",
            "EncryptionType": "2",
            "DataProtocol": 1,
            "ProjectId": "prj-zunfat46",
            "Region": "gz",
            "ModuleId": 0,
            "EnableProductScript": "true",
            "UpdateTime": 1,
            "ProductName": "testProduct",
            "CreateUserId": 0,
            "ProductDesc": "test",
            "NetType": "else",
            "ProductType": 0,
            "CreatorNickName": "test",
            "CreateTime": 1,
            "CategoryId": 3,
            "BindStrategy": 0,
            "ProductId": "4GDIU5HTEN"
        },
        "RequestId": "1c469fbf-d80c-4299-9b54-31340898b839"
    }
}
```

