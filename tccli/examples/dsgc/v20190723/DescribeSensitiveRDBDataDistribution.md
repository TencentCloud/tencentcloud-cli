**Example 1: 示例**

接口调用示例

Input: 

```
tccli dsgc DescribeSensitiveRDBDataDistribution --cli-unfold-argument  \
    --DspaId abc \
    --ComplianceId 0 \
    --AssetList.0.DataSourceType abc \
    --AssetList.0.DataSourceInfo.0.DataSourceId abc \
    --AssetList.0.DataSourceInfo.0.BindList abc
```

Output: 
```
{
    "Response": {
        "LevelDistribution": [
            {
                "Key": "abc",
                "Value": 0
            }
        ],
        "CategoryDistribution": [
            {
                "Key": "abc",
                "Value": 0
            }
        ],
        "RuleDistribution": [
            {
                "RuleId": 0,
                "RuleName": "abc",
                "LevelId": 0,
                "LevelName": "abc",
                "RuleCnt": 0
            }
        ],
        "SensitiveDataNum": 0,
        "RequestId": "abc"
    }
}
```

