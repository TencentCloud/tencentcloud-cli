**Example 1: 获取产品详情**

获取产品详情

Input: 

```
tccli iotexplorer DescribeStudioProduct --cli-unfold-argument  \
    --ProductId M5AWDSEUYO
```

Output: 
```
{
    "Response": {
        "Product": {
            "ProductId": "M5AWDSEUYO",
            "ProductName": "testtproduct",
            "CategoryId": 3,
            "ProductType": 0,
            "EncryptionType": "2",
            "NetType": "else",
            "DataProtocol": 1,
            "ProductDesc": "desc",
            "ProjectId": "prj-zunfat46",
            "DevStatus": "dev",
            "EnableProductScript": "xx",
            "CreateTime": 1560341975,
            "UpdateTime": 1560341975,
            "Region": "gz",
            "ModuleId": 0,
            "CreateUserId": 1,
            "CreatorNickName": "test"
        },
        "RequestId": "1c469fbf-d80c-4299-9b54-31340898b839"
    }
}
```

