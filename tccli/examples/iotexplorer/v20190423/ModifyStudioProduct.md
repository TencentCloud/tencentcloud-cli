**Example 1: 修改产品**

修改产品名称和描述等信息

Input: 

```
tccli iotexplorer ModifyStudioProduct --cli-unfold-argument  \
    --ProductId 4GDIU5HTEN \
    --ProductName testProduct \
    --ProductDesc Pdesc \
    --ModuleId 0
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
            "CategoryId": 3,
            "ProductId": "xx"
        },
        "RequestId": "xx"
    }
}
```

