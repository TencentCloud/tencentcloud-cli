**Example 1: 获取产品OTA模块列表**



Input: 

```
tccli iotexplorer ListProductOtaModules --cli-unfold-argument  \
    --ProductID 8Q7X2QKV59
```

Output: 
```
{
    "Response": {
        "Modules": [
            {
                "CreateTime": 1753261941,
                "FwType": "default",
                "IsBuildIn": true,
                "Name": "",
                "ProductID": "8Q7X2QKV59",
                "ProductName": "ota测试",
                "Remark": ""
            },
            {
                "CreateTime": 1756953617,
                "FwType": "bms",
                "IsBuildIn": false,
                "Name": "",
                "ProductID": "8Q7X2QKV59",
                "ProductName": "ota测试",
                "Remark": ""
            }
        ],
        "RequestId": "2face868-8e90-4a42-98f9-54810ef3f1f8"
    }
}
```

