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
            "ProductId": "4GDIU5HTEN",
            "ProductName": "testProduct",
            "CategoryId": 3,
            "ProductType": 0,
            "EncryptionType": "2",
            "NetType": "else",
            "DataProtocol": 1,
            "ProductDesc": "Pdesc",
            "ProjectId": "prj-zunfat46",
            "DevStatus": "dev",
            "CreateTime": 1560341825,
            "UpdateTime": 1560414507,
            "Region": "gz",
            "ModuleId": 0
        },
        "RequestId": "6b6e765c-1625-49e6-9743-452e6ce15caa"
    }
}
```

