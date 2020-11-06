**Example 1: 获取产品列表**

获取产品列表

Input: 

```
tccli iotexplorer GetStudioProductList --cli-unfold-argument  \
    --ProjectId prj-zunfat46 \
    --DevStatus dev \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "Products": [
            {
                "ProductId": "4GDIU5HTEN",
                "ProductName": "testproduct",
                "CategoryId": 3,
                "ProductType": 0,
                "EncryptionType": "2",
                "NetType": "else",
                "DataProtocol": 1,
                "ProductDesc": "desc",
                "ProjectId": "prj-zunfat46",
                "DevStatus": "dev",
                "CreateTime": 1560341825,
                "UpdateTime": 1560341825,
                "Region": "gz",
                "ModuleId": 0
            },
            {
                "ProductId": "BJQM4UXMKN",
                "ProductName": "testtproduct",
                "CategoryId": 3,
                "ProductType": 0,
                "EncryptionType": "2",
                "NetType": "else",
                "DataProtocol": 1,
                "ProductDesc": "desc",
                "ProjectId": "prj-zunfat46",
                "DevStatus": "dev",
                "CreateTime": 1560341975,
                "UpdateTime": 1560341975,
                "Region": "gz",
                "ModuleId": 0
            }
        ],
        "RequestId": "55e612b3-ed75-44fe-b141-1c1a35d9a0da",
        "Total": 2
    }
}
```

