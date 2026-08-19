**Example 1: 获取分类检测项列表**

获取分类检测项列表

Input: 

```
tccli csip DescribeBaselineCategoryItemList --cli-unfold-argument  \
    --MemberId mem-tencent-6*************29 \
    --ParentCategoryID 4 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ItemList": [
            {
                "AffectedVersionList": [],
                "Category": {
                    "CheckAssetType": "HOST",
                    "Description": "Redis 弱口令检测(Windows)",
                    "ID": 206,
                    "Name": "Redis 弱口令检测(Windows)"
                },
                "CheckObject": [
                    "HOST"
                ],
                "CustomItemID": 0,
                "DefaultValueList": [],
                "Description": "Redis 采用弱口令容易被黑客猜解从而获取数据权限，导致数据被黑客偷窃、删除等；Redis 高权限用户可导致系统失陷。",
                "FixSuggestion": "1. 打开 Redis 配置文件 redis.conf，找到 requirepass 参数，将注释删除，设置强密码；\n2. 如果 Redis 开启了 aclfile 鉴权，需要找到 aclfile 参数对应的文件，在文件中将弱密码更改为强密码；\n3. 重启 Redis 服务",
                "ID": 5396,
                "IsCustomConf": false,
                "Name": "Redis 弱口令检测(Windows)",
                "ReferenceLink": "",
                "RiskLevel": "HIGH",
                "RuleID": 14382,
                "SupportCustomValue": false,
                "SupportFix": false,
                "SystemCategory": {
                    "CheckAssetType": "HOST",
                    "Description": "弱口令",
                    "ID": 4,
                    "Name": "弱口令"
                },
                "WebEditParam": ""
            }
        ],
        "TotalCount": 20,
        "RequestId": "4e2c62bc-1ea1-4793-92d9-942a876f0eab"
    }
}
```

