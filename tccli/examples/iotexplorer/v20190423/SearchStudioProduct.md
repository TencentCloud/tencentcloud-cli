**Example 1: 搜索产品**

搜索产品

Input: 

```
tccli iotexplorer SearchStudioProduct --cli-unfold-argument  \
    --ProjectId prj-zunfat46 \
    --DevStatus dev \
    --Offset 0 \
    --Limit 0 \
    --ProductName testtproduct
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Products": [
            {
                "ProductId": "productId",
                "ProductName": "name",
                "CategoryId": 593,
                "ProductType": 0,
                "EncryptionType": "2",
                "NetType": "wifi",
                "DataProtocol": 1,
                "ProductDesc": "",
                "ProjectId": "prj-wg9**b2",
                "DevStatus": "dev",
                "CreateTime": 1686100765,
                "UpdateTime": 1686100802,
                "Region": "gz",
                "ModuleId": 0,
                "EnableProductScript": "",
                "CreatorNickName": "name",
                "CreateUserId": 1,
                "BindStrategy": 0
            }
        ],
        "RequestId": "0935a11f-a172-4bd8-8bae-f143444aaff3"
    }
}
```

