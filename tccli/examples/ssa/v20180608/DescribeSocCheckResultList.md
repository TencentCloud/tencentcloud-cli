**Example 1: 配置检测详情列表**



Input: 

```
tccli ssa DescribeSocCheckResultList --cli-unfold-argument  \
    --Filter.0.FilterValue 1023115 \
    --Filter.0.FilterOperatorType 1 \
    --Filter.0.FilterKey  PloyId \
    --PageIndex 1 \
    --PageSize 3 \
    --Sorter.0.SortType 1 \
    --Sorter.0.SortKey RiskCount
```

Output: 
```
{
    "Response": {
        "Data": {
            "NormalTotal": 124,
            "MiddleTotal": 72,
            "Total": 269,
            "LowTotal": 20,
            "HighTotal": 53,
            "List": [
                {
                    "TotalAssetNum": 7,
                    "FailAssetNum": 0,
                    "Name": "关系型数据库-MariaDB应该启用备份",
                    "Result": "正常",
                    "PloyName": "腾讯云默认安全规范检查",
                    "PloyId": 1022732,
                    "Type": "数据安全",
                    "CheckId": "00fe63c2-94c7-11ea-89eb-6c92bf621820",
                    "DealUrl": "",
                    "AssetType": "mariadb"
                },
                {
                    "TotalAssetNum": 32,
                    "FailAssetNum": 0,
                    "Name": "CLB不应转发高危端口",
                    "Result": "正常",
                    "PloyName": "腾讯云默认安全规范检查",
                    "PloyId": 1022732,
                    "Type": "网络访问控制",
                    "CheckId": "12a8e83e-ddbd-4bb4-8d87-88da71facedf",
                    "DealUrl": "",
                    "AssetType": "clb"
                },
                {
                    "TotalAssetNum": 8,
                    "FailAssetNum": 0,
                    "Name": "Nosql数据库-Redis应该开启自动备份",
                    "Result": "正常",
                    "PloyName": "腾讯云默认安全规范检查",
                    "PloyId": 1022732,
                    "Type": "数据安全",
                    "CheckId": "3c6d8565-94c4-11ea-89eb-6c92bf621820",
                    "DealUrl": "",
                    "AssetType": "redis"
                }
            ]
        },
        "RequestId": "8e668163-32f4-4a77-b248-9b14cbee1232"
    }
}
```

