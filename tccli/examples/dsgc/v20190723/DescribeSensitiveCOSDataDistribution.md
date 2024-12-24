**Example 1: 示例**

描述

Input: 

```
tccli dsgc DescribeSensitiveCOSDataDistribution --cli-unfold-argument  \
    --DspaId dspa-abcd1234 \
    --ComplianceId 1 \
    --AssetList.0.DataSourceType 1 \
    --AssetList.0.DataSourceInfo.0.DataSourceId cdb-ab2352sd \
    --AssetList.0.DataSourceInfo.0.BindList lxldb01
```

Output: 
```
{
    "Response": {
        "LevelDistribution": [
            {
                "Key": "高",
                "Value": 10
            }
        ],
        "CategoryDistribution": [
            {
                "Key": "个人信息",
                "Value": 30
            }
        ],
        "RuleDistribution": [
            {
                "RuleId": 106,
                "RuleName": "身份证",
                "LevelId": 102,
                "LevelName": "高",
                "RuleCnt": 3
            }
        ],
        "SensitiveDataNum": 9,
        "RequestId": "fagxc-23rs-f"
    }
}
```

