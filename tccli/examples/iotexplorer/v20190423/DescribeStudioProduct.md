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
            "BindStrategy": 0,
            "DeviceCount": 1
        },
        "RequestId": "1c469fbf-d80c-4299-9b54-31340898b839"
    }
}
```

