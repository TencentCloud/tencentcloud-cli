**Example 1: 获取OTA模块列表**



Input: 

```
tccli iotexplorer ListOtaModules --cli-unfold-argument  \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Modules": [
            {
                "CreateTime": 1756953617,
                "FwType": "bms",
                "IsBuildIn": false,
                "Name": "",
                "ProductID": "8Q7X2QKV59",
                "ProductName": "ota测试",
                "Remark": ""
            },
            {
                "CreateTime": 1756889779,
                "FwType": "mcu",
                "IsBuildIn": true,
                "Name": "",
                "ProductID": "SR5E1Q7C2A",
                "ProductName": "yufa",
                "Remark": ""
            },
            {
                "CreateTime": 1756889779,
                "FwType": "mcu",
                "IsBuildIn": true,
                "Name": "",
                "ProductID": "186XLZGJM5",
                "ProductName": "预发测试",
                "Remark": ""
            },
            {
                "CreateTime": 1756350539,
                "FwType": "default",
                "IsBuildIn": true,
                "Name": "",
                "ProductID": "SR5E1Q7C2A",
                "ProductName": "yufa",
                "Remark": ""
            }
        ],
        "RequestId": "c2862940-3dd8-4453-a8d8-31dacad30961",
        "TotalCount": 15
    }
}
```

