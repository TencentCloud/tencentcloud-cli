**Example 1: 检查项列表**



Input: 

```
tccli ssa DescribeSocCheckItemList --cli-unfold-argument  \
    --Filter.0.FilterValue 默认安全规范 \
    --Filter.0.FilterOperatorType 1 \
    --Filter.0.FilterKey Standard \
    --PageIndex 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Total": 49,
            "List": [
                {
                    "Type": "数据安全",
                    "Name": "关系型数据库-MariaDB应该启用备份",
                    "Standard": "默认安全规范,等级保护三级合规",
                    "IsFree": 2,
                    "CheckId": "00fe63c2-94c7-11ea-89eb-6c92bf621820",
                    "Level": 3,
                    "AssetType": "mariadb"
                },
                {
                    "Type": "数据安全",
                    "Name": "关系型数据库-Mysql应该启用备份",
                    "Standard": "默认安全规范,等级保护三级合规",
                    "IsFree": 2,
                    "CheckId": "0bef9efa-94c7-11ea-89eb-6c92bf621820",
                    "Level": 3,
                    "AssetType": "cdb"
                },
                {
                    "Type": "网络访问控制",
                    "Name": "CLB不应转发高危端口",
                    "Standard": "默认安全规范,等级保护三级合规",
                    "IsFree": 2,
                    "CheckId": "12a8e83e-ddbd-4bb4-8d87-88da71facedf",
                    "Level": 4,
                    "AssetType": "clb"
                },
                {
                    "Type": "数据安全",
                    "Name": "COS存储桶ACL公共权限不应该设置为公共读写",
                    "Standard": "默认安全规范,等级保护三级合规",
                    "IsFree": 2,
                    "CheckId": "17a5c13d-f95d-4065-8e7d-33b6b56e71b5",
                    "Level": 4,
                    "AssetType": "cos"
                },
                {
                    "Type": "数据安全",
                    "Name": "Nosql数据库-Redis应该开启自动备份",
                    "Standard": "默认安全规范,等级保护三级合规",
                    "IsFree": 2,
                    "CheckId": "3c6d8565-94c4-11ea-89eb-6c92bf621820",
                    "Level": 3,
                    "AssetType": "redis"
                },
                {
                    "Type": "监控告警",
                    "Name": "CLB绑定的证书应该在有效期内",
                    "Standard": "默认安全规范",
                    "IsFree": 2,
                    "CheckId": "4119efe5-35b7-4809-b047-eb29b78c4069",
                    "Level": 3,
                    "AssetType": "clb"
                },
                {
                    "Type": "数据安全",
                    "Name": "COS存储桶应配置合理的桶策略",
                    "Standard": "默认安全规范,等级保护三级合规",
                    "IsFree": 2,
                    "CheckId": "58ae4eaa-73f4-11ea-8657-6c92bf622ce2",
                    "Level": 4,
                    "AssetType": "cos"
                },
                {
                    "Type": "数据安全",
                    "Name": "COS存储桶应开启防盗链功能",
                    "Standard": "默认安全规范,等级保护三级合规",
                    "IsFree": 2,
                    "CheckId": "5d5e7b8a-7e2b-11ea-8657-6c92bf622ce2",
                    "Level": 3,
                    "AssetType": "cos"
                },
                {
                    "Type": "数据安全",
                    "Name": "COS存储桶应开启服务端加密",
                    "Standard": "默认安全规范,等级保护三级合规",
                    "IsFree": 2,
                    "CheckId": "5d7ab655-7e2b-11ea-8657-6c92bf622ce2",
                    "Level": 3,
                    "AssetType": "cos"
                },
                {
                    "Type": "数据安全",
                    "Name": "CBS应开启定期快照功能",
                    "Standard": "默认安全规范,等级保护三级合规",
                    "IsFree": 2,
                    "CheckId": "6d269c6f-37d3-426e-8f4e-6fe06f6a9f31",
                    "Level": 3,
                    "AssetType": "cbs"
                }
            ]
        },
        "RequestId": "f961981c-0ea3-4e08-b557-ee503ae37f1e"
    }
}
```

