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
        "Total": 1,
        "Products": [
            {
                "DevStatus": "dev",
                "EncryptionType": "2",
                "DataProtocol": 1,
                "ProjectId": "prj-zunfat46",
                "Region": "gz",
                "EnableProductScript": "",
                "UpdateTime": 1560341975,
                "ProductName": "testtproduct",
                "ProductDesc": "desc",
                "NetType": "else",
                "ProductType": 0,
                "ModuleId": 0,
                "CreateTime": 1560341975,
                "CategoryId": 3,
                "CreateUserId": 0,
                "CreatorNickName": "xx",
                "ProductId": "BJQM4UXMKN"
            }
        ],
        "RequestId": "0935a11f-a172-4bd8-8bae-f143444aaff3"
    }
}
```

