**Example 1: 搜索产品**

搜索产品

Input: 

```
tccli iotexplorer SearchStudioProduct --cli-unfold-argument  \
    --ProjectId prj-zunfat46 \
    --ProductName testtproduct \
    --Limit 0 \
    --Offset 0 \
    --DevStatus dev
```

Output: 
```
{
    "Response": {
        "Products": [
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
        "RequestId": "0935a11f-a172-4bd8-8bae-f143444aaff3",
        "Total": 1
    }
}
```

