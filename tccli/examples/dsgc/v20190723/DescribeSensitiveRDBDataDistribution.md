**Example 1: 数据资产报告-查询rdb的敏感数据分布**

接口调用示例

Input: 

```
tccli dsgc DescribeSensitiveRDBDataDistribution --cli-unfold-argument  \
    --DspaId dspa-a1b2c3 \
    --ComplianceId 0 \
    --AssetList.0.DataSourceType cdb \
    --AssetList.0.DataSourceInfo.0.DataSourceId cdb-a1b2c3 \
    --AssetList.0.DataSourceInfo.0.BindList asset
```

Output: 
```
{
    "Response": {
        "LevelDistribution": [
            {
                "Key": "high",
                "Value": 0
            }
        ],
        "CategoryDistribution": [
            {
                "Key": "个人信息",
                "Value": 5
            }
        ],
        "RuleDistribution": [
            {
                "RuleId": 1,
                "RuleName": "个人信息泄漏",
                "LevelId": 3,
                "LevelName": "高风险",
                "RuleCnt": 2
            }
        ],
        "SensitiveDataNum": 0,
        "RequestId": "9f266ea1-30b1-4941-b513-417660be5e64"
    }
}
```

